=====
Usage
=====

To use PatchIO in a project::

    import patchio


Command-Line Arguments
----------------------

You can use :func:`patch_args <patchio.patch_args>` to monkey patch command-line arguments.

This utility can be used as a context manager:

.. code-block:: python

    import sys
    with patch_args(["hello", "world"]) as args:
        assert " ".join(sys.argv[1:]) == "hello world"
        assert args == sys.argv


This utility can also be used as a decorator:

.. code-block:: python

    import sys
    @patch_args(["hello", "world"])
    def get_args():
        return sys.argv
    assert " ".join(get_args()) == "hello world"
