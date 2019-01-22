import os
from setuptools import setup, find_packages


def read_requirements(fn):
    p = os.path.join(os.path.dirname(__file__), fn)

    with open(p, 'r') as f:
        return list(f.readlines())


setup(
    name='flask_hw',
    use_scm_version=True,
    author="Begin J Samuel <begin.samuel@hcl.com>",
    url="https://github.com/ERS-HCL/py-container",
    license="MIT",
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
    python_requires=">=3.6",
    setup_requires=["setuptools_scm", "wheel"])
