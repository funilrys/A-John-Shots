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

from re import compile, search


class Regex(object):
    """
    A simple implementation ot the python.re package
    """

    def __init__(self, data, regex, return_data=False, group=0):
        super(Regex, self).__init__()
        self.data = data
        self.regex = regex
        self.return_data = return_data
        self.group = group

    def match(self):
        """Used to get exploitable result of re.search"""

        if isinstance(self.regex, list) and isinstance(self.data, str):
            result = []
            for item in self.regex:
                to_match = compile(item)
                local_result = to_match.search(self.data)

                if self.return_data and local_result is not None:
                    result.append(local_result.group(self.group))
                elif self.return_data == False and local_result is not None:
                    return True
            if self.return_data and result:
                return result
            return False
        elif isinstance(self.data, list) and isinstance(self.Regex, str):
            result = []
            for item in self.data:
                to_match = compile(self.regex)
                local_result = to_match.search(item)

                if self.return_data and local_result is not None:
                    result.append(local_result.group(self.group))
                elif self.return_data == False and local_result is not None:
                    return True
            if self.return_data and result:
                return result
            return False
        elif isinstance(self.data, str) and isinstance(self.regex, str):
            toMatch = compile(self.regex)
            result = toMatch.search(self.data)

            if self.return_data and result is not None:
                return result.group(self.group).strip()
            elif self.return_data == False and result is not None:
                return True
            return False
        return None
