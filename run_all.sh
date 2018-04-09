#!/bin/bash
#
# Little helper to run all the scripts, under python coverage if coverage is available
#

set -eu
failed=""

if which coverage > /dev/null; then
    COVERAGE="`which coverage` run -a"
else
    COVERAGE=''
fi
for f in */[^_]*py; do
    PYTHONPATH=. python $COVERAGE $f || failed+=" $f"
    echo "I: done $f. Exit code $?"
done;

if [ ! -z "$failed" ]; then
    echo "Failed: $failed";
    exit 1
fi