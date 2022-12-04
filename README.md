# Multispecies Leaf Disease & Leaf Type Classification 🍃

![Python version](https://img.shields.io/badge/python-v3.10-green)

![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Anaconda](https://img.shields.io/badge/Anaconda-44A833.svg?style=for-the-badge&logo=Anaconda&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white)

![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Numpy](https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white)
![Tensorflow](https://img.shields.io/badge/TensorFlow-FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)

**Authors**

[Eshwaran Venkat](mailto:eshwaran@ischool.berkeley.edu) & [Tigran Poladian](mailto:tpoladian@ischool.berkeley.edu) under [Uri Schonfeld](mailto:shuri@ischool.berkeley.edu)

- [Multispecies Leaf Disease \& Leaf Type Classification 🍃](#multispecies-leaf-disease--leaf-type-classification-)
  - [Setup 📦](#setup-)
    - [:notebook: Requirements](#notebook-requirements)
    - [Local Setup](#local-setup)
    - [Use Github Codepsaces](#use-github-codepsaces)
  - [Dataset Setup 🛠](#dataset-setup-)
  - [Additional guides](#additional-guides)

## Setup 📦

### :notebook: Requirements

- `python@3.10`
- `conda` environment

### Local Setup

Assuming `conda` and `python` are available and are in `PATH` (accessible from anywhere on the system), run the following commands:

```bash
conda env create --name leafydex python=3.10 -y
conda activate leafydex

conda install -c anaconda ipykernel -y
python -m ipykernel install --user --name=leafydex

git clone https://github.com/cricksmaidiene/leafydex
cd leafydex
python -m pip install -r requirements.txt
python -m pip install -e .
```

### Use Github Codepsaces

- Go to the top-right corner of the repository and click `Code`
- Start a [github codespaces](https://docs.github.com/en/codespaces) on the `main` branch
- append `?editor=jupyter` of the codespaces URL to start exploring on Jupyterlab

## Dataset Setup 🛠

> Add Kaggle API key to `/credentials` (all files within this directory are ignored by git)

Instructions for UNIX-based systems (or Codespaces). Windows may require different commands

```bash
mkdir ~/.kaggle #ignore if directory already present
chmod 600 credentials/kaggle.json
cp credentials/kaggle.json ~/.kaggle/kaggle.json
python -m pip install kaggle
kaggle datasets download -d csafrit2/plant-leaves-for-image-classification -p ./data/raw
unzip data/raw/plant-leaves-for-image-classification.zip -d data/raw
rm data/raw/plant-leaves-for-image-classification.zip
```

- Get API key from [`https://www.kaggle.com/account`](https://www.kaggle.com/account)
- Review [Kaggle API Docs](https://www.kaggle.com/docs/api)

## Additional guides

- **Practices**: Please read [practices.md](practices.md) for details on how to set up this project beyond the base installation.

- **Structure**: Please read [structure.md](structure.md) to see the file structure of this project

- **Execution Trail**: Please read [trail.md](trail.md) to see the trail of execution across multiple files

---
Project structure based on the [cookiecutter conda data science project template](https://github.com/jvelezmagic/cookiecutter-conda-data-science).
