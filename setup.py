#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup
from sys import version_info


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


def requirements():
    with open("requirements.txt", "r") as f:
        requirements = f.readlines()
    if version_info.major == 2:
        requirements.append("mock==2.0.0")
    return requirements


setup(
    name='pytest-automock',
    version='0.0.1',
    author='Daniel Papp',
    author_email='jakab922@gmail.com',
    maintainer='Daniel Papp',
    maintainer_email='jakab922@gmail.com',
    license='MIT',
    url='https://github.com/jakab922/pytest-automock',
    description='A module that automatically mocks out variables',
    long_description=read('README.rst'),
    py_modules=['pytest_automock'],
    install_requires=requirements(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'pytest_automock = pytest_automock.plugin',
        ],
    },
)
