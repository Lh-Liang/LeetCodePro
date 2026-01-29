#
# @lc app=leetcode id=3762 lang=python3
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        def is_feasible(subarray):
            # Check if all differences with respect to a base element are divisible by k
            base = subarray[0]
            for num in subarray:
                if (num - base) % k != 0:
                    return False
            return True

        def min_operations(subarray):
            # Calculate minimum operations needed once feasibility is confirmed
            # Use sorted subarray for easier calculation of median or target value
            sorted_sub = sorted(subarray)
            median = sorted_sub[len(sorted_sub) // 2]
            operations = sum(abs(num - median) // k for num in sorted_sub)
            return operations
        
        ans = []
        for li, ri in queries:
            subarray = nums[li:ri+1]
            if is_feasible(subarray):
                ans.append(min_operations(subarray))
            else:
                ans.append(-1)
        return ans
# @lc code=end