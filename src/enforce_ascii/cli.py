from __future__ import print_function

import argparse

from . import __description__
from . import __version__
from . import get_non_ascii_files
from . import get_non_ascii_words


def get_args(argv=None):
    ap = argparse.ArgumentParser(description=__description__)
    ap.add_argument("--version", action="version", version=__version__)
    ap.add_argument(
        "--check",
        action="store_true",
        help="return code is `1`, when non-ASCII files are found",
    )
    ap.add_argument(
        "filenames", nargs="+", metavar="FILENAME", help="path to the files to check"
    )
    args = ap.parse_args()
    return args


def run(*filenames, check=False):
    bad_encodings = get_non_ascii_files(*filenames)

    for filename, encoding in bad_encodings.items():
        words = get_non_ascii_words(filename)
        words = ", ".join((f"'{w}'" for w in sorted(words)))
        print(f"- {filename} ({encoding}): {words}")

    if bad_encodings and check:
        return 1
    else:
        return 0
