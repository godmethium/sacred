#!/usr/bin/env python
# coding=utf-8
from setuptools import setup

classifiers = """
Development Status :: 5 - Production/Stable
Intended Audience :: Science/Research
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Topic :: Utilities
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Artificial Intelligence
Topic :: Software Development :: Libraries :: Python Modules
License :: OSI Approved :: MIT License
"""

try:
    from sacred import __about__
    about = __about__.__dict__
except ImportError:
    # installing - dependencies are not there yet
    # Manually extract the __about__
    about = dict()
    exec(open("sacred/__about__.py").read(), about)


setup(
    name='sacred',
    version=about['__version__'],

    author=about['__author__'],
    author_email=about['__author_email__'],

    url=about['__url__'],

    packages=['sacred', 'sacred.observers', 'sacred.config', 'sacred.stflow'],
    scripts=[],
    install_requires=[],
    tests_require=[],

    classifiers=list(filter(None, classifiers.split('\n'))),
    description='Facilitates automated and reproducible experimental research',
    long_description=open('README.rst').read()
)
