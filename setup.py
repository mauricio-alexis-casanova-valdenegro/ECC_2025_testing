#!/usr/bin/env python3

from setuptools import setup

setup(
    name="ECC2025",
    version="0.1.8",
    description="ECC2025",
    url="https://github.com/MIROptics/ECC2025",
    author="Luciano Pereira",
    author_email="luciano.pereira.valenzuela@gmail.com",
    license="Apache 2.0",
    packages=["ECC2025"],
    package_dir={"ECC2025": "python_package"},
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy",
        "qiskit>=1.3.1,<1.4.0",
        "qiskit-aer>=0.16.0,<0.17.0",
        "qiskit_aer",
        "pylatexenc",
        "matplotlib",
        "scikit-learn",
        "pandas",
        "qiskit_algorithms",
        "seaborn",
        "tensorflow",
        "keras",
        "pyscf",
        "qiskit_nature",
        "qiskit-machine-learning>=0.7.0,<0.8.0",
        "qiskit-finance>=0.4.0,<0.5.0",
    ],
)
