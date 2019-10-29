#!/bin/bash
#
# Little helper to run all the scripts, under python coverage if coverage is available
#

set -eu
failed=""

pytest --doctest-modules --cov=patterns
