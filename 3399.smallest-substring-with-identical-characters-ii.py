#
# @lc app=leetcode id=3399 lang=python3
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        
        # Pre-calculate block lengths for efficiency in the binary search
        lengths = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            lengths.append(j - i)
            i = j
            
        def check1():
            # For k=1, the string must be strictly alternating: 0101... or 1010...
            f1 = 0
            for i in range(n):
                # Target pattern: 0101...
                target = '0' if i % 2 == 0 else '1'
                if s[i] != target:
                    f1 += 1
            # min(f1, n - f1) gives the minimum flips to match either 0101... or 1010...
            return min(f1, n - f1) <= numOps
            
        def checkK(k):
            # For k >= 2, we can greedily flip every (k+1)-th character in each block
            total_flips = 0
            for length in lengths:
                total_flips += length // (k + 1)
                if total_flips > numOps:
                    return False
            return True
            
        low = 1
        high = n
        ans = n
        
        # Binary search for the minimum possible maximum length k
        while low <= high:
            mid = (low + high) // 2
            if mid == 1:
                possible = check1()
            else:
                possible = checkK(mid)
                
            if possible:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
# @lc code=end