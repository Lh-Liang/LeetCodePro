#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # The condition (count > length / 2) is equivalent to (2 * count - length > 0).
        # Assign +1 to target and -1 to others. We need to count subarrays with sum > 0.
        # This is equivalent to counting pairs (i, j) such that prefix_sum[j] > prefix_sum[i].
        
        ans = 0
        prefix_sum = 0
        # Number of prefix sums seen so far that are strictly less than current prefix_sum
        smaller_count = 0
        # Frequency of each prefix sum value
        freq = {0: 1}
        
        for num in nums:
            if num == target:
                # prefix_sum increases: S -> S+1
                # New smaller elements = old smaller elements + those equal to S
                smaller_count += freq.get(prefix_sum, 0)
                prefix_sum += 1
            else:
                # prefix_sum decreases: S -> S-1
                # New smaller elements = old smaller elements - those equal to S-1
                prefix_sum -= 1
                smaller_count -= freq.get(prefix_sum, 0)
            
            ans += smaller_count
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
            
        return ans
# @lc code=end