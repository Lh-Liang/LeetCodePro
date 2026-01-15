#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = n + 1  # Shift values from [-n, n] to [1, 2n+1]
        size = 2 * n + 3
        bit = [0] * size
        
        def update(i):
            while i < size:
                bit[i] += 1
                i += i & (-i)
        
        def query(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & (-i)
            return total
        
        result = 0
        prefix_sum = 0
        update(offset)  # Add initial prefix_sum = 0
        
        for num in nums:
            prefix_sum += 1 if num == target else -1
            val = prefix_sum + offset
            # Count how many previous prefix sums are < current
            result += query(val - 1)
            update(val)
        
        return result
# @lc code=end