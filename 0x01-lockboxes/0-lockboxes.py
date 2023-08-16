def canUnlockAll(boxes):
    """
    Check if all the boxes can be unlocked, given the list of boxes and their keys.

    Args:
        boxes (list of lists): A list of lists where each inner list represents a box
                               and contains keys to other boxes.

    Returns:
        bool: True if all the boxes can be unlocked, False otherwise.
    """
    def dfs(box_idx):
        """
        Perform a depth-first search (DFS) to explore the boxes and unlock them.

        Args:
            box_idx (int): The index of the current box being visited.

        """
        visited.add(box_idx)  # Mark the current box as visited
        for key in boxes[box_idx]:  # Iterate through the keys in the current box
            if key not in visited:  # Check if the key points to an unvisited box
                dfs(key)  # Recursively visit the box pointed by the key

    n = len(boxes)
    visited = set()  # Create an empty set to keep track of visited boxes
    dfs(0)  # Start DFS from the first box (box with index 0)

    return len(visited) == n  # Check if all boxes have been visited

