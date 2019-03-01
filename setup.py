#!/bin/env python3

"""
A John Shots - A tool to get the Security Hash Algorightms (SHA) of all file in a given path.

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Contributors:
    Let's contribute to A John Shots!

Project link:
    https://github.com/funilrys/A-John-Shots

License:
::

    MIT License

    Copyright (c) 2017-2019 Nissar Chababy

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

from re import compile as comp

from setuptools import setup


def _get_requirements():
    """
    This function extract all requirements from requirements.txt.
    """

    with open("requirements.txt") as file:
        requirements = file.read().splitlines()

    return requirements


def _get_version():
    """
    This function will extract the version from a_john_shots/__init__.py
    """

    to_match = comp(r'VERSION\s=\s"(.*)"\n')
    extracted = to_match.findall(
        open("a_john_shots/__init__.py", encoding="utf-8").read()
    )[0]

    return ".".join([x for x in extracted.split(".") if x.isdigit()])


def _get_long_description():
    """
    This function return the long description.
    """

    return open("README.rst", encoding="utf-8").read()  # pragma: no cover


setup(
    name="a-john-shots",
    version=_get_version(),
    description="A tool to get the Security Hash Algorightms (SHA) of all file in a given path.", # pylint: disable=line-too-long
    long_description=_get_long_description(),
    author="funilrys",
    author_email="contact@funilrys.com",
    license="MIT https://raw.githubusercontent.com/funilrys/A-John-Shots/master/LICENSE",
    url="https://github.com/funilrys/A-John-Shots",
    platforms=["any"],
    packages=["a_john_shots"],
    keywords=["Python", "JSON", "SHA-1", "SHA-512", "SHA-224", "SHA-384", "SHA", "MD5"],
    classifiers=[
        "Environment :: Console",
        "Topic :: Software Development",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"console_scripts": ["a-john-shots=a_john_shots:command_line"]},
)
