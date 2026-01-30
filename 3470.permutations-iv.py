#
# @lc app=leetcode id=3470 lang=python3
#
# [3470] Permutations IV
#

# @lc code=start
from typing import List
from functools import lru_cache

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        # Precompute odds and evens
        odds = [i for i in range(1, n+1) if i % 2 == 1]
        evens = [i for i in range(1, n+1) if i % 2 == 0]

        @lru_cache(maxsize=None)
        def count(used_mask: int, last_val: int, last_parity: int) -> int:
            # last_parity: 0 for even, 1 for odd, -1 for start
            # last_val is not used for constraints, only parity matters
            cnt = 0
            if bin(used_mask).count('1') == n:
                return 1
            for nxt in range(1, n+1):
                if (used_mask >> (nxt-1)) & 1:
                    continue
                parity = nxt % 2
                if last_parity != -1 and parity == last_parity:
                    continue
                cnt += count(used_mask | (1 << (nxt-1)), nxt, parity)
            return cnt

        answer = []
        used_mask = 0
        last_parity = -1
        for pos in range(n):
            found = False
            for nxt in range(1, n+1):
                if (used_mask >> (nxt-1)) & 1:
                    continue
                parity = nxt % 2
                if last_parity != -1 and parity == last_parity:
                    continue
                cnt = count(used_mask | (1 << (nxt-1)), nxt, parity)
                if cnt < k:
                    k -= cnt
                else:
                    answer.append(nxt)
                    used_mask |= (1 << (nxt-1))
                    last_parity = parity
                    found = True
                    break
            if not found:
                return []
        return answer
# @lc code=end