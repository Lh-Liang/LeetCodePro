#
# @lc app=leetcode id=3640 lang=python3
#
# [3640] Trionic Array II
#

# @lc code=start
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0
        
        # Step 1: Precalculate max increasing sum ending at i (len >= 2)
        pref_inc = [-float('inf')] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                pref_inc[i] = nums[i] + max(nums[i-1], pref_inc[i-1])
        
        # Step 2: Precalculate max increasing sum starting at i (len >= 2)
        suff_inc = [-float('inf')] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                suff_inc[i] = nums[i] + max(nums[i+1], suff_inc[i+1])
        
        # Step 3: Prefix sums for range sum calculation
        p = [0] * (n + 1)
        for i in range(n):
            p[i+1] = p[i] + nums[i]
            
        # Step 4: Iterate through maximal strictly decreasing subarrays
        ans = -float('inf')
        idx = 0
        while idx < n - 1:
            j = idx
            while j + 1 < n and nums[j] > nums[j+1]:
                j += 1
            
            if j > idx:
                # For decreasing segment nums[idx...j], find p, q s.t. idx <= p < q <= j
                max_val_p = -float('inf')
                for k in range(idx, j + 1):
                    # Try k as 'q' (valley)
                    if k > idx and suff_inc[k] != -float('inf') and max_val_p != -float('inf'):
                        ans = max(ans, max_val_p + p[k] + suff_inc[k])
                    
                    # Try k as 'p' (peak)
                    if pref_inc[k] != -float('inf'):
                        val_p = pref_inc[k] - p[k+1]
                        if val_p > max_val_p:
                            max_val_p = val_p
                idx = j
            else:
                idx += 1
                
        return int(ans)
# @lc code=end