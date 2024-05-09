#!/usr/bin/python3

"""
Min Opetaion module
"""


def minOperations(n):
    """ Function cals the min"""

    if n <= 0:
        return 0
    ops = 0
    curlen = 1
    clip = 0

    while curlen < n:
        if n % curlen == 0:
            clip = curlen
            ops += 1
        curlen += clip
        ops += 1
    return ops
