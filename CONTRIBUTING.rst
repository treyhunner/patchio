Contributing
============

Below is a list of tips for submitting issues and pull requests.  These are
suggestions and not requirements.

Submitting Issues
-----------------

Issues are often easier to reproduce/resolve when they have:

- A pull request with a failing test demonstrating the issue
- A code example that produces the issue consistently
- A traceback (when applicable)

Pull Requests
-------------

When creating a pull request, try to:

- Write tests if applicable
- Note important changes in the `CHANGES`_ file
- Update the `README`_ file if needed
- Update the documentation if needed
- Add yourself to the `AUTHORS`_ file
- Conform to `PEP8`_ for code contributions

.. _AUTHORS: AUTHORS.rst
.. _CHANGES: CHANGES.rst
.. _README: README.rst

Testing
-------

You will need `tox`_ and `coverage`_ installed to run the tests on your code:

.. code-block:: bash

    $ pip install tox coverage

To run the tests and generate a coverage report (in ``htmlcov`` directory):

.. code-block:: bash

    $ make test-all

**Please note**: Before a pull request can be merged, all tests must pass and
code/branch coverage in tests must be 100%.


.. _pep8: http://www.python.org/dev/peps/pep-0008/
.. _tox: http://testrun.org/tox/latest/
.. _coverage: https://pypi.python.org/pypi/coverage/
