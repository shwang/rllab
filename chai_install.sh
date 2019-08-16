#!/bin/bash
set -e
# Installs rllab on CHAI server
#
# Assumes that relevant apt-get packages from
# scripts/linux_setup.sh are already installed.
conda env create -f environment.yml
conda activate rllab
pip install -e .
