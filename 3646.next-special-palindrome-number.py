#
# @lc app=leetcode id=3646 lang=python3
#
# [3646] Next Special Palindrome Number
#

# @lc code=start

from typing import Dict, List
import itertools
import sys


class Solution:
    def get_all_pals(self, freq: Dict[int, int], L: int) -> List[str]:
        p = L // 2
        odds = [k for k in freq if freq[k] % 2 == 1]
        multiset: List[str] = []
        if L % 2 == 0:
            for k in freq:
                multiset.extend([str(k)] * (freq[k] // 2))
        else:
            o = odds[0]
            for k in freq:
                cnt = (freq[k] - 1) // 2 if k == o else freq[k] // 2
                multiset.extend([str(k)] * cnt)
        unique_lefts = set(''.join(perm) for perm in itertools.permutations(multiset))
        pals = []
        if L % 2 == 0:
            for left in unique_lefts:
                full = left + left[::-1]
                pals.append(full)
        else:
            middle = str(odds[0])
            for left_paired in unique_lefts:
                full = left_paired + middle + left_paired[::-1]
                pals.append(full)
        return sorted(pals)

    def get_smallest_pal(self, freq: Dict[int, int], L: int) -> str:
        odds = [k for k in freq if freq[k] % 2 == 1]
        if L % 2 == 0:
            count_left = {k: freq[k] // 2 for k in freq}
            left = ''
            for _ in range(L // 2):
                for d in range(1, 10):
                    if count_left.get(d, 0) > 0:
                        left += str(d)
                        count_left[d] -= 1
                        break
            return left + left[::-1]
        else:
            o = odds[0]
            count_left = {}
            for k in freq:
                if k == o:
                    count_left[k] = (freq[k] - 1) // 2
                else:
                    count_left[k] = freq[k] // 2
            left_paired = ''
            p = L // 2
            for _ in range(p):
                for d in range(1, 10):
                    if count_left.get(d, 0) > 0:
                        left_paired += str(d)
                        count_left[d] -= 1
                        break
            middle = str(o)
            left = left_paired + middle
            return left + left_paired[::-1]

    def specialPalindrome(self, n: int) -> int:
        n_str = str(n)
        d = len(n_str)
        odds_list = [1, 3, 5, 7, 9]
        evens_list = [2, 4, 6, 8]
        all_S = []
        # m=0: subsets of evens, non-empty
        for mask in range(1 << 4):
            Se = [evens_list[i] for i in range(4) if (mask & (1 << i))]
            tot = sum(Se)
            if tot > 0:
                freq = {k: k for k in Se}
                all_S.append((tot, freq))
        # m=1: one odd + subsets of evens
        for o in odds_list:
            for mask in range(1 << 4):
                Se = [evens_list[i] for i in range(4) if (mask & (1 << i))]
                tot = sum(Se) + o
                freq = {k: k for k in Se}
                freq[o] = o
                all_S.append((tot, freq))
        candidates = []
        # L == d: smallest pal > n_str for each S
        for Lf, freq in all_S:
            if Lf != d:
                continue
            pals = self.get_all_pals(freq, Lf)
            for pal in pals:
                if pal > n_str:
                    candidates.append(int(pal))
                    break
        # L > d: smallest pal for each S
        for Lf, freq in all_S:
            if Lf > d:
                pal_str = self.get_smallest_pal(freq, Lf)
                candidates.append(int(pal_str))
        return min(candidates)
# @lc code=end