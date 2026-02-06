#
# @lc app=leetcode id=3538 lang=python3
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        # Initialize a 2D dp array with inf values
        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        
        # Base case: no merge, direct calculation of travel time
        for i in range(n - 1):
            dp[i][0] = (position[i + 1] - position[i]) * time[i]
        
        # Fill dp table considering merges
        for j in range(1, k + 1):
            for i in range(n - j - 1):
                # Calculate minimum cost by merging segments i and i+1 through j merges
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + (position[i + j + 1] - position[i]) * (time[i] + sum(time[i+1:i+j+1])))
                
                # Try merging different sections and update dp table accordingly
                for m in range(i + 1, n - j):
                    cost_merge = sum((position[m+1+x] - position[m+x]) * time[m+x] for x in range(j))
                    dp[i][j] = min(dp[i][j], dp[m][0] + cost_merge)
        
        # Return minimum possible travel time after exactly k merges from start to end of road
        return min(dp[0][j] for j in range(k + 1)) if n > k else sum((position[x+1]-position[x])*time[x] for x in range(n-1))
# @lc code=end