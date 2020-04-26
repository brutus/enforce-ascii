# Changelog

All notable changes to this project will be documented in this file. The format
is based on [Keep a Changelog][], and this project adheres to
[Semantic Versioning][].

You can find the **issue tracker** at:
<https://github.com/brutus/require-ascii/issues>

[keep a changelog]: https://keepachangelog.com/
[semantic versioning]: https://semver.org/

<!-- TOWNCRIER -->

## 0.2.0 (2020-04-26)

### Changes

- Quote non-ASCII tokens, to make whitespace more visible.

### Bugfixes

- Add `--build` flag to publish command.


## 0.1.0 (2020-04-26)

### Features

- Add support for [pre-commit](https://pre-commit.com/) hook.
- Initial `enforce-ascii` package on PyPi; with utility functions and command.
