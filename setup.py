#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
from io import open
import re
import sys

from setuptools import find_packages, setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

def open_file(filename):
    """Open and read the file *filename*."""
    with open(filename) as f:
        return f.read()


readme = open_file('README.md')


setup(
    name='lupe',
    author='Carlos Abraham',
    author_email='abraham@19cah.com',
    version=version,
    url='https://github.com/19cah/lupe',
    packages=find_packages(exclude=['docs', 'tests', 'tests.tabular_output']),
    include_package_data=True,
    description='LUPE: a better cli app helper',
    long_description=readme,
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3-ALPHA'
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Terminals :: CLI,
    ]
)
