#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import lupe

from setuptools import find_packages, setup

def open_file(filename):
    """Open and read the file *filename*."""
    with open(filename) as f:
        return f.read()


setup(
    name=lupe.__title__,
    author=lupe.__author__,
    author_email=lupe.__email__,
    version=lupe.__version__,
    url=lupe.__uri__,
    include_package_data=True,
    description='LUPE: a better cli app helper',
    project_urls={
        'Lupe source': 'https://github.com/19cah/lupe/',
    },
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
