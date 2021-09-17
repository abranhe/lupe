#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup.py file for lupe"""

from setuptools import setup

DESCRIPTION = 'The CLI helper you need 🥭'
LONG_DESCRIPTION = open("readme.md").read()

VERSION = '0.1.1'
URL = 'https://github.com/abranhe/lupe'

setup(
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url=URL,

    author='Abraham Hernandez',
    author_email='abraham@abranhe.com',
    license='MIT',

    classifiers=[
        'Intended Audience :: Developers'
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

        'Operating System :: OS Independent',
        'Operating System :: MacOS',
        'Operating System :: Unix',
    ],

    include_package_data=True,
    keywords='command line interface cli lupe',
)
