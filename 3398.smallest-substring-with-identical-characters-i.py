#
# @lc app=leetcode id=3398 lang=python3
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        
        def check(k):
            if k == 1:
                # For k=1, the string must be alternating: 0101... or 1010...
                count1 = 0 # mismatches with 0101...
                for i in range(n):
                    expected = '0' if i % 2 == 0 else '1'
                    if s[i] != expected:
                        count1 += 1
                count2 = n - count1 # mismatches with 1010...
                return min(count1, count2) <= numOps
            
            # For k > 1, we can treat each run of identical characters independently.
            # A run of length L requires floor(L / (k + 1)) flips to break into
            # pieces of length at most k.
            total_ops = 0
            curr_run_len = 0
            prev_char = ''
            for char in s:
                if char == prev_char:
                    curr_run_len += 1
                else:
                    total_ops += curr_run_len // (k + 1)
                    curr_run_len = 1
                    prev_char = char
            total_ops += curr_run_len // (k + 1)
            return total_ops <= numOps

        low = 1
        high = n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
# @lc code=end