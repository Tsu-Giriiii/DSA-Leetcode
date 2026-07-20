class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total_elements = m * n
        
        # Optimize k to avoid redundant full rotations
        k = k % total_elements
        
        # If no effective shifts are needed, return the grid as is
        if k == 0:
            return grid
            
        # Create a blank grid of the same size to store the result
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # 1. Flatten the current 2D index to a 1D index
                old_1d_index = i * n + j
                
                # 2. Find the new 1D index after shifting k times
                new_1d_index = (old_1d_index + k) % total_elements
                
                # 3. Convert the new 1D index back into 2D coordinates
                new_row = new_1d_index // n
                new_col = new_1d_index % n
                
                # Place the element in its new home
                result[new_row][new_col] = grid[i][j]
                
        return result
            
        