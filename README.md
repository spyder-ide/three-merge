# three-merge
[![Project License - MIT](https://img.shields.io/pypi/l/three-merge.svg)](https://raw.githubusercontent.com/spyder-ide/three-merge/master/LICENSE)
[![pypi version](https://img.shields.io/pypi/v/three-merge.svg)](https://pypi.org/project/three-merge/)
[![conda version](https://img.shields.io/conda/vn/conda-forge/three-merge.svg)](https://www.anaconda.com/download/)
[![download count](https://img.shields.io/conda/dn/conda-forge/three-merge.svg)](https://www.anaconda.com/download/)
[![Downloads](https://pepy.tech/badge/three-merge)](https://pepy.tech/project/three-merge)
[![PyPI status](https://img.shields.io/pypi/status/three-merge.svg)](https://github.com/spyder-ide/three-merge)
![Linux tests](https://github.com/spyder-ide/three-merge/workflows/Linux%20tests/badge.svg)
![MacOS tests](https://github.com/spyder-ide/three-merge/workflows/MacOS%20tests/badge.svg)
![Windows tests](https://github.com/spyder-ide/three-merge/workflows/Windows%20tests/badge.svg)

*Copyright © 2020– Spyder Project Contributors*

## Overview
Simple Python library to perform a 3-way merge between strings, based on [diff-match-patch](https://github.com/google/diff-match-patch). This library performs merges at a character level, as opposed to most VCS systems, which opt for a line-based approach.


## Installing
To install three-merge, you can use both conda or pip package managers:

```bash
# Using conda (Recommended)
conda install three-merge -c spyder-ide

# Using pip
pip install three-merge
```

## Dependencies
This package depends on [diff-match-patch](https://github.com/google/diff-match-patch) to compute and track the differences across the source and target strings with respect to the base one.

## Installing locally
To install and develop three-merge locally, you will need to install diff-match-patch:

```bash
# Using conda
conda install diff-match-patch

# Using pip
pip install diff-match-patch
```

Then, you can install the package locally using pip:

```bash
pip install -U -e .
```

## Running tests
We use pytest to run tests as it follows:

```bash
pytest -x -v three_merge/tests
```

## Package usage
Three-merge provides a ``merge`` function to merge changes from two strings (source, target) with respect a original string (base). This library is able to handle additions, deletions and preserved sections across both strings, while detecting and highlighting possible merge conflicts (like Git).

```python
# Package import
from three_merge import merge

# Strings have non-conflicting additions
base = '123456789101112'
source = '0123456789101112'
target = '12345678910111213'

# merged = '012345678910111213'
merged = merge(source, target, base)

# Strings have an addition conflict
base = '123456789101112'
source = '123a456789101112'
target = '123b456789101112'

# merged = '123<<<<<<< ++ a ======= ++ b >>>>>>>456789101112'
merged = merge(source, target, base)

# Strings have non-conflicting addition/deletions
base = '123456789101112'
source = '123456789ab101112'
target = '123789101112'

# merged = '123789ab101112'
merged = merge(source, target, base)
```

For more examples, please take a look at our [tests](https://github.com/spyder-ide/three-merge/blob/master/three_merge/tests/test_merge.py).


## Changelog
Please see our [CHANGELOG](https://github.com/spyder-ide/three-merge/blob/master/CHANGELOG.md) file to learn more about our new features and improvements.


## Contribution guidelines
We follow PEP8 and PEP257 for all Python modules. We use MyPy type annotations for all functions and classes declared on this package. Feel free to send a PR or create an issue if you have any problem/question.

