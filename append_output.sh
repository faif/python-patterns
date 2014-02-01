#!/bin/bash

set -e

src=$(sed -n -e "0,/### OUTPUT ###/p" "$1")
output=$(python "$1" | sed 's/^/# /')

echo -e "${src}\n${output}" > "$1"
