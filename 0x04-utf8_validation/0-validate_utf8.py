#!/usr/bin/python3
"""
UTF-8 Validation module
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing 1 byte of data each.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """
    num_bytes_to_follow = 0

    for byte in data:
        if num_bytes_to_follow == 0:
            if (byte >> 7) == 0b0:  # 1-byte character
                num_bytes_to_follow = 0
            elif (byte >> 5) == 0b110:  # 2-byte character
                num_bytes_to_follow = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes_to_follow = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes_to_follow = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0

