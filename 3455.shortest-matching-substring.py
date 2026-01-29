#
# @lc app=leetcode id=3455 lang=python3
#
# [3455] Shortest Matching Substring
#

# @lc code=start
import bisect

class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        parts = p.split('*')
        p1, p2, p3 = parts
        n = len(s)

        def get_indices(pattern):
            if not pattern: return []
            res = []
            curr = s.find(pattern)
            while curr != -1:
                res.append(curr)
                curr = s.find(pattern, curr + 1)
            return res

        idx1 = get_indices(p1)
        idx2 = get_indices(p2)
        idx3 = get_indices(p3)

        # If a non-empty part is not found, no match is possible
        if (p1 and not idx1) or (p2 and not idx2) or (p3 and not idx3):
            return -1

        ans = float('inf')
        l1, l2, l3 = len(p1), len(p2), len(p3)

        if p2:
            # Iterate through middle part occurrences
            for k in idx2:
                # Find largest i such that i + l1 <= k
                if not p1:
                    i = k
                else:
                    pos = bisect.bisect_right(idx1, k - l1)
                    if pos == 0: continue
                    i = idx1[pos - 1]
                
                # Find smallest j such that j >= k + l2
                if not p3:
                    j = k + l2
                else:
                    pos = bisect.bisect_left(idx3, k + l2)
                    if pos == len(idx3): continue
                    j = idx3[pos]
                
                ans = min(ans, (j + l3) - i)
        else:
            # p2 is empty, match p1 and p3 directly
            if not p1 and not p3:
                return 0
            if not p1:
                return l3
            if not p3:
                return l1
            
            for j in idx3:
                pos = bisect.bisect_right(idx1, j - l1)
                if pos > 0:
                    i = idx1[pos - 1]
                    ans = min(ans, (j + l3) - i)

        return int(ans) if ans != float('inf') else -1
# @lc code=end