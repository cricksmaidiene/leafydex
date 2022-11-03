# Multispecies Leaf Disease Classification 🍃
![Python version](https://img.shields.io/badge/python-v3.10-green)
    
![Python version](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
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
conda activate project_207
python -m ipykernel install --user --name=project_207
```

### For developers 👩🏽‍💻

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
    conda create --name project_207 python=3.10 -y
    conda activate project_207
    ```
    
* Clone the repository and install dependencies
    ```bash
    git clone https://github.com/cricksmaidiene/w207_final_project
    cd w207_final_project
    python -m pip install -r requirements.txt
    ```

* Add anaconda environment as a Jupyter Kernel
    ```bash
    conda install -c anaconda ipykernel -y
    python -m ipykernel install --user --name=project_207
    ```