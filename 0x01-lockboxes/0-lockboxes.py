#!/usr/bin/env python3

"""
Lockboxes Problem:
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes. Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.
    
    Parameters:
        boxes (list): A list of lists representing boxes and their keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    from copy import deepcopy

    if type(boxes) is not list or len(boxes) < 1:
        return False

    for box in boxes:
        if type(box) is not list:
            return False

    copyBoxes = deepcopy(boxes)
    keys_list = [0]

    while len(keys_list) > 0:
        key = keys_list[0]
        keys_list = keys_list[1:]

        if type(key) is not int or key < 0:
            return False

        copyBoxes[key].append(-1)

        for new_key in copyBoxes[key]:
            if new_key is -1:
                continue
            if new_key >= len(copyBoxes):
                continue
            if -1 in copyBoxes[new_key] or new_key in keys_list:
                continue
            keys_list.append(new_key)

    for box in copyBoxes:
        if -1 not in box:
            return False

    return True
