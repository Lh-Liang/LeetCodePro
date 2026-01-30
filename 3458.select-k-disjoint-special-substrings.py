#
# @lc app=leetcode id=3458 lang=python3
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0:
            return True
        n = len(s)
        # Track first and last occurrence for each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
        res = 0
        used = [False] * n  # Track used indices to ensure disjointness
        i = 0
        while i < n:
            # Find candidate substring starting at i
            r = last[s[i]]
            j = i
            while j < r:
                r = max(r, last[s[j]])
                j += 1
            # Check if the substring is not the entire string
            if not (i == 0 and r == n - 1):
                # Verify special: chars within [i,r] do not appear outside
                is_special = True
                for idx in range(i, r + 1):
                    ch = s[idx]
                    if first[ch] < i or last[ch] > r:
                        is_special = False
                        break
                # Ensure disjointness: indices not used before
                if is_special and all(not used[x] for x in range(i, r + 1)):
                    for x in range(i, r + 1):
                        used[x] = True
                    res += 1
                    if res >= k:
                        return True
            i = r + 1
        return res >= k
# @lc code=end