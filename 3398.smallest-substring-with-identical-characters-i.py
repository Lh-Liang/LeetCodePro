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
                # For k=1, the string must be strictly alternating.
                # Compare s with "0101..." and "1010..."
                pattern1_flips = 0 # Target: 010101...
                pattern2_flips = 0 # Target: 101010...
                for i in range(n):
                    expected1 = str(i % 2)
                    expected2 = str((i + 1) % 2)
                    if s[i] != expected1:
                        pattern1_flips += 1
                    if s[i] != expected2:
                        pattern2_flips += 1
                return min(pattern1_flips, pattern2_flips) <= numOps
            
            # For k >= 2, we can greedily break blocks of identical characters.
            total_flips = 0
            current_block_len = 1
            for i in range(1, n):
                if s[i] == s[i-1]:
                    current_block_len += 1
                else:
                    total_flips += current_block_len // (k + 1)
                    current_block_len = 1
            total_flips += current_block_len // (k + 1)
            return total_flips <= numOps

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