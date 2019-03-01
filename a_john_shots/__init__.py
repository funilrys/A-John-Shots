#!/bin/env python3

"""
A John Shots - A tool to get the Security Hash Algorightms (SHA) of all file in a given path.

This is the module entry which provides the API endpoints and the CLI.

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
# pylint: disable=bad-continuation, too-many-arguments
import argparse
from json import dump, dumps

from colorama import Fore, Style
from colorama import init as initiate

from a_john_shots.core import Core
from a_john_shots.defaults import DEFAULT_OUTPUT_FILENAME

VERSION = "2.0.0"


def get(
    file_or_dir_path,
    sha="sha512",
    search=None,
    save=False,
    save_destination=None,
    exclude=None,
):
    """
    Return the SHA representation of the given path children.

    .. note::
        If :code:`file_or_dir_path` is a directory, we will get
        the SHA representation of all children files.

    .. note::
        If :code:`file_or_dir_path` is a file, we will get
        the SHA representation of the given file.

    :param file_or_dir_path: The file or directory we are working with.
    :type file_or_dir_path: str

    :param sha:
        The SHA to use. Can be one of the following:
        ::

            - all
            - sha1
            - sha224
            - sha384
            - sha513
    :type sha: str

    :param search:
        The pattern the filename have to match in order to be
        taken in consideration.
    :type search: str

    :param save:
        Tell the system if we are allowed to save the result into a JSON file.

        .. note::
            The default file name is :code:`faith-slosh.json`.

        .. note::
            Even if this argument is set to :code:`True`, we return the
            dict representation if needed.
    :type save: bool

    :param save_destination: The destination file.
    :type save_destination: str

    :param exclude:
        The pattern the filename have to match in order to be
        excluded.
    :type exclude: str|list
    """

    sha = sha.lower()
    result = Core(file_or_dir_path, search=search, exclude=exclude, algorithm=sha).get()

    if save_destination is None:
        save_destination = DEFAULT_OUTPUT_FILENAME

    if save:
        print(save_destination)
        with open(save_destination, "w") as file:
            dump(result, file, ensure_ascii=False, indent=4, sort_keys=True)

    return result


def command_line():
    """
    Provide the CLI.
    """

    if __name__ == "a_john_shots":
        initiate(True)

        parser = argparse.ArgumentParser(
            description="A John Shots - A tool to get the Security Hash "
            "Algorightms (SHA) of all file in a given path.",
            epilog=f"Crafted with %s by %s"
            % (
                f"{Fore.RED}♥{Fore.RESET}",
                f"{Style.BRIGHT}{Fore.CYAN}Nissar Chababy (Funilrys){Style.RESET_ALL}",
            ),
        )

        parser.add_argument(
            "-a",
            "--algorithm",
            type=str,
            default="sha512",
            help="The SHA algorithm to use. Can be ALL, SHA1, SHA224, SHA384 or SHA512 (default).",
        )

        parser.add_argument(
            "-d",
            "--destination",
            type=str,
            help="Set the file we are going to write the JSON output to.",
        )

        parser.add_argument(
            "-e",
            "--exclude",
            type=str,
            help="The (regex) pattern the filename has to match in order "
            "to be excluded from the output.",
        )

        parser.add_argument(
            "-p", "--path", type=str, help="The file or directory path to read."
        )

        parser.add_argument("--print", action="store_true", help="Print the output.")

        parser.add_argument(
            "-s",
            "--search",
            type=str,
            help="The (regex) pattern the filename has to match in order "
            "to be included into the output.",
        )

        parser.add_argument(
            "--save", action="store_true", help="Save the output into a JSON file."
        )

        parser.add_argument(
            "-v", "--version", action="version", version="%(prog)s " + VERSION
        )

        args = parser.parse_args()

        if args.path:
            if args.print:
                print(
                    dumps(
                        get(
                            args.path,
                            sha=args.algorithm,
                            search=args.search,
                            save=args.save,
                            save_destination=args.destination,
                            exclude=args.exclude,
                        ),
                        ensure_ascii=False,
                        indent=4,
                        sort_keys=True,
                    )
                )
            else:
                get(
                    args.path,
                    sha=args.algorithm,
                    search=args.search,
                    save=args.save,
                    save_destination=args.destination,
                    exclude=args.exclude,
                )
