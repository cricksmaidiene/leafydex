#!/bin/bash

# This script assumes that conda is available in PATH

read -p "Name of Environment: " conda_env_input
read -p "Auto Setup? (Press Enter to continue, any key otherwise) " auto_setup

python_ver_input="3.10"
project_input=""

if [[ -n "${auto_setup}" ]]; then
    read -p "Python Version in X.Y format:" python_ver_input
    read -p "Setup Repository? (Enter to continue, any other key otherwise): " project_input
fi

echo "Creating Environment and Kernel for: $conda_env_input with $python_ver_input"

conda create --name $conda_env_input python=$python_ver_input -y
source /home/ubuntu/anaconda3/etc/profile.d/conda.sh
conda activate $conda_env_input

python --version
conda install -c anaconda ipykernel -y
python -m ipykernel install --user --name=$conda_env_input

python -m pip install pandas tensorflow keras pillow opencv-python

if [[ -n "${project_input}" ]]; then
    echo "Skipping Project Setup"
else
    echo "Setting Project Repository"
    git clone https://github.com/cricksmaidiene/w207_final_project
fi

echo "To remove the environment, run the following commands:"
echo "conda remove --name $conda_env_input" 
echo "jupyter kernelspec remove $conda_env_input"
