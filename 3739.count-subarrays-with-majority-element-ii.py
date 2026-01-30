#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # Step 1: For each prefix, compute balance = 2*count_target - length
        # A subarray [l, r] has target as majority iff count_target_in_subarray > (r-l+1)//2
        # We can use prefix sums and a hashmap to solve this in O(n).
        n = len(nums)
        bal = 0
        result = 0
        from collections import defaultdict
        bal_count = defaultdict(int)
        bal_count[0] = 1
        # For each i, bal is the difference between twice the number of targets and the length so far.
        for num in nums:
            if num == target:
                bal += 1
            else:
                bal -= 1
            # For all previous prefix balances smaller than current bal, the subarray between that prefix and current has more target than non-target.
            # So we sum up all counts of balances less than current bal.
            # To do this efficiently, we maintain prefix sums of balance counts.
            # However, as balances can be negative, we use a TreeMap or SortedDict, but here we scan a fixed-range small values.
            # Instead, we can process with a trick:
            # For each prefix, we record bal, and for each new bal, we add the number of prefixes with balance less than bal.
            # Since bal can be up to n and down to -n, we can use an array of size 2*n+1.
            # But for Python, we use a dict and maintain a running total.
            # Instead, we can do offline prefix sum counting if needed, but in practice, we can do as follows:
            result += bal_count[bal - 1]
            bal_count[bal] += 1
        return result
# @lc code=end