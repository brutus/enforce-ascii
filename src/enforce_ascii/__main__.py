import sys

from . import get_args
from . import run


def main():
    args = get_args()
    return run(*args.filenames, check=args.check)


if __name__ == "__main__":
    sys.exit(main())
