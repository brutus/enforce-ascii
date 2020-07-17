# Enforce ASCII

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

**VERSION**: `0.2.1`

A Python package to find files containing non-ASCII encoded characters. If you
find any bugs, issues or anything, please use the [issue tracker][] on GitHub -
issues and PRs are welcome ❤️

## Install

It's on [PyPi] as `enforce-ascii`, you can install it with _pip_, _pipx_, etc.

```shell
pip install enforce-ascii
```

## Usage

```shell
$ enforce-ascii --help
usage: enforce-ascii [-h] [--version] [--check] FILENAME [FILENAME ...]

A pre-commit hook, that rejects files containing non ASCII characters.

positional arguments:
  FILENAME    path to the files to check

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
  --check     return code is `1`, when non-ASCII files are found
```

### Example

```shell
$ enforce-ascii tests/files/*/*.txt
- tests/files/bad/special.txt (Windows-1252): 'there…'
- tests/files/bad/umlaut.txt (utf-8): 'föur', 'käle', 'Åir'
```

## Pre-Commit

This can be used as a [pre-commit][] hook:

```yaml
- repo: https://github.com/brutus/enforce-ascii
  rev: v0.2.1
  hooks:
      - id: enforce-ascii
```

[issue tracker]: https://github.com/brutus/enforce-ascii/issues
[pre-commit]: https://pre-commit.com/
[pypi]: https://pypi.org/project/enforce-ascii/
