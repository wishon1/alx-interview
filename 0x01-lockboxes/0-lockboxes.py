#!/usr/bin/python3
"""
This module provides a function to determine if all boxes in a given list
can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes in the list can be opened.

    Parameters:
        boxes (List[List[int]]): A list of lists representing the boxes and
        their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Edge case: Empty list of boxes
    if not boxes:
        return False

    num_boxes = len(boxes)
    # Initialize a boolean array to keep track of visited boxes
    visited = [False] * num_boxes

    # Mark the first box (box 0) as visited initially
    visited[0] = True

    # Initialize a stack for DFS traversal
    stack = [0]

    # Perform DFS traversal
    while stack:
        box_idx = stack.pop()
        # Iterate over keys in the current box
        for key in boxes[box_idx]:
            # Check if the key opens a valid box and if the box has not
            # been visited
            if 0 <= key < num_boxes and not visited[key]:
                # Mark the box as visited and add it to the stack for further
                # traversal
                visited[key] = True
                stack.append(key)

    # Check if all boxes have been visited
    return all(visited)
