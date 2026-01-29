#
# @lc app=leetcode id=3470 lang=python3
#
# [3470] Permutations IV
#

# @lc code=start
from typing import List

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        # Precompute factorials, capped at k + 1 to prevent dealing with 100!
        LIMIT = k + 1
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = min(LIMIT, fact[i - 1] * i)

        def count_ways(rem_o, rem_e, next_is_odd):
            """
            Calculates how many ways to complete an alternating sequence.
            Since the parity must alternate, the parity of every remaining position 
            is fixed. Thus, we just need to check if the counts of remaining 
            odd/even numbers match the required parity slots.
            """
            total_rem = rem_o + rem_e
            if total_rem == 0:
                return 1
            
            # If we must start with Odd:
            # If total_rem is 2m, we need m odd and m even.
            # If total_rem is 2m+1, we need m+1 odd and m even.
            if next_is_odd:
                if not (rem_o == (total_rem + 1) // 2 and rem_e == total_rem // 2):
                    return 0
            else:
                # If we must start with Even:
                if not (rem_e == (total_rem + 1) // 2 and rem_o == total_rem // 2):
                    return 0
            
            # If the parity counts are valid, the number of ways is simply 
            # the number of ways to arrange the remaining odd numbers multiplied 
            # by the number of ways to arrange the remaining even numbers.
            res = fact[rem_o]
            if res >= LIMIT: 
                res = LIMIT
            res *= fact[rem_e]
            return min(LIMIT, res)

        res = []
        used = [False] * (n + 1)
        rem_o = (n + 1) // 2
        rem_e = n // 2

        for i in range(n):
            found = False
            for v in range(1, n + 1):
                if used[v]:
                    continue
                
                is_odd = (v % 2 != 0)
                # Check alternating constraint against the previous element
                if i > 0 and is_odd == (res[-1] % 2 != 0):
                    continue

                # Calculate remaining counts and the required parity for the next position
                n_rem_o = rem_o - (1 if is_odd else 0)
                n_rem_e = rem_e - (1 if not is_odd else 0)
                next_is_odd = not is_odd
                
                ways = count_ways(n_rem_o, n_rem_e, next_is_odd)
                
                if k <= ways:
                    res.append(v)
                    used[v] = True
                    rem_o, rem_e = n_rem_o, n_rem_e
                    found = True
                    break
                else:
                    k -= ways
            
            if not found:
                return []

        return res
# @lc code=end