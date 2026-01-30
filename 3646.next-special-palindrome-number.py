#
# @lc app=leetcode id=3646 lang=python3
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
class Solution:
    def specialPalindrome(self, n: int) -> int:
        from itertools import combinations, permutations
        n = int(n)
        res = float('inf')
        digits = [str(i) for i in range(1, 10)]
        from collections import Counter

        # Generate all subsets of digits (since digit k must appear exactly k times)
        for l in range(1, 10):
            for comb in combinations(digits, l):
                counts = {}
                total = 0
                for d in comb:
                    k = int(d)
                    counts[d] = k
                    total += k
                # Try to build palindrome
                odd = [d for d in counts if counts[d] % 2 == 1]
                if len(odd) > 1:
                    continue
                # Build half string
                half = []
                for d in sorted(counts):
                    half.extend([d] * (counts[d] // 2))
                centers = odd if odd else ['']
                used = set()
                for center in centers:
                    # Permute half to form palindrome (avoid duplicates)
                    for perm in set(permutations(half)):
                        if perm and perm[0] == '0':
                            continue
                        half_str = ''.join(perm)
                        pal = half_str + center + half_str[::-1]
                        if pal and int(pal) > n and int(pal) < res:
                            res = int(pal)
        return res
# @lc code=end