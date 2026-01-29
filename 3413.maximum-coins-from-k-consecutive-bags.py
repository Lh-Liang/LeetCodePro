#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        
        def solve(arr, k):
            n = len(arr)
            ans = 0
            current_sum = 0
            j = 0
            for i in range(n):
                # Window starts at the beginning of segment i
                R = arr[i][0] + k - 1
                
                # Extend j to include all segments fully contained within [arr[i][0], R]
                while j < n and arr[j][1] <= R:
                    current_sum += (arr[j][1] - arr[j][0] + 1) * arr[j][2]
                    j += 1
                
                # Total coins = full segments + partial overlap with the next segment (j)
                res = current_sum
                if j < n:
                    overlap = max(0, R - arr[j][0] + 1)
                    res += overlap * arr[j][2]
                
                ans = max(ans, res)
                
                # Before moving to next i, remove segment i from the current_sum
                # Ensure j doesn't fall behind i
                if j > i:
                    current_sum -= (arr[i][1] - arr[i][0] + 1) * arr[i][2]
                else:
                    j = i + 1
                    current_sum = 0
            return ans

        # Case 1: Window starts at some li
        ans1 = solve(coins, k)
        
        # Case 2: Window ends at some ri
        # Transform [l, r, c] to [-r, -l, c] to reuse the 'start at' logic
        reversed_coins = []
        for l, r, c in coins:
            reversed_coins.append([-r, -l, c])
        reversed_coins.sort()
        
        ans2 = solve(reversed_coins, k)
        
        return max(ans1, ans2)
# @lc code=end