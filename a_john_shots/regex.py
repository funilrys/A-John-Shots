!/usr/bin/env python

#    python-regex - A simple implementation ot the python.re package
#    Copyright (C) 2017  Funilrys - Nissar Chababy <contact at funilrys dot com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#    Original Version: https://github.com/funilrys/python-regex


from re import compile, search


class Regex(object):
    """A simple implementation ot the python.re package"""

    def __init__(self, data, regex, return_data=False, group=0):
        super(Regex, self).__init__()
        self.data = data
        self.regex = regex
        self.return_data = return_data
        self.group = group

    def match(self):
        """Used to get exploitable result of re.search"""

        toMatch = compile(self.regex)
        result = toMatch.search(self.data)

        if self.return_data and result is not None:
            return result.group(self.group).strip()
        elif self.return_data == False and result is not None:
            return True
        else:
            return False
