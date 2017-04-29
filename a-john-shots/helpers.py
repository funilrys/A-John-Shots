#!/bin/env python


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
