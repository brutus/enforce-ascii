"""
A pre-commit hook, that rejects files containing non ASCII characters.

"""

__version__ = "0.2.1"
__description__ = __doc__.strip().split("\n\n")[0]


from .utils import get_encoding  # noqa: 401
from .utils import get_non_ascii_files  # noqa: 401
from .utils import get_non_ascii_words  # noqa: 401
from .utils import is_ascii  # noqa: 401
from .cli import get_args  # noqa: 401
from .cli import run  # noqa: 401
