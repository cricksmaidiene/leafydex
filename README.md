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

## Setup 📦

* Setup Locally

### :notebook: Requirements

* `python@3.10`
* `conda` environment

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
```

### Use Github Codepsaces

* Go to the top-right corner of the repository and click `Code`
* Start a [github codespaces](https://docs.github.com/en/codespaces) on the `main` branch
* append `?editor=jupyter` of the codespaces URL to start exploring on Jupyterlab

## Dataset Setup 🛠

> Add Kaggle API key to `leafydex/credentials` (all files within this directory are ignored by git)

Instructions for UNIX-based systems (or Codespaces). Windows may require different commands
```bash
mkdir ~/.kaggle #ignore if directory already present
chmod 600 credentials/kaggle.json
cp credentials/kaggle.json ~/.kaggle/kaggle.json
python -m pip install kaggle
cd data
kaggle datasets download -d csafrit2/plant-leaves-for-image-classification
unzip plant-leaves-for-image-classification
```

* Get API key from [`https://www.kaggle.com/account`](https://www.kaggle.com/account)
* Review [Kaggle API Docs](https://www.kaggle.com/docs/api)