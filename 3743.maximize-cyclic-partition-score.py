#
# @lc app=leetcode id=3743 lang=python3
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Compute the gaps between adjacent elements (cyclic)
        gaps = []
        for i in range(n):
            gap = abs(nums[i] - nums[(i+1)%n])
            gaps.append((gap, i))
        # For each possible rotation (start position), find the k-1 largest gaps
        max_score = 0
        for start in range(n):
            # Compute prefix max and min for this rotation
            arr = nums[start:] + nums[:start]
            prefix_max = [arr[0]]
            prefix_min = [arr[0]]
            for i in range(1, n):
                prefix_max.append(max(prefix_max[-1], arr[i]))
                prefix_min.append(min(prefix_min[-1], arr[i]))
            # Find k-1 largest gaps in this rotation
            gap_list = []
            for i in range(n-1):
                gap_list.append(abs(arr[i] - arr[i+1]))
            gap_list.append(abs(arr[-1] - arr[0]))  # cyclic gap
            # Sort gaps and take k-1 largest
            sorted_gaps = sorted(gap_list, reverse=True)
            total_range = max(arr) - min(arr)
            if k == 1:
                max_score = max(max_score, total_range)
                continue
            # The sum of (max-min) over k parts is: total_range + sum of k-1 largest gaps
            score = total_range
            for i in range(k-1):
                score += sorted_gaps[i]
            max_score = max(max_score, score)
        return max_score
# @lc code=end