# flake8: noqa
# pylint: skip-file

from setuptools import setup, find_packages

__version__ = None
exec(open("db_clustering/version_.py").read())

setup(
    name="db_clustering",
    python_requires=">=3.7",
    author="Valerie Schnapp",
    author_email="valerie.f.schnapp@gmail.com",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "matplotlib==3.1.1",
        "numpy==1.17.4",
        "scikit-learn==0.22.1",
        "scipy==1.3.1",
        "pytest==5.2.1",
        "jupyter==1.0.0",
    ],
    zip_safe=False,
    url="https://github.com/schnappv/density-based-clustering",
    description="A density based clustering algorithm for anomaly detection",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.7",
    ],
)
