# Leafydex Package - Notebook Guide

- [Leafydex Package - Notebook Guide](#leafydex-package---notebook-guide)
  - [Module in Notebook](#module-in-notebook)
  - [Set up Git diff for notebooks and lab](#set-up-git-diff-for-notebooks-and-lab)
  - [Set up Plotly for Jupyterlab](#set-up-plotly-for-jupyterlab)
- [Invoke command](#invoke-command)

## Module in Notebook

To use the module inside your notebooks, add `%autoreload` at the top of your notebook :

```python
%load_ext autoreload
%autoreload 2
```

Example of module usage :

```python
from leafydex.utils.paths import data_dir
data_dir()
```

## Set up Git diff for notebooks and lab

We use [nbdime](https://nbdime.readthedocs.io/en/stable/index.html) for diffing and merging Jupyter notebooks.

To configure it to this git project :

```
nbdime config-git --enable
```

To enable notebook extension :

```
nbdime extensions --enable --sys-prefix
```

Or, if you prefer full control, you can run the individual steps:

```
jupyter serverextension enable --py nbdime --sys-prefix

jupyter nbextension install --py nbdime --sys-prefix
jupyter nbextension enable --py nbdime --sys-prefix

jupyter labextension install nbdime-jupyterlab
```

You may need to rebuild the extension : `jupyter lab build`

## Set up Plotly for Jupyterlab

Plotly works in notebook but further steps are needed for it to work in Jupyterlab :

- @jupyter-widgets/jupyterlab-manager # Jupyter widgets support
- plotlywidget  # FigureWidget support
- @jupyterlab/plotly-extension  # offline iplot support

There are conflict versions between those extensions so check the [latest Plotly README](https://github.com/plotly/plotly.py#installation-of-plotlypy-version-3) to ensure you fetch the correct ones.

```
jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.36 --no-build
jupyter labextension install plotlywidget@0.2.1  --no-build
jupyter labextension install @jupyterlab/plotly-extension@0.16  --no-build
jupyter lab build
```

# Invoke command

We use [Invoke](http://www.pyinvoke.org/) to manage an
unique entry point into all of the project tasks.

List of all tasks for project :

```
$ invoke -l

Available tasks:

  lab     Launch Jupyter lab
```

Help on a particular task :

```
$ invoke --help lab
Usage: inv[oke] [--core-opts] notebook [--options] [other tasks here ...]

Docstring:
  Launch Jupyter lab

Options:
  -i STRING, --ip=STRING   IP to listen on, defaults to *
  -p, --port               Port to listen on, defaults to 8888
```

You will find the definition of each task inside the `tasks.py` file, so you can add your own.
