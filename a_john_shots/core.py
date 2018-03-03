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
This is the brain of the module/library.
"""

from json import dump, dumps
from os import path, sep, walk

from a_john_shots.hash import Hash
from a_john_shots.helpers import combine_dicts, unset_empty
from a_john_shots.regex import Regex


class Core(object):
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

    def __init__(self, path, **args):
        self.directory_separator = sep
        self.default_output_file = '.' + self.directory_separator + 'faith-slosh.json'
        self.default_exclude = [r'\.git', r'vendor', r'nbproject']

        self.path = path

        optional_arguments = {
            "search": None,
            "output": False,
            "output_destination": None,
            "algorithm": "sha512",
            "exclude": []
        }

        for (arg, default) in optional_arguments.items():
            if arg == "search":
                setattr(self, arg, args.get(arg, self.data_to_search(default)))
            elif arg == "output_destination":
                setattr(self, arg, args.get(arg, self.destination(default)))
            else:
                setattr(self, arg, args.get(arg, default))

        self.ppath = [self.path]
        self.exclude.extend(self.default_exclude)

    def data_to_search(self, data):
        """
        A simple method to filter self.search if it's not a string

        :param data: A string, the data to search
        """

        if isinstance(data, str):
            return data
        return False

    def destination(self, output_destination):
        """
        A simple method to filter self.destination if it's not a string

        :param output_destination: A string, the output destination
        """

        if isinstance(output_destination, str):
            return output_destination
        return self.default_output_file

    def get(self):
        """
        Brain of the program.
        In charge to print the results into JSON format
        """

        result = {}
        file_hash = {}

        if path.isfile(self.path):
            file_hash = Hash(self.path, self.algorithm, False).get()
            result = self.hierarchy(file_hash)
        elif path.isdir(self.path):
            for root, dirs, files in walk(self.path):
                for file in files:
                    sub = self.get_file_under_directory(root, file)
                    if not self.search:
                        result = combine_dicts(sub, result)
                    elif Regex(file, self.search).match():
                        result = combine_dicts(sub, result)
        else:
            return None

        if self.output or self.output_destination != self.default_output_file:
            with open(self.output_destination, 'w') as file:
                dump(
                    result,
                    file,
                    ensure_ascii=False,
                    indent=4,
                    sort_keys=True)

        if not self.output:
            print(dumps(result, ensure_ascii=False, indent=4, sort_keys=True))
        return

    def hierarchy(self, hash_of_file):
        """Build the dictionary of data

        :param hash_of_file: A dict, Hash of the current file.
        """

        result = {}

        for item in self.ppath:
            hierarchy = unset_empty(item.split(self.directory_separator))
            local_result = result

            for funilrys in hierarchy:
                if funilrys == hierarchy[-1]:
                    local_result = local_result.setdefault(
                        funilrys, hash_of_file)
                else:
                    local_result = local_result.setdefault(funilrys, {})

        return result

    def get_file_under_directory(self, root, file):
        """Get the file(s) which is/are under the current directory

        :param root: A string, the current root
        :param file: A string, the current file
        """

        result = {}
        path_to_file = path.join(root, file)
        if Regex(path_to_file, self.exclude).match() == False:
            self.ppath = unset_empty(path_to_file.split(self.path))
            file_hash = Hash(path_to_file, self.algorithm).get()
            result = self.hierarchy(file_hash)

        return result
