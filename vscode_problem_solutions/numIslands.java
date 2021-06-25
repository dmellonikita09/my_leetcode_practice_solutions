int islands = 0;
    public int numIslands(char[][] grid) {
        for (int r=0; r<grid.length; r+=1) {
            for (int c=0; c<grid[r].length; c+=1) {
                if (grid[r][c] == '1') {
                    this.islands+=1;
                    tagIslands(r, c, grid);
                }
            }
        }
        return this.islands;
    }

    public void tagIslands(int row, int column, char[][] grid) {
        if (row < 0 || column < 0) {
            return;
        }
        if (row >= grid.length || column >= grid[row].length) {
            return;
        }
        if (grid[row][column] == '1') {
            grid[row][column] = 2;
            tagIslands(row+1, column, grid);
            tagIslands(row-1, column, grid);
            tagIslands(row, column+1, grid);
            tagIslands(row, column-1, grid);
        }
    }