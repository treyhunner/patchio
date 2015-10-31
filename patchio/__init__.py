from contextlib import ContextDecorator
import sys


__author__ = 'Trey Hunner'
__email__ = 'trey@treyhunner.com'
__version__ = '0.1.0'


class patch_args(ContextDecorator):

    """
    Context manager for patching ``sys.argv``.

    Usage::

        import sys
        with patch_args(["some_arg", "another_arg"]) as args:
            assert sys.argv == args
    """

    def __init__(self, args):
        """Save fake arguments and real arguments."""
        self.args = args
        self._old_values = []

    def __enter__(self):
        """Monkey patch ``sys.argv`` to use fake arguments."""
        self._old_values.append(sys.argv)
        sys.argv = self.args
        return sys.argv

    def __exit__(self, exc_type, exc_value, traceback):
        """Restore ``sys.argv`` to real argument values."""
        sys.argv = self._old_values.pop()
