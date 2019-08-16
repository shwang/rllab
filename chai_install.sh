#!/usr/bin/env /bin/bash
set -e
# Installs rllab locally on CHAI server in conda environment `rllab3`.
#
# Assumes that relevant apt-get packages from
# scripts/linux_setup.sh are already installed.
conda env create -f environment.yml
eval "$(conda shell.bash hook)"
conda activate rllab3
pip install -e .
