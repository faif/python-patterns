#!/bin/bash

set -e

src=$(sed -n -e '/### OUTPUT ###/,$!p' "$1")
output=$(python "$1" | sed 's/^/# /')

# These are done separately to avoid having to insert a newline, which causes
# problems when the text itself has '\n' in strings
echo "$src" > $1
echo -e "\n### OUTPUT ###" >> $1
echo "$output" >> $1
