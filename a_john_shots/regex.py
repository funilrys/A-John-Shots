#!/usr/bin/env python

# python-regex - A simple implementation ot the python.re package
# Copyright (c) 2017 Funilrys - Nissar Chababy <contact at funilrys dot com>
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Original Version: https://github.com/funilrys/python-regex

"""
A simple implementation ot the python.re package.
"""

from re import compile as comp
from re import sub as substrings
from re import escape


class Regex(object):  # pylint: disable=too-few-public-methods

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
        - replace_with: str
            The value to replace the matched regex with.
        - occurences: int
            The number of occurence to replace.
    """

    def __init__(self, data, regex, **args):
        super(Regex, self).__init__()

        # We initiate the needed variable in order to be usable all over class
        self.data = data
        self.regex = regex

        # We assign the default value of our optional arguments
        optional_arguments = {
            "escape": False,
            "group": 0,
            "occurences": 0,
            "rematch": False,
            "replace_with": None,
            "return_data": True
        }

        # We initiate our optional_arguments in order to be usable all over the
        # class
        for (arg, default) in optional_arguments.items():
            setattr(self, arg, args.get(arg, default))

        # We initiate regex according to self.escape status.
        if self.escape:  # pylint: disable=no-member
            self.regex = escape(regex)
        else:
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
        if self.rematch:  # pylint: disable=no-member
            pre_result = to_match.findall(data_to_match)
        else:
            pre_result = to_match.search(data_to_match)

        if self.return_data and pre_result is not None:  # pylint: disable=no-member
            if self.rematch:  # pylint: disable=no-member
                for data in pre_result:
                    if isinstance(data, tuple):
                        result.extend(list(data))
                    else:
                        result.append(data)

                if self.group != 0:  # pylint: disable=no-member
                    return result[self.group]  # pylint: disable=no-member
            else:
                result = pre_result.group(
                    self.group).strip()  # pylint: disable=no-member

            return result
        elif not self.return_data and pre_result is not None:  # pylint: disable=no-member
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

    def replace(self):
        """
        Used to replace a matched string with another.
        """

        if self.replace_with is not None:  # pylint: disable=no-member
            return substrings(
                self.regex,
                self.replace_with,  # pylint: disable=no-member
                self.data,
                self.occurences)  # pylint: disable=no-member
        return self.data
