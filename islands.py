# ideas for solving the islands problem

"""Given a 2d grid map of '1's (land) and '0's (water), count the number of
   islands. An island is surrounded by water and is formed by connecting adjacent
   lands horizontally or vertically. You may assume all four edges of the grid
   are all surrounded by water."""

def islands(island):
    """See full description above. Given a grid, return an int that represents
       number of islands in the grid.
       no diagional checking in this implementation.

       >>>islands([[11110], [11010], [11000], [00000]])
       1
       >>>islands([[11000], [11000], [00100], [00011]])
       3"""

    # make a loop to go through each cell in grid from top-L to bottom-R
    # if current cell is 'land', send it to helper function
    # helper rewrites this cell and all surrounding that are also 'land'
    # which means they won't be flagged as land when we return to main function
    # when helper returns, increment counter, continue searching grid for 'land'

    