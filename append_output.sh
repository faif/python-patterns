#!/bin/bash

# This script (given path to a python script as an argument)
# appends python outputs to given file.

set -e

output_marker='OUTPUT = """'

# get everything (excluding part between `output_marker` and the end of the file)
# into `src` var
src=$(sed -n -e "/$output_marker/,\$!p" "$1")
output=$(python "$1")

echo "$src" > $1
echo -e "\n" >> $1
echo "$output_marker" >> $1
echo "$output" >> $1
echo '"""  # noqa' >> $1
