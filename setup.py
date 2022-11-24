import os

from setuptools import setup, find_packages

def readme() -> str:
    """Utility function to read the README.md.

    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.

    Args:
        nothing

    Returns:
        String of readed README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='leafydex',
    version='0.1.0',
    author=['Eshwaran Venkateswaran', 'Tigran Poladian'],
    author_email=['eshwaran@ischool.berkeley.edu', 'tpoladian@ischool.berkeley.edu'],
    description='Code, studies and explorations on plant leaf diseases and leaf type classifications for berkeley mids 207 final project',
    python_requires='>=3.10',
    license='BSD-3',
    url='https://github.com/cricksmaidiene/leafydex',
    packages=find_packages(),
    long_description=readme(),
)