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
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            if first[idx] == n:
                first[idx] = i
            last[idx] = i

        intervals = []

        # Build minimal valid intervals starting at first occurrence of each character
        for c in range(26):
            l = first[c]
            if l == n:
                continue
            r = last[c]
            i = l
            valid = True
            while i <= r:
                x = ord(s[i]) - 97
                if first[x] < l:
                    valid = False
                    break
                r = max(r, last[x])
                i += 1

            if valid and not (l == 0 and r == n - 1):
                intervals.append((l, r))

        # Maximum number of non-overlapping intervals via greedy scheduling
        intervals.sort(key=lambda p: (p[1], -p[0]))

        count = 0
        end = -1
        for l, r in intervals:
            if l > end:
                count += 1
                end = r
                if count >= k:
                    return True

        return False
# @lc code=end
