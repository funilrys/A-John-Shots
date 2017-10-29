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


from .core import Core


def get(path, **args):
    """
    A simple script to get Security Hash Algorithms into JSON format

    :param path: A string, the path of the file or the directory we have to return.
    :param search: A string, the pattern the file have to match in ordrer to be included in the results
    :param output: A bool, Print on screen (False), print on file (True)
    :param output_destination: A string, the destination of the results
    :param algorithm: A string, the algorithm to use. Possibility: all, sha1, sha224, sha384, sha512
    :param exclude: A list, the list of path, filename or in general, a pattern to exclude
    """

    return Core(path, **args).get()
