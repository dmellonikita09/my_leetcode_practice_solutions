def dfs(grid, r,c ):
    grid[r][c]= '0'
    list = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    for row, col in list:
        if row>=0 and col>=0 and row < len(grid) and col< len(grid[row]) and grid[row][col] == '1':
            dfs(grid, row, col)
def numberOfIslands(grid):
    islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '1':
                dfs(grid, r, c)
                islands += 1
    return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numberOfIslands(grid))