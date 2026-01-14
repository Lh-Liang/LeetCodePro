#
# @lc app=leetcode id=3670 lang=python3
#
# [3670] Maximum Product of Two Integers With No Common Bits
#
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max_prod = 0
        n = len(nums)
        
        for i in range(n - 1):
            # Early termination: if best possible product from this point <= max_prod
            if nums[i] * nums[i + 1] <= max_prod:
                break
            
            for j in range(i + 1, n):
                if nums[i] & nums[j] == 0:
                    max_prod = max(max_prod, nums[i] * nums[j])
                    break  # Found the best match for nums[i] since array is sorted
        
        return max_prod
# @lc code=end