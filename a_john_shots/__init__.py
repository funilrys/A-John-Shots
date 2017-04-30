#!/bin/env python
from .core import Core


def get(path, **args):
    return Core(path, **args).get()
