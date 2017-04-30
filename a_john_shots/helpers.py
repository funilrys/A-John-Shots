#!/bin/env python

#    A-John-Shots - Python module/library for saving Security Hash Algorithms into JSON format.
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

#    Original Version: https://github.com/funilrys/A-John-Shots


def unset_empty(list_to_format):
    """Delete all empty element(s) from a given lis

    :param list_to_format: A list, List to format
    """

    return ' '.join(list_to_format).split()


def combine_dicts(dict1, dict2):
    """Combine two dictionnaries into one

    :param dict1: A dict, First dict
    :param dict2: A dict, Second dict
    """

    result = {}

    for k, v in dict1.items():
        if k in dict2.keys():
            if isinstance(dict2[k], dict):
                result[k] = combine_dicts(v, dict2.pop(k))
        else:
            result[k] = v
    for k, v in dict2.items():
        result[k] = v
    return result
