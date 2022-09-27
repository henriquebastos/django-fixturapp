import os
import time
from fabric.api import *


def test(args=None):
    """
    Run tests. TestCase can be specified as argument:

        fab test
        fab test:fixturapp.FixturappLoadTests
    """
    if args is None:
        args = ""
    with cd(os.path.dirname(__file__)):
        local(f'./bin/django test {args} --verbosity=0', capture=False)


def _pep8(files):
    """
    Validates a list of files for PEP8 compliance.
    """
    result = []
    with cd(os.path.dirname(__file__)):
        for f in files:
            if f.endswith('.py'):
                if out := local(f"pep8 {f}"):
                    result.append(out)

    if result:
        print(''.join(result).rstrip())
        abort("Staged files did not pass PEP8 validation.")


def git_pre_commit():
    """
    Pre-commit hook for git. Just add the bellow script to
    .git/hooks/pre-commit:

        #!/bin/sh
        fab pre_commit
        code=$?
        exit $code
    """
    _pep8(local("git diff-index --name-only --cached HEAD -- ").splitlines())
    test()
