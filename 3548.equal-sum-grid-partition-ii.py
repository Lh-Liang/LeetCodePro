#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)
        
        # Function to calculate prefix sums
        def calculate_prefix_sums(matrix):
            prefix_sums = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
            for i in range(1, len(matrix) + 1):
                for j in range(1, len(matrix[0]) + 1):
                    prefix_sums[i][j] = matrix[i-1][j-1] + prefix_sums[i-1][j] + prefix_sums[i][j-1] - prefix_sums[i-1][j-1]
            return prefix_sums
        
        # Calculate prefix sums for rows and columns correctly without relying directly on transposition.
        row_prefix_sums = calculate_prefix_sums(grid)
        col_prefix_sums = [[0] * (m+1) for _ in range(n+1)]
        for j in range(1, n+1):
            for i in range(1, m+1):
                col_prefix_sums[j][i] = grid[i-1][j-1] + col_prefix_sums[j][i-1]
                
        # Check horizontal cuts
        for row in range(1, m):
            top_sum = row_prefix_sums[row][-1]
            bottom_sum = total_sum - top_sum
            if self.check_partition_possible(top_sum, bottom_sum, grid[:row], grid[row:]):
                return True
            
        # Check vertical cuts
        for col in range(1, n):
            left_sum = col_prefix_sums[col][-2]
            right_sum = total_sum - left_sum
            left_grid = [row[:col] for row in grid]
            right_grid = [row[col:] for row in grid]
            if self.check_partition_possible(left_sum, right_sum, left_grid, right_grid):
                return True
        
        return False
    
    def check_partition_possible(self, sum_a, sum_b, section_a, section_b):
        # Check if sums are equal or can be made equal by removing one cell while maintaining connectivity.
        if sum_a == sum_b:
            return True
        elif abs(sum_a - sum_b) <= max(max(max(section_a)), max(max(section_b))): # Simplified check condition.
            # Implement detailed logic to ensure a single removal maintains connectivity using DFS/BFS.
            return self.is_connected_after_removal(section_a) or self.is_connected_after_removal(section_b)
        return False
    
    def is_connected_after_removal(self, section):
        # Implement BFS/DFS to ensure all parts remain reachable after a single removal.
        # Placeholder function; needs detailed implementation based on problem constraints.
        pass  # Replace with actual logic ensuring connectivity post-removal.
# @lc code=end