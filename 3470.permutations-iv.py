#
# @lc app=leetcode id=3470 lang=python3
#
# [3470] Permutations IV
#

# @lc code=start
import math

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        # Precompute capped factorials to avoid overflow
        MAX_K = 10**15 + 7
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = min(MAX_K, fact[i-1] * i)
            
        def get_ways(rem_o, rem_e, next_is_odd):
            if rem_o < 0 or rem_e < 0: return 0
            if next_is_odd:
                if rem_o != rem_e and rem_o != rem_e + 1: return 0
            else:
                if rem_e != rem_o and rem_e != rem_o + 1: return 0
            return min(MAX_K, fact[rem_o] * fact[rem_e])

        res = []
        used = [False] * (n + 1)
        rem_o = (n + 1) // 2
        rem_e = n // 2
        
        for i in range(n):
            found = False
            for val in range(1, n + 1):
                if not used[val]:
                    is_odd = (val % 2 != 0)
                    # Check parity constraint
                    if i > 0 and is_odd == (res[-1] % 2 != 0):
                        continue
                    
                    # Calculate ways if we pick 'val'
                    ways = get_ways(rem_o - (1 if is_odd else 0), 
                                    rem_e - (0 if is_odd else 1), 
                                    not is_odd if i < n - 1 else True)
                    
                    if k <= ways:
                        res.append(val)
                        used[val] = True
                        if is_odd: rem_o -= 1
                        else: rem_e -= 1
                        found = True
                        break
                    else:
                        k -= ways
            if not found:
                return []
        
        return res
# @lc code=end