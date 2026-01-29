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
                cnt1 = 0 # flips for 0101...
                cnt2 = 0 # flips for 1010...
                for i in range(n):
                    # Check against '010101...'
                    if i % 2 == 0:
                        if s[i] != '0': cnt1 += 1
                        if s[i] != '1': cnt2 += 1
                    else:
                        if s[i] != '1': cnt1 += 1
                        if s[i] != '0': cnt2 += 1
                return min(cnt1, cnt2) <= numOps
            
            # For k > 1, use the greedy formula: floor(L / (k+1)) flips per run of length L
            total_ops = 0
            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                length = j - i
                total_ops += length // (k + 1)
                i = j
            return total_ops <= numOps

        # Binary search for the minimum length k
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