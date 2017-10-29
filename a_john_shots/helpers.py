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


def unset_empty(list_to_format):
    """
    Delete all empty element(s) from a given list.

    :param list_to_format: A list, List to format.
    """

    return ' '.join(list_to_format).split()


def combine_dicts(dict1, dict2):
    """
    Combine two dictionnaries.

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
