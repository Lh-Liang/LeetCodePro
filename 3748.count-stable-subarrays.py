#
# @lc app=leetcode id=3748 lang=python3
#
# [3748] Count Stable Subarrays
#

# @lc code=start
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        nb = [n] * n
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                nb[i] = i
            else:
                nb[i] = nb[i + 1]
        maxj = [0] * n
        for i in range(n):
            maxj[i] = nb[i] if nb[i] < n else n - 1
        leni = [maxj[i] - i + 1 for i in range(n)]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + leni[i]
        prevb = [-1] * n
        lastb = -1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                lastb = i
            prevb[i + 1] = lastb
        ans = []
        for l, r in queries:
            run_start = prevb[r] + 1
            split_ = max(l, run_start)
            sum_left = prefix[split_] - prefix[l] if split_ > l else 0
            nr = r - split_ + 1
            sum_right = nr * (nr + 1) // 2
            ans.append(sum_left + sum_right)
        return ans

# @lc code=end