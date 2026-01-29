#
# @lc app=leetcode id=3420 lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        inc_end = list(range(n))
        for i in range(n - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                inc_end[i] = inc_end[i + 1]
            else:
                inc_end[i] = i
        ans = 0
        for start in range(n):
            cost = 0
            pos = start
            brk = False
            while pos < n:
                seg_end = right[pos]
                if seg_end == pos + 1:
                    if seg_end == n:
                        pos = n
                    else:
                        pos = inc_end[pos]
                    continue
                terms = seg_end - pos - 1
                seg_cost = nums[pos] * terms - (prefix[seg_end] - prefix[pos + 1])
                if cost + seg_cost > k:
                    remain = k - cost
                    lo = pos
                    hi = seg_end - 1
                    while lo < hi:
                        mid = lo + (hi - lo + 1) // 2
                        tterms = mid - pos
                        pcost = nums[pos] * tterms - (prefix[mid + 1] - prefix[pos + 1])
                        if pcost <= remain:
                            lo = mid
                        else:
                            hi = mid - 1
                    ans += lo - start + 1
                    brk = True
                    break
                cost += seg_cost
                pos = seg_end
            if not brk:
                ans += n - start
        return ans

# @lc code=end