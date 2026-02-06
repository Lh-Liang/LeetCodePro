#
# @lc app=leetcode id=3762 lang=python3
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        def can_make_equal(subarray):
            # Check if all elements can be made equal mod k
            first_mod = subarray[0] % k
            for num in subarray:
                if num % k != first_mod:
                    return False
            return True
        
        def min_operations(subarray):
            # Calculate minimum operations assuming can_make_equal is True
            target = min(subarray)  # Use any element as target post adjustment by k multiples
            total_ops = 0
            for num in subarray:
                total_ops += abs(num - target) // k  # Each operation is equivalent to one move by k
            return total_ops
        
        ans = []
        for li, ri in queries:
            subarray = nums[li:ri+1]
            if not can_make_equal(subarray):
                ans.append(-1)  # If impossible to make equal mod k return -1
            else:
                ans.append(min_operations(subarray))  # Calculate required operations if feasible
        return ans
# @lc code=end