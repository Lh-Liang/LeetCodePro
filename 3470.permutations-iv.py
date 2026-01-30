#
# @lc app=leetcode id=3470 lang=python3
#
# [3470] Permutations IV
#

# @lc code=start
from typing import List
import functools

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        odds = [x for x in range(1, n+1) if x%2 == 1]
        evens = [x for x in range(1, n+1) if x%2 == 0]
        total_odd, total_even = len(odds), len(evens)
        used = [False] * (n+1)

        @functools.lru_cache(None)
        def dp(remain_odd, remain_even, last_parity):
            if remain_odd == 0 and remain_even == 0:
                return 1
            res = 0
            if last_parity != 1 and remain_odd > 0:
                res += remain_odd * dp(remain_odd-1, remain_even, 1)
            if last_parity != 0 and remain_even > 0:
                res += remain_even * dp(remain_odd, remain_even-1, 0)
            return res

        answer = []
        curr_odd, curr_even = total_odd, total_even
        last_parity = -1  # start with any
        for pos in range(n):
            for x in range(1, n+1):
                if used[x]:
                    continue
                this_parity = x % 2
                if last_parity != -1 and this_parity == last_parity:
                    continue
                num_ways = dp(curr_odd - (this_parity==1), curr_even - (this_parity==0), this_parity)
                if k > num_ways:
                    k -= num_ways
                else:
                    answer.append(x)
                    used[x] = True
                    if this_parity == 1:
                        curr_odd -= 1
                    else:
                        curr_even -= 1
                    last_parity = this_parity
                    break
            else:
                return []
        # Verification step: Check adjacent parity and length
        if len(answer) != n:
            return []
        for i in range(1, n):
            if (answer[i] % 2) == (answer[i-1] % 2):
                return []
        return answer
# @lc code=end