#
# @lc app=leetcode id=3470 lang=python3
#
# [3470] Permutations IV
#

# @lc code=start
from typing import List
from bisect import bisect_left

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        # Precompute factorials up to n (Python big ints are fine for n<=100)
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i

        odds = list(range(1, n + 1, 2))
        evens = list(range(2, n + 1, 2))
        ro, re = len(odds), len(evens)

        # Total count check
        if ro == re:
            total = 2 * fact[ro] * fact[re]
        elif ro == re + 1:
            total = fact[ro] * fact[re]
        else:
            total = 0

        if k > total:
            return []

        def completions_after_pick(is_odd_pick: bool, ro0: int, re0: int, m: int) -> int:
            """Number of ways to fill m remaining positions after picking current number.
            ro0/re0 are remaining counts AFTER the pick. Next parity is opposite of pick."""
            if m == 0:
                return 1

            next_is_odd = not is_odd_pick
            if next_is_odd:
                odd_slots = (m + 1) // 2
                even_slots = m // 2
            else:
                even_slots = (m + 1) // 2
                odd_slots = m // 2

            if ro0 != odd_slots or re0 != even_slots:
                return 0
            return fact[ro0] * fact[re0]

        ans: List[int] = []
        prev_is_odd = None  # unknown before first pick

        for i in range(1, n + 1):
            # Determine allowed parity for this position
            if i == 1:
                if ro == re:
                    allow_odd = allow_even = True
                else:
                    # n is odd case: must start with odd
                    allow_odd, allow_even = True, False
            else:
                # Must alternate
                allow_odd = not prev_is_odd
                allow_even = prev_is_odd

            m = n - i
            picked = None

            # Iterate candidates in increasing order
            if allow_odd and allow_even:
                p1 = p2 = 0
                while p1 < len(odds) or p2 < len(evens):
                    if p2 == len(evens) or (p1 < len(odds) and odds[p1] < evens[p2]):
                        x = odds[p1]
                        p1 += 1
                    else:
                        x = evens[p2]
                        p2 += 1

                    is_odd = (x & 1) == 1
                    nro, nre = (ro - 1, re) if is_odd else (ro, re - 1)
                    cnt = completions_after_pick(is_odd, nro, nre, m)
                    if k > cnt:
                        k -= cnt
                    else:
                        picked = x
                        break
            else:
                cand_list = odds if allow_odd else evens
                for x in cand_list:
                    is_odd = (x & 1) == 1
                    nro, nre = (ro - 1, re) if is_odd else (ro, re - 1)
                    cnt = completions_after_pick(is_odd, nro, nre, m)
                    if k > cnt:
                        k -= cnt
                    else:
                        picked = x
                        break

            if picked is None:
                return []

            # Commit the pick: remove from the corresponding list
            ans.append(picked)
            prev_is_odd = (picked & 1) == 1
            if prev_is_odd:
                idx = bisect_left(odds, picked)
                del odds[idx]
                ro -= 1
            else:
                idx = bisect_left(evens, picked)
                del evens[idx]
                re -= 1

        return ans
# @lc code=end
