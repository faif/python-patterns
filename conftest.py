import sys


def pytest_ignore_collect(path):
    if sys.version_info[0] > 2:
        if str(path).endswith("__py2.py"):
            return True
    else:
        if str(path).endswith("__py3.py"):
            return True
