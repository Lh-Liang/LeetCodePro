#
# @lc app=leetcode id=3470 lang=python3
#
# [3470] Permutations IV
#

# @lc code=start
from typing import List

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        odds = list(range(1, n + 1, 2))
        evens = list(range(2, n + 1, 2))
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
        
        def count_ways(ro: int, re: int, next_p: int) -> int:
            if ro < 0 or re < 0:
                return 0
            m = ro + re
            if m == 0:
                return 1
            req_nextp_slots = (m + 1) // 2
            req_other_slots = m // 2
            if next_p == 1:
                req_odd = req_nextp_slots
                req_even = req_other_slots
            else:
                req_odd = req_other_slots
                req_even = req_nextp_slots
            if req_odd != ro or req_even != re:
                return 0
            return fact[ro] * fact[re]
        
        perm = []
        curr_k = k
        last_parity = -1
        for pos in range(n):
            if pos == 0:
                found = False
                for cand in range(1, n + 1):
                    is_odd = (cand % 2 == 1)
                    ro = len(odds) - 1 if is_odd else len(odds)
                    re = len(evens) - 1 if not is_odd else len(evens)
                    next_p = 1 - int(is_odd)
                    ways = count_ways(ro, re, next_p)
                    if ways == 0:
                        continue
                    if curr_k <= ways:
                        perm.append(cand)
                        if is_odd:
                            odds.remove(cand)
                        else:
                            evens.remove(cand)
                        last_parity = 1 if is_odd else 0
                        found = True
                        break
                    else:
                        curr_k -= ways
                if not found:
                    return []
            else:
                req_p = 1 - last_parity
                candidates = odds if req_p == 1 else evens
                num_cand = len(candidates)
                if num_cand == 0:
                    return []
                ro = len(odds) - 1 if req_p == 1 else len(odds)
                re = len(evens) - 1 if req_p == 0 else len(evens)
                next_p = 1 - req_p
                S = count_ways(ro, re, next_p)
                if S == 0:
                    return []
                idx = (curr_k - 1) // S
                if idx >= num_cand:
                    return []
                cand = candidates[idx]
                perm.append(cand)
                del candidates[idx]
                last_parity = req_p
                curr_k = ((curr_k - 1) % S) + 1
        return perm

# @lc code=end