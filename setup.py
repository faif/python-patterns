# -*- encoding: utf-8 -*-

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='patterns',
    version='1.0.0',
    author='Sakis Kasampalis and Contributors',
    description='A collection of design patterns/idioms in Python.',
    long_description=read('README.md'),
    url='https://github.com/faif/python-patterns',
    keywords='design patterns, idioms',
    platforms=['any'],
    license='Apache Software License v2.0',
    packages=['patterns'],
    install_requires=[
        'six'
    ],
    extras_require={
        'dev': [
            'tox',
            'flake8',
            'coverage',
        ],
        'travis': [
            'python-coveralls',
        ]
    },
    test_suite='tests',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
