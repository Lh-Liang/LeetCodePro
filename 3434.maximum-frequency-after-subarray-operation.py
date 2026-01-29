#
# @lc app=leetcode id=3434 lang=python3
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Store positions of each number (1 to 50)
        pos = [[] for _ in range(51)]
        # Precompute prefix sums for the count of k
        pref_k = [0] * (n + 1)
        
        for i, x in enumerate(nums):
            pos[x].append(i)
            pref_k[i+1] = pref_k[i] + (1 if x == k else 0)
        
        total_k = pref_k[n]
        max_gain = 0
        
        # Iterate through each possible value v that could be transformed into k
        for v in range(1, 51):
            # Skip k itself as transforming k to k yields no gain
            if v == k or not pos[v]:
                continue
            
            curr_gain = 0
            prev_p = -1
            # For each value v, find the maximum (count(v) - count(k)) in any subarray
            # Using Kadane's algorithm on the sequence of v (+1) and k (-1)
            for p in pos[v]:
                # Number of k's between the previous occurrence of v and the current one
                num_k_between = pref_k[p] - pref_k[prev_p + 1]
                # Either extend the previous subarray sum (subtracting k's) or start fresh with current v
                curr_gain = max(0, curr_gain - num_k_between) + 1
                if curr_gain > max_gain:
                    max_gain = curr_gain
                prev_p = p
        
        return total_k + max_gain
# @lc code=end