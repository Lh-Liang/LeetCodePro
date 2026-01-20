#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # Offset to handle negative indices in BIT
        # Range of prefix sums is [-n, n].
        # We map -n to 1, 0 to n+1, n to 2n+1.
        offset = n + 1
        size = 2 * n + 2
        bit = [0] * (size + 1)

        def update(i, delta):
            while i < len(bit):
                bit[i] += delta
                i += i & (-i)

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s

        ans = 0
        current_prefix_sum = 0
        
        # Initialize with prefix sum 0 (representing empty prefix before start)
        # Map 0 to offset
        update(0 + offset, 1)

        for num in nums:
            if num == target:
                current_prefix_sum += 1
            else:
                current_prefix_sum -= 1
            
            # We want to count previous prefix sums P_prev such that
            # current_prefix_sum - P_prev > 0  => P_prev < current_prefix_sum
            # In BIT, we query for indices strictly less than (current_prefix_sum + offset)
            # which is query(current_prefix_sum + offset - 1)
            
            count = query(current_prefix_sum + offset - 1)
            ans += count
            
            # Add current prefix sum to BIT
            update(current_prefix_sum + offset, 1)
            
        return ans

# @lc code=end