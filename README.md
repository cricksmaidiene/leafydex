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

### For viewers 🔍

* Use the the anaconda environment lock file to setup.
* Add conda environment as jupyter kernel to run notebooks.

```bash
conda env create -f environment.lock.yaml --force
conda activate leafydex
python -m ipykernel install --user --name=leafydex
```

### For developers 👩🏽‍💻

#### :notebook: Requirements

- `python@3.10`
- `node@^16.17.1`
- `pnpm@^7.13.2`

#### Automatic Setup (Linux / Mac only) ⚙️

* Setup the workspace using `workspace.sh` file

    ```bash
    bash workspace.sh
    ```

    * Installs a conda environment with `python v3.10`
    * Adds the conda environment as a jupyter kernel to be used for notebooks
    * Downloads the project repository and installs necessary packages
    * Runs husky and pre-commit hooks

#### Manual Setup 🛠

* Setup conda environment with `python v3.10`
    ```bash
    conda env create -f environment.lock.yaml --force
    conda activate leafydex
    ```
* Add anaconda environment as a Jupyter Kernel
    ```bash
    conda install -c anaconda ipykernel -y
    python -m ipykernel install --user --name=leafydex
    ```
* Install additional python dependencies
    ```bash
    python -m pip install black pre-commit kaggle
    ```
* Install `node` dependencies and set [husky](https://typicode.github.io/husky/#/) as executable:
    ```bash
    pnpm i
    chmod ug+x .husky/*
    chmod ug+x .git/hooks/*
    ```

* Clone the repository (dependencies already installed through conda environment file)
    ```bash
    git clone https://github.com/cricksmaidiene/leafydex
    cd leafydex
    ```

* Download Kaggle dataset
    * Get API key from [`https://www.kaggle.com/account`](https://www.kaggle.com/account)
    * Review [Kaggle API Docs](https://www.kaggle.com/docs/api)
    * Add Kaggle API key to `leafydex/credentials` (all files within this directory are ignored by git)

    ```bash
    mkdir ~/.kaggle
    cp credentials/kaggle.json ~/.kaggle/kaggle.json
    cd data
    kaggle datasets download -d csafrit2/plant-leaves-for-image-classification
    unzip plant-leaves-for-image-classification
    ```
