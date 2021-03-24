#!/bin/bash

source /initialise_conda.sh

set -e  # Fail as soon as we detect an error

echo "Checking flake8 compliance"
flake8 ndscan test

echo "Checking yapf formatting"
yapf -d -r ndscan test

echo "Run the unit tests"
python -m unittest discover -v test
