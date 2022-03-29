A John Shots (Hash To JSON)
===========================

A tool to get the Security Hash Algorightms (SHA) of all file in a given path.
------------------------------------------------------------------------------

The objective of this project is to provide a tool which give the SHAx representation of all file in a given tree/path.

-------------


Installation
------------

From PyPi
^^^^^^^^^

::

    $ pip3 install --user a-john-shots


We recommend the :code:`--user` flag which installs the required dependencies at the user level. More information about it can be found on `pip documentation`_.

From GitHub
^^^^^^^^^^^

::

    $ pip3 install --user git+https://github.com/funilrys/A-John-Shots.git@master#egg=a-john-shots

We recommend the :code:`--user` flag which installs the required dependencies at the user level. More information about it can be found on `pip documentation`_.

-------------

Usage
-----

CLI
^^^

::

    usage: a-john-shots [-h] [-a ALGORITHM] [-d DESTINATION] [-e EXCLUDE]
                    [-p PATH] [--print] [-s SEARCH] [--save] [-v]

    A John Shots - A tool to get the Security Hash Algorightms (SHA) of all file
    in a given path.

    optional arguments:
        -h, --help            show this help message and exit
        -a ALGORITHM, --algorithm ALGORITHM
                                The SHA algorithm to use. Can be ALL, SHA1, SHA224,
                                SHA384 or SHA512 (default).
        -d DESTINATION, --destination DESTINATION
                                Set the file we are going to write the JSON output to.
        -e EXCLUDE, --exclude EXCLUDE
                                The (regex) pattern the filename has to match in order
                                to be excluded from the output.
        -p PATH, --path PATH  The file or directory path to read.
        --print               Print the output.
        -s SEARCH, --search SEARCH
                                The (regex) pattern the filename has to match in order
                                to be included into the output.
        --save                Save the output into a JSON file.
        -v, --version         show program's version number and exit

    Crafted with ♥ by Nissar Chababy (Funilrys)

API
^^^

::

    Help on function get in a_john_shots:

    a_john_shots.get = get(file_or_dir_path, sha='sha512', search=None, save=False, save_destination=None, exclude=None)
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


-------------

License
-------

::

    MIT License

    Copyright (c) 2017, 2018, 2019, 2020, 2021, 2022 Nissar Chababy

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



.. _pip documentation: https://pip.pypa.io/en/stable/reference/pip_install/?highlight=--user#cmdoption-user
