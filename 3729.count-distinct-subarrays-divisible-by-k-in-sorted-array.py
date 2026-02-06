#
# @lc app=leetcode id=3729 lang=python3
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        prefix_sum = 0
        mod_count = defaultdict(int)
        mod_count[0] = 1 # To account for any subarray starting from index 0 being divisible by k
        total_good_subarrays = 0
        for num in nums:
            prefix_sum += num
            mod_key = prefix_sum % k
            total_good_subarrays += mod_count[mod_key]
            mod_count[mod_key] += 1
        return total_good_subarrays # Counts distinct subarrays with sum divisible by k
# @lc code=end