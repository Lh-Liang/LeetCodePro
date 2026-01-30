#
# @lc app=leetcode id=3646 lang=python3
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
class Solution:
    def specialPalindrome(self, n: int) -> int:
        # Step 1: Analyze feasible digit count combinations for special palindromes
        # Step 2: Avoid generating all permutations; instead, construct palindromes directly using digit count constraints
        # Step 3: For each possible length (starting from len(n)+1), generate all multisets {digit: count} where count==digit and sum(counts)==total length
        # Step 4: For each valid multiset, attempt to build palindromic numbers directly (using counts symmetry)
        # Step 5: For each constructed palindrome, check if it is strictly greater than n
        # Step 6: Track the minimal valid palindrome found
        # Note: This approach avoids brute-force permutation and uses analytical reasoning to construct palindromes efficiently
        from collections import Counter
        nlen = len(str(n))
        res = None
        # Helper to attempt to build all palindromes for given digit counts
        def build_palindromes(dcount):
            digits = []
            for d, c in dcount.items():
                digits.extend([str(d)]*c)
            # Identify digits with odd count (if any)
            odd_digits = [d for d, c in dcount.items() if c % 2]
            half = []
            center = ''
            for d in sorted(dcount):
                half.extend([str(d)]*(dcount[d]//2))
                if dcount[d] % 2:
                    center = str(d)
            from itertools import permutations
            seen = set()
            for p in set(permutations(half)):
                if p[0] == '0':
                    continue
                left = ''.join(p)
                pal = left + center + left[::-1]
                if int(pal) > n:
                    yield int(pal)
        # Try all possible lengths
        for total_len in range(2, nlen+4):
            # Find all assignments of digits 1..9 where k appears k times and sum==total_len
            def dfs(idx, curr, left):
                if idx == 10:
                    if left == 0 and curr:
                        dcount = {k: k for k in curr}
                        # Palindrome possible if at most one odd count
                        odd = sum(1 for v in dcount.values() if v % 2)
                        if (total_len % 2 == 0 and odd == 0) or (total_len % 2 == 1 and odd == 1):
                            for val in build_palindromes(dcount):
                                nonlocal res
                                if res is None or val < res:
                                    res = val
                    return
                if idx > 0 and left >= idx:
                    curr.append(idx)
                    dfs(idx+1, curr, left-idx)
                    curr.pop()
                dfs(idx+1, curr, left)
            dfs(1, [], total_len)
            if res is not None:
                return res
        return -1
# @lc code=end