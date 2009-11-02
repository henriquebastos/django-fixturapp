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
        local('./bin/django test %s --verbosity=0' % args, capture=False)


def autotest(command=None, sleep=1):
    """
    Run autotest for a given test command.

    It considers the fabfile.py directory as the project root directory, then
    monitors changes in any inner python files.

    Usage:

        fab autotest:"manage.py test -v 0"

    This is based on Jeff Winkler's nosy script.
    """

    def checkSum():
        '''
        Return a long which can be used to know if any .py files have changed.
        Looks in all project's subdirectory.
        '''

        def hash_stat(file):
            from stat import ST_SIZE, ST_MTIME
            stats = os.stat(file)
            return stats[ST_SIZE] + stats[ST_MTIME]

        hash_ = 0
        for root, dirs, files in os.walk(os.path.dirname(__file__)):
            # We are only interested int python files
            files = [os.path.join(root, f) for f in files if f.endswith('.py')]
            hash_ += sum(map(hash_stat, files))
        return hash_

    if command is None:
        raise ValueError("Test command expected.")

    val = 0
    while(True):
        actual_val = checkSum()
        if val != actual_val:
            val = actual_val
            os.system(command)
        time.sleep(sleep)


def _pep8(files):
    """
    Validates a list of files for PEP8 compliance.
    """
    result = []
    with cd(os.path.dirname(__file__)):
        for f in files:
            if f.endswith('.py'):
                out = local("pep8 %s" % f)
                if out:
                    result.append(out)

    if result:
        print(''.join(result).rstrip())
        abort("Staged files did not pass PEP8 validation.")


def pre_commit():
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
