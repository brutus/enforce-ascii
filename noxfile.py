from pathlib import Path

import nox


PYTHON_VERSIONS = ["3.6", "3.7", "3.8"]

SOURCE_DIRECTORY = Path("src").resolve()
TEST_DIRECTORY = Path("tests").resolve()

TOOLS_TEST = [
    "pytest",
    ".",
]

nox.options.reuse_existing_virtualenvs = True


@nox.session(python=PYTHON_VERSIONS)
def test(session):
    """ Run pytest test suit for Python versions. """
    session.install(*TOOLS_TEST)
    args = session.posargs if session.posargs else [str(TEST_DIRECTORY)]
    session.run("pytest", *args)
