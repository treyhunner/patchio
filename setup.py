#!/usr/bin/env python

from patchio import __version__


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='patchio',
    version=__version__,
    description="Python monkey-patching utilities",
    long_description=readme + '\n\n' + history,
    author="Trey Hunner",
    author_email='trey@treyhunner.com',
    url='https://github.com/treyhunner/patchio',
    packages=[
        'patchio',
    ],
    package_dir={'patchio':
                 'patchio'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='patchio',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
