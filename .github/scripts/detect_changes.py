#!/usr/bin/env python3
"""
Script to detect changed Python files in a git repository.
Used by GitHub Actions workflow to determine which files to lint/test.
"""
import os
import subprocess
import sys


def get_changed_files(event_name, base_ref=None, before_sha=None, after_sha=None):
    """
    Get list of changed Python files based on git diff.
    
    Args:
        event_name: GitHub event name ('pull_request' or 'push')
        base_ref: Base branch for PR comparisons
        before_sha: Before SHA for push comparisons
        after_sha: After SHA for push comparisons
    
    Returns:
        tuple: (has_python_changes, changed_files)
    """
    # Determine the correct git diff command based on event type
    if event_name == 'pull_request':
        # For PRs, compare against base branch
        cmd = ['git', 'diff', '--name-only', '--diff-filter=ACMRT', f'origin/{base_ref}', 'HEAD']
    else:
        # For pushes, use the before/after SHAs
        cmd = ['git', 'diff', '--name-only', '--diff-filter=ACMRT', before_sha, after_sha]
    
    # Execute git command and get output
    result = subprocess.run(cmd, capture_output=True, text=True)
    all_changed_files = [f for f in result.stdout.strip().split('\n') if f]
    
    # Filter for Python files, excluding setup.py initially
    changed_files = [f for f in all_changed_files if f.endswith('.py') and f != 'setup.py']
    
    # Add setup.py only if it was actually changed
    if 'setup.py' in all_changed_files:
        changed_files.append('setup.py')
    
    # Check if we have any Python changes
    has_python_changes = len(changed_files) > 0
    
    return has_python_changes, changed_files


if __name__ == "__main__":
    # Get parameters from environment variables or command line
    event_name = os.environ.get('GITHUB_EVENT_NAME', sys.argv[1] if len(sys.argv) > 1 else None)
    base_ref = os.environ.get('GITHUB_BASE_REF', sys.argv[2] if len(sys.argv) > 2 else None)
    before_sha = os.environ.get('GITHUB_BEFORE', sys.argv[3] if len(sys.argv) > 3 else None)
    after_sha = os.environ.get('GITHUB_AFTER', sys.argv[4] if len(sys.argv) > 4 else None)
    
    # Get changed files
    has_changes, files = get_changed_files(event_name, base_ref, before_sha, after_sha)
    
    # Output for GitHub Actions
    if has_changes:
        print(f"::set-output name=has_python_changes::true")
        print(f"::set-output name=files::{' '.join(files)}")
        print("Changed Python files:", ' '.join(files))
    else:
        print("::set-output name=has_python_changes::false")
        print("::set-output name=files::")
        print("No Python files changed")