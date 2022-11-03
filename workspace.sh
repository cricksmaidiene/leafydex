#!/bin/bash

# This script assumes that conda is available in PATH

echo "Creating Environment and Kernel for w207 project"

# environment setup stuff
conda env create -f environment.lock.yaml --force

# MODIFY CONDA PATH below based on location of conda
source /home/ubuntu/anaconda3/etc/profile.d/conda.sh
conda activate project_207

# jupyter kernel stuff
python --version
conda install -c anaconda ipykernel -y
python -m ipykernel install --user --name=project_207

# pre commit stuff
pnpm i
chmod ug+x .husky/*
chmod ug+x .git/hooks/*

# git clone stuff
git clone https://github.com/cricksmaidiene/w207_final_project
cd w207_final_project

# kaggle and data stuff
python -m pip install kaggle
mkdir ~/.kaggle
cp credentials/kaggle.json ~/.kaggle/kaggle.json
cd data
kaggle datasets download -d csafrit2/plant-leaves-for-image-classification
unzip plant-leaves-for-image-classification

echo "To remove the environment, run the following commands:"
echo "conda remove --name $conda_env_input"
echo "jupyter kernelspec remove $conda_env_input"
