#!/bin/env python

#    A-John-Shots - Python module/library for saving Security Hash Algorithms into JSON format.
#    Copyright (C) 2017  Funilrys - Nissar Chababy <contact at funilrys dot com>
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.

#    Original Version: https://github.com/funilrys/A-John-Shots

"""
This is the main entry to a_john_shots.
A John Shots is a Python module/library for saving Security Hash Algorithms
into JSON format.
"""

from a_john_shots.core import Core


def get(path, **args):
    """
    A simple script to get Security Hash Algorithms into JSON format

    Arguments:
        - path: str
            The path of the file or the directory we have to return
        - search: str
            The pattern the file have to match in order to be included in the
            results.
        - output: bool
            True: Print on file | False: Print on file and on screen.
        - algorithm: str
            The algorithm to use.
            Possibilities:
                - all
                - sha1
                - sha224
                - sha384
                - sha512
        - exclude: list
            The list of path, filenames or in general, a pattern to exclude.

    Returns:
        Pretty dict/JSON
    """

    return Core(path, **args).get()
