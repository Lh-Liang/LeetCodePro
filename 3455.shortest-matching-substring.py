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
        p1, p2, p3 = parts[0], parts[1], parts[2]
        n1, n2, n3 = len(p1), len(p2), len(p3)
        n = len(s)

        def get_all_occurrences(pattern, text):
            if not pattern: return []
            # KMP algorithm for O(N + M) matching
            m = len(pattern)
            lps = [0] * m
            j = 0
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                lps[i] = j
            
            res = []
            j = 0
            for i in range(len(text)):
                while j > 0 and text[i] != pattern[j]:
                    j = lps[j-1]
                if text[i] == pattern[j]:
                    j += 1
                if j == m:
                    res.append(i - m + 1)
                    j = lps[j-1]
            return res

        S1 = get_all_occurrences(p1, s)
        S2 = get_all_occurrences(p2, s)
        S3 = get_all_occurrences(p3, s)

        # If a required part is missing
        if (p1 and not S1) or (p2 and not S2) or (p3 and not S3):
            return -1

        ans = float('inf')

        if p2:
            for s2 in S2:
                # Find best s1: max index in S1 such that s1 + n1 <= s2
                if not p1:
                    s1_best = s2
                else:
                    idx1 = bisect.bisect_right(S1, s2 - n1) - 1
                    s1_best = S1[idx1] if idx1 >= 0 else None
                
                # Find best s3: min index in S3 such that s3 >= s2 + n2
                if not p3:
                    s3_end = s2 + n2
                else:
                    idx3 = bisect.bisect_left(S3, s2 + n2)
                    s3_end = S3[idx3] + n3 if idx3 < len(S3) else None
                
                if s1_best is not None and s3_end is not None:
                    ans = min(ans, s3_end - s1_best)
        else:
            # p2 is empty, constraint is s1 + n1 <= s3
            if not p1 and not p3:
                return 0
            elif not p1:
                return n3
            elif not p3:
                return n1
            else:
                # Both p1 and p3 exist, p2 is empty
                for s3 in S3:
                    idx1 = bisect.bisect_right(S1, s3 - n1) - 1
                    if idx1 >= 0:
                        ans = min(ans, (s3 + n3) - S1[idx1])

        return int(ans) if ans != float('inf') else -1
# @lc code=end