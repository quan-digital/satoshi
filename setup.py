#!/usr/bin/env python
from setuptools import setup, find_packages
from os.path import join, dirname

here = dirname(__file__)

setup(name='satoshi',
      version='0.1.0',
      description='Manipulate satoshi-related prices in Python 3, simple and sweet.',
      long_description=open(join(here, 'README.md')).read(),
      author='canokaue',
      author_email='kaue.cano@quan.digital',
      url='https://github.com/quan-digital/satoshi/',
      install_requires=[
        'requests==2.23.0'
      ],
      packages=find_packages(),
      )