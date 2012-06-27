from fabric.api import *
from fabric.contrib.console import confirm

def test(app=""):
    """

    Tests the given app or the entire project.

    Example usage:

        $ fab test:app=polls

    This is also acceptable:

        $ fab test:polls

    If no app is given, the default is none. The entire project will be tested
    in this case.
    
    """

    local("python manage.py test %s" % app)
