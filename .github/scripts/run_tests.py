#!/usr/bin/env python3
"""
Script to run pytest on specific files based on changes.
Used by GitHub Actions workflow for PR testing.
"""
import os
import subprocess
import sys


def run_tests_for_changed_files(changed_files):
    """
    Run appropriate tests for the changed files.
    
    Args:
        changed_files: List of changed Python files
    """
    # Run test discovery first
    print("Running pytest discovery...")
    subprocess.run(['python', '-m', 'pytest', '--collect-only', '-v'])
    
    # Extract module paths from changed files
    print("Running tests for changed files...")
    modules = []
    for file in changed_files:
        if file.startswith('patterns/'):
            # Convert file path to module path (remove .py and replace / with .)
            module_path = file.replace('.py', '').replace('/', '.')
            modules.append(module_path)
    
    # Run tests for each module
    for module in modules:
        module_name = module.split('.')[-1]
        print(f"Testing module: {module}")
        subprocess.run(['python', '-m', 'pytest', '-xvs', 'tests/', '-k', module_name], 
                      check=False)
    
    # Then run doctests on the changed files
    print("Running doctests for changed files...")
    for file in changed_files:
        if file.endswith('.py'):
            print(f"Running doctest for {file}")
            subprocess.run(['python', '-m', 'pytest', '--doctest-modules', '-v', file], 
                         check=False)


if __name__ == "__main__":
    # Get list of changed files from arguments
    changed_files = sys.argv[1].split() if len(sys.argv) > 1 else []
    
    # Run the tests
    run_tests_for_changed_files(changed_files)