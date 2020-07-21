# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Spyder Project Contributors
#
# Licensed under the terms of the MIT License
# (see LICENSE for details)
# -----------------------------------------------------------------------------
"""Setup script for three_merge."""

# Standard library imports
import ast
import os
import os.path as osp

# Third party imports
from setuptools import find_packages, setup

HERE = osp.dirname(osp.abspath(__file__))


def get_version(module='three_merge'):
    """Get version."""
    with open(os.path.join(HERE, module, '__init__.py'), 'r') as f:
        data = f.read()
    lines = data.split('\n')
    for line in lines:
        if line.startswith('VERSION_INFO'):
            version_tuple = ast.literal_eval(line.split('=')[-1].strip())
            version = '.'.join(map(str, version_tuple))
            break
    return version


def get_description():
    """Get long description."""
    with open(os.path.join(HERE, 'README.md'), 'r') as f:
        data = f.read()
    return data


REQUIREMENTS = [
    'diff-match-patch'
]

EXTRAS_REQUIRE = {
    'test': [
        'pytest',
        'pytest-cov',
        'flaky',
        'pytest-timeout'
    ]
}


setup(
    name='three-merge',
    version=get_version(),
    keywords=['Merge', 'Files', 'Three-way'],
    url='https://github.com/spyder-ide/three-merge',
    license='MIT',
    author='Spyder Project Contributors',
    author_email='spyder.python@gmail.com',
    description='Simple library for merging two strings with respect '
                'to a base one',
    long_description=get_description(),
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['contrib', 'docs']),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
        ],
    extras_require=EXTRAS_REQUIRE
    )
