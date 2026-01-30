#
# @lc app=leetcode id=3762 lang=python3
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        ans = []
        for li, ri in queries:
            subarray = nums[li:ri+1]
            remainders = [num % k for num in subarray]
            if len(set(remainders)) != 1:
                ans.append(-1)
                continue
            # Sort subarray to find median more easily
            subarray.sort()
            median = subarray[len(subarray) // 2]
            operations = sum(abs(num - median) // k for num in subarray)
            ans.append(operations)
        return ans
# @lc code=end