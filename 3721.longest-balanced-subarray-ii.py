#
# @lc app=leetcode id=3721 lang=python3
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        def check(L: int) -> bool:
            even_cnt = {}
            odd_cnt = {}
            dist_e = dist_o = 0
            # first window [0, L)
            for i in range(L):
                num = nums[i]
                cnt = even_cnt if num & 1 == 0 else odd_cnt
                cnt[num] = cnt.get(num, 0) + 1
                if cnt[num] == 1:
                    if num & 1 == 0:
                        dist_e += 1
                    else:
                        dist_o += 1
            if dist_e == dist_o:
                return True
            for start in range(1, n - L + 1):
                num_out = nums[start - 1]
                cnt_out = even_cnt if num_out & 1 == 0 else odd_cnt
                cnt_out[num_out] -= 1
                if cnt_out[num_out] == 0:
                    if num_out & 1 == 0:
                        dist_e -= 1
                    else:
                        dist_o -= 1
                num_in = nums[start + L - 1]
                cnt_in = even_cnt if num_in & 1 == 0 else odd_cnt
                cnt_in[num_in] = cnt_in.get(num_in, 0) + 1
                if cnt_in[num_in] == 1:
                    if num_in & 1 == 0:
                        dist_e += 1
                    else:
                        dist_o += 1
                if dist_e == dist_o:
                    return True
            return False
        lo = 0
        hi = n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

# @lc code=end