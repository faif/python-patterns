#!/usr/bin/env python3
"""
Script to generate a summary for GitHub Actions workflow.
Used to create a consistent summary at the end of the workflow.
"""
import os
import sys


def generate_summary(has_python_changes):
    """
    Generate a summary for GitHub Actions step summary.
    
    Args:
        has_python_changes: Boolean indicating if any Python files were changed
    """
    # Get the path to the GitHub step summary file
    summary_file = os.environ.get('GITHUB_STEP_SUMMARY')
    if not summary_file:
        print("GITHUB_STEP_SUMMARY environment variable not found.")
        return
    
    with open(summary_file, 'a') as f:
        f.write('## Pull Request Lint Results\n')
        if has_python_changes:
            f.write('Linting has completed for all Python files changed in this PR.\n')
            f.write('See individual job logs for detailed results.\n')
        else:
            f.write('No Python files were changed in this PR. Linting was skipped.\n')
        f.write('\n')
        f.write('⚠️ **Note:** This PR still requires manual approval regardless of linting results.\n')


if __name__ == "__main__":
    # Get whether there were Python changes from arguments
    has_python_changes = sys.argv[1].lower() == 'true' if len(sys.argv) > 1 else False
    
    # Generate the summary
    generate_summary(has_python_changes)