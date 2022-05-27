class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perim = 0
        w, l = len(grid), len(grid[0])
        
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                
                # if land has been found
                if grid[r][c] == 1:    
                    perim += 4
                    
                    #look above
                    if (r > 0 and grid[r-1][c] == 1):
                        perim -= 2
                    #look left
                    if (c > 0 and grid [r][c-1] == 1):
                        perim -= 2
                        
        return perim