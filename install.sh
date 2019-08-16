# Installs rllab on CHAI server
# Assumes that relevant apt-get packages from
# scripts/linux_setup.sh are already installed.
conda env create create -f environment.yml
conda activate rllab
pip install -e .
yes | pip install mujoco_py
