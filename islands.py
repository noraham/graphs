# ideas for solving the islands problem

"""Given a 2d grid map of '1's (land) and '0's (water), count the number of
   islands. An island is surrounded by water and is formed by connecting adjacent
   lands horizontally or vertically. You may assume all four edges of the grid
   are all surrounded by water."""

def islands(island):
    """See full description above. Given a grid, return an int that represents
       number of islands in the grid.
       no diagional checking in this implementation.

       >>> islands([[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]])
       1
       >>> islands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]])
       3"""

    # my plan:
    # make a loop to go through each cell in grid from top-L to bottom-R
    # if current cell is 'land', send it to helper function
    # helper rewrites this cell and all surrounding that are also 'land'
    # which means they won't be flagged as land when we return to main function
    # when helper returns, increment counter, continue searching grid for 'land'

    island_count = 0
    down = len(island[0])
    across = len(island)

    def explore(x, y):
        """For start cell, find all contiguous 'land' and rewrite those cells.
           Keep going until no more contiguous land.
           This implementation doesn't count diagonals as connected."""
        island[x][y] = '#'
        # recursively call explore if we are still in bounds and neighbor is land
        if x > 0 and island[x - 1][y] == 1:
            explore(x-1, y)
        if y > 0 and island[x][y - 1] == 1:
            explore(x, y-1)
        if x + 1 < across and island[x + 1][y] == 1:
            explore(x+1, y)
        if y + 1 < down and island[x][y + 1] == 1:
            explore(x, y+1)

    for x in xrange(across):
        for y in xrange(down):
            if island[x][y] == 1:
                explore(x, y)
                island_count += 1

    return island_count


# uncomment the lines below to run doctests
if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print "Tests passed!"