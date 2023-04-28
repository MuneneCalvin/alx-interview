#!/usr/bin/python3
'''
0-lockboxes.py
'''


def canUnlockAll(boxes):
    '''
    method that determines if all the boxes can be opened.
    '''
    # get the number of boxes
    n = len(boxes)

    # initialize an array to mark if a box has been visited or not
    visited = [False] * n

    # mark the first box as visited
    visited[0] = True

    # initialize a list to keep track of keys found in boxes
    found_keys = [0]

    # loop through the list of found keys and mark all the boxes that can be
    # opened by each key as visited
    while found_keys:
        box_idx = found_keys.pop()
        boxes_to_open = boxes[box_idx]
        for key in boxes_to_open:
            if key < n and not visited[key]:
                visited[key] = True
                found_keys.append(key)

    # check if all boxes have been visited
    return all(visited)
