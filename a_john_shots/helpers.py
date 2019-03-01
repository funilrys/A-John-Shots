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
# pylint: disable=bad-continuation, too-many-arguments

from re import compile as comp


def combine_dicts(dict_1, dict_2):
    """
    Combine two dictionnaries.

    :param dict_1: The first dict.
    :type dict_1: dict

    :param dict_2: The second dict.
    :type dict_2: dict

    :return: The combined dict.
    :rtype: dict
    """

    result = {}

    for key, value in dict_1.items():
        if key in dict_2.keys():
            if isinstance(dict_2[key], dict):
                result[key] = combine_dicts(value, dict_2.pop(key))
        else:
            result[key] = value
    for key, value in dict_2.items():
        result[key] = value
    return result


class Regex:  # pylint: disable=too-few-public-methods

    """
    A simple implementation ot the python.re package

    Arguments:
        - data: str or list
            The data or a list of data to check.
        - regex: str or list
            The regex or a list or regex.
        - return_data: bool
            - True: Return matched string
            - False: Return False|True
        - group: int
            The group to return.
        - rematch: bool
            Implementation of Bash ${BASH_REMATCH}.
            - True: Returned matched groups into a list format.
        - occurences: int
            The number of occurence to replace.
    """

    def __init__(
        self, data, regex, group=0, occurences=0, rematch=False, return_data=True
    ):
        super(Regex, self).__init__()

        # We initiate the needed variable in order to be usable all over class
        self.data = data
        self.regex = regex

        self.group = group
        self.occurences = occurences
        self.rematch = rematch
        self.return_data = return_data

        # We initiate regex according to self.escape status.
        self.regex = regex

    def match(self, regex=None, data_to_match=None):
        """
        Used to get exploitable result of re.search

        Arguments:
            - data: str
                The data or a list of data to check.
            - regex: str
                The regex or a list or regex.

        Returns:
            list or bool
            - bool: if self.return_data is False
            - list: otherwise
        """

        # We initate this variable which gonna contain the returned data
        result = []

        if not regex:
            regex = self.regex

        if not data_to_match:
            data_to_match = self.data

        # We compile the regex string
        to_match = comp(regex)

        # In case we have to use the implementation of ${BASH_REMATCH} we use
        # re.findall otherwise, we use re.search
        if self.rematch:
            pre_result = to_match.findall(data_to_match)
        else:
            pre_result = to_match.search(data_to_match)

        if self.return_data and pre_result is not None:
            if self.rematch:
                for data in pre_result:
                    if isinstance(data, tuple):
                        result.extend(list(data))
                    else:
                        result.append(data)

                if self.group != 0:
                    return result[self.group]
            else:
                result = pre_result.group(self.group).strip()

            return result

        if not self.return_data and pre_result is not None:
            return True
        return False

    def loop_matching(self):
        """
        This method can be used to perform a loop matching.
        """

        results = []

        if isinstance(self.data, str):
            if isinstance(self.regex, list):
                for exp in self.regex:
                    matched = self.match(regex=exp)

                    try:
                        results.extend(matched)
                    except TypeError:
                        results.append(matched)

                if not self.return_data:
                    if True in results:
                        return True
                    return False
            else:
                return self.match()

        elif isinstance(self.data, list) and isinstance(self.regex, str):
            for string in self.data:
                results.extend(self.match(data_to_match=string))

        return results
