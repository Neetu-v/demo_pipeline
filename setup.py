from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="Neetu",
      author_email="neetudabas2@gmail.com",
      packages=find_packages(),
      install_requires=["pandas==2.0.3","numpy==1.23","flask==2.3.1"]
      )