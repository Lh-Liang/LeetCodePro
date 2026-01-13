#
# @lc app=leetcode id=3455 lang=python3
#
# [3455] Shortest Matching Substring
#

# @lc code=start
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        n = len(s)

        # Split p into A*B*C (exactly two '*')
        i1 = p.find('*')
        i2 = p.find('*', i1 + 1)
        A = p[:i1]
        B = p[i1 + 1:i2]
        C = p[i2 + 1:]

        def kmp_matches(text: str, pat: str):
            """Return boolean array match[i] (0<=i<=n) if pat matches text starting at i.
            If pat is empty, it matches at every i (including n).
            """
            nn = len(text)
            m = len(pat)
            if m == 0:
                return [True] * (nn + 1)

            # prefix function
            pi = [0] * m
            for i in range(1, m):
                j = pi[i - 1]
                while j > 0 and pat[i] != pat[j]:
                    j = pi[j - 1]
                if pat[i] == pat[j]:
                    j += 1
                pi[i] = j

            res = [False] * (nn + 1)
            j = 0
            for i, ch in enumerate(text):
                while j > 0 and ch != pat[j]:
                    j = pi[j - 1]
                if ch == pat[j]:
                    j += 1
                if j == m:
                    start = i - m + 1
                    res[start] = True
                    j = pi[j - 1]
            return res

        Amatch = kmp_matches(s, A)
        Bmatch = kmp_matches(s, B)
        Cmatch = kmp_matches(s, C)

        lenA, lenB, lenC = len(A), len(B), len(C)
        INF = 10**18

        # nextC[i] = smallest j>=i with Cmatch[j]
        nextC = [INF] * (n + 2)
        nextC[n] = n if Cmatch[n] else INF
        for i in range(n - 1, -1, -1):
            nextC[i] = i if Cmatch[i] else nextC[i + 1]

        # minEndFromB[i] = minimal end position (exclusive) for some B at b>=i then C after it
        minEndFromB = [INF] * (n + 2)
        minEndFromB[n + 1] = INF
        for i in range(n, -1, -1):
            best = minEndFromB[i + 1]
            if Bmatch[i]:
                endB = i + lenB
                if endB <= n:
                    cpos = nextC[endB]
                    if cpos != INF:
                        end = cpos + lenC
                        if end < best:
                            best = end
            minEndFromB[i] = best

        ans = INF
        for l in range(0, n + 1):
            if not Amatch[l]:
                continue
            posAend = l + lenA
            if posAend > n:
                continue
            end = minEndFromB[posAend]
            if end != INF:
                cand = end - l
                if cand < ans:
                    ans = cand

        return -1 if ans == INF else ans
# @lc code=end
