#
# @lc app=leetcode id=3455 lang=python3
#
# [3455] Shortest Matching Substring
#

# @lc code=start
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        # Special case: pattern is '**', matches empty substring
        if p == '**':
            return 0
        # Split pattern into prefix, mid, suffix
        stars = [i for i, c in enumerate(p) if c == '*']
        pre = p[:stars[0]]
        mid = p[stars[0]+1:stars[1]]
        suf = p[stars[1]+1:]
        n = len(s)
        min_len = float('inf')
        for i in range(n+1):
            # Try matching prefix at position i
            if i+len(pre) > n:
                break
            if s[i:i+len(pre)] != pre:
                continue
            # Now look for mid and suf after the first star
            start1 = i+len(pre)
            for j in range(start1, n+1):
                # Try matching mid at position j
                if j+len(mid) > n:
                    break
                if s[j:j+len(mid)] != mid:
                    continue
                # Now look for suf after the second star
                start2 = j+len(mid)
                for k in range(start2, n+1):
                    if k+len(suf) > n:
                        break
                    if s[k:k+len(suf)] != suf:
                        continue
                    # The boundaries are: i ... k+len(suf)-1
                    min_len = min(min_len, k+len(suf)-i)
        return -1 if min_len == float('inf') else min_len
# @lc code=end