#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import defaultdict
        n = len(nums)
        indices = defaultdict(list)
        # Preprocess indices for each number in nums
        for i, num in enumerate(nums):
            indices[num].append(i)
        answers = []
        for query in queries:
            target_index = query
            target_value = nums[target_index]
            if len(indices[target_value]) == 1: # Only one occurrence of the value
                answers.append(-1)
                continue
            min_distance = float('inf')
            for idx in indices[target_value]:
                if idx == target_index:
                    continue
                # Calculate circular distance
                distance = min(abs(idx - target_index), n - abs(idx - target_index))
                min_distance = min(min_distance, distance)
            answers.append(min_distance)
        return answers
# @lc code=end