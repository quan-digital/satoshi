#!/usr/bin/env python
from setuptools import setup, find_packages
from os.path import join, dirname

here = dirname(__file__)

setup(name='satoshi',
      version='0.1.3',
      description='Manipulate satoshi-related prices in Python 3, simple and sweet.',
      long_description=open(join(here, 'README.md')).read(),
      license='MIT',
      long_description_content_type="text/markdown",
      author='canokaue',
      author_email='kaue.cano@quan.digital',
      url='https://github.com/quan-digital/satoshi/',
      download_url = 'https://github.com/quan-digital/satoshi/dist/satoshi-0.1.3.tar.gz',
      install_requires=[
        'requests==2.23.0'
      ],
      packages=find_packages(),
      keywords = ['satoshi', 'satoshi-nakamoto', 'bitcoin', 'crypto-api', 'bitcoin-price', 'bitcoin-api', 
      'satoshi-price', 'digital-currency', 'fiat'],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
      ],
      include_package_data=True
      )