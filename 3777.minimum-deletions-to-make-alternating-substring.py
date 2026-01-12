#
# @lc app=leetcode id=3777 lang=python3
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        s_list = list(s)
        bit = [0] * (n + 1)
        
        def update(i, delta):
            while i < n:
                bit[i] += delta
                i += i & (-i)
        
        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & (-i)
            return res

        # x[i] is 1 if s[i] == s[i+1], else 0
        x = [0] * (n - 1)
        for i in range(n - 1):
            if s_list[i] == s_list[i+1]:
                x[i] = 1
                update(i + 1, 1)
        
        results = []
        for q in queries:
            if q[0] == 1:
                j = q[1]
                s_list[j] = 'B' if s_list[j] == 'A' else 'A'
                # Flipping s[j] affects x[j-1] and x[j]
                for i in (j - 1, j):
                    if 0 <= i < n - 1:
                        new_val = 1 if s_list[i] == s_list[i+1] else 0
                        if new_val != x[i]:
                            update(i + 1, new_val - x[i])
                            x[i] = new_val
            else:
                l, r = q[1], q[2]
                # Minimum deletions for substring s[l..r] is sum of x[i] for i in [l, r-1]
                # This corresponds to range [l+1, r] in 1-indexed BIT
                if l < r:
                    results.append(query(r) - query(l))
                else:
                    results.append(0)
        
        return results
# @lc code=end