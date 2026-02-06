#
# @lc app=leetcode id=3743 lang=python3
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[-1] * (k + 1) for _ in range(n)]  # DP table for memoization
        
        def max_score(start: int, remaining_k: int) -> int:
            if remaining_k == 0:
                return 0
            if dp[start][remaining_k] != -1:
                return dp[start][remaining_k]
            
            current_max, current_min = float('-inf'), float('inf')
            result = 0
            
            # Consider all end points for this partition starting from `start`
            for length in range(1, n + 1):
                idx = (start + length - 1) % n  # Wrap-around using modulo operation
                current_max = max(current_max, nums[idx])
                current_min = min(current_min, nums[idx])
                current_range = current_max - current_min
                score_with_partition = current_range + max_score((start + length) % n, remaining_k - 1)
                result = max(result, score_with_partition)
                if length == n:
                    break  # Avoid wrapping around more than once
            dp[start][remaining_k] = result
            return result
        
        return max(max_score(i, k) for i in range(n))
# @lc code=end