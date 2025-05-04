#!/usr/bin/env python3
"""
Script to generate a custom tox configuration for testing changed files.
Used by GitHub Actions workflow for PR testing.
"""
import os
import sys


def generate_tox_config(changed_files, output_file='tox_pr.ini'):
    """
    Generate a customized tox configuration for testing changed files.
    
    Args:
        changed_files: List of changed Python files
        output_file: Path to write the tox configuration to
    """
    with open(output_file, 'w') as tox_file:
        # Write tox section
        tox_file.write('[tox]\n')
        tox_file.write('envlist = py312\n')
        tox_file.write('skip_missing_interpreters = true\n\n')
        
        # Write testenv section
        tox_file.write('[testenv]\n')
        tox_file.write('setenv =\n')
        tox_file.write('    COVERAGE_FILE = .coverage.{envname}\n')
        tox_file.write('deps =\n')
        tox_file.write('    -r requirements-dev.txt\n')
        tox_file.write('allowlist_externals =\n')
        tox_file.write('    pytest\n')
        tox_file.write('    coverage\n')
        tox_file.write('commands =\n')
        
        # Always run a baseline test with coverage
        tox_file.write('    pytest -xvs --cov=patterns tests/ --cov-report=term-missing\n')
        
        # Add test commands for changed files
        tox_file.write('    # Run specific tests for changed files\n')
        
        for file in changed_files:
            if file.endswith('.py'):
                # Handle implementation files
                if file.startswith('patterns/'):
                    module_name = os.path.basename(file)[:-3]  # Remove .py extension
                    pattern_dir = os.path.dirname(file).split('/', 1)[1] if '/' in os.path.dirname(file) else ''
                    
                    tox_file.write(f'    # Testing {file}\n')
                    
                    # Check for specific test file and add it conditionally
                    test_file = f'tests/{pattern_dir}/test_{module_name}.py'
                    # Use conditional for test file
                    tox_file.write(f'    python -c "import os.path; test_path=\'{test_file}\'; print(f\'Test file {{test_path}} exists: {{os.path.exists(test_path)}}\')" \n')
                    tox_file.write(f'    pytest -xvs --cov=patterns --cov-append tests/{pattern_dir}/ -k "{module_name}"\n')
                
                # Run test files directly if modified
                if file.startswith('tests/'):
                    tox_file.write(f'    pytest -xvs --cov=patterns --cov-append {file}\n')
        
        # Run doctests on pattern files
        tox_file.write('    # Run doctests\n')
        for file in changed_files:
            if file.startswith('patterns/') and file.endswith('.py'):
                tox_file.write(f'    pytest --doctest-modules -v --cov=patterns --cov-append {file}\n')
        
        # Add coverage report commands
        tox_file.write('    coverage combine\n')
        tox_file.write('    coverage report\n')


if __name__ == "__main__":
    # Get list of changed files from arguments
    changed_files = sys.argv[1].split() if len(sys.argv) > 1 else []
    
    # Generate the tox configuration
    generate_tox_config(changed_files)
    
    # Print the configuration to stdout
    with open('tox_pr.ini', 'r') as f:
        print(f.read())