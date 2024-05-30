#!/usr/bin/env python3

"""
Validate module
"""


def validUTF8(data):
    """ Function validates if the dataset is utf-8 encoded"""
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & num:
                num_bytes += 1
                mask >>= 1
            # 1 byte character
            if num_bytes == 0:
                continue
            # Characters with more than 4 bytes are invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the next bytes are 10xxxxxx
            if not (num & mask1 and not (num & mask2)):
                return False
        num_bytes -= 1

    return num_bytes == 0
