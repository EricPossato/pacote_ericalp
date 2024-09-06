#!/usr/bin/env python3
from setuptools import setup

setup(name='dev_aberto_ericalp',
      version='0.1',
      packages=['dev_aberto'],
      scripts=['scripts/hello.py'],
      python_requires='>=3.12',
      install_requires=['requests', 'setuptools','wheel'],
      )