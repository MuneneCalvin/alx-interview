#!/usr/bin/python3


def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    keys = [0]
    while keys:
        box_idx = keys.pop()
        for key in boxes[box_idx]:
            if key < n and not visited[key]:
                visited[key] = True
                keys.append(key)
    return all(visited)
