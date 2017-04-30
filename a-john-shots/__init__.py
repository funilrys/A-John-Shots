#!/bin/env python
from core import Core


def get(path, **args):
    Core(path, **args).get()
