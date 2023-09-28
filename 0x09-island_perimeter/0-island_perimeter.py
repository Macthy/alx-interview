def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): A 2D grid where 1 represents land, and 0 represents water.
            The grid is completely surrounded by water, and there is only one island.

    Returns:
        int: The perimeter of the island.

    Note:
        - The grid is rectangular, with its width and height not exceeding 100.
        - Cells are connected horizontally/vertically (not diagonally).
        - The island doesn’t have “lakes” (water inside that isn’t connected to the water
          surrounding the island).
    """
    perimeter = 0  # Initialize the perimeter to 0

    # Define the directions for horizontal and vertical neighbors
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Iterate through the grid to calculate the perimeter
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r < 0
                        or r >= len(grid)
                        or c < 0
                        or c >= len(grid[0])
                        or grid[r][c] == 0
                    ):
                        perimeter += 1

    return perimeter

