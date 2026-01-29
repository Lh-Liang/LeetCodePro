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

        def update(idx, val):
            idx += 1  # 1-based indexing
            while idx <= n:
                bit[idx] += val
                idx += idx & (-idx)

        def query(idx):
            idx += 1
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & (-idx)
            return res

        def get_sum(l, r):
            if l > r: return 0
            return query(r) - query(l - 1)

        # Initialize BIT with adjacent identical pairs
        # B[i] = 1 if s[i] == s[i+1]
        for i in range(n - 1):
            if s_list[i] == s_list[i+1]:
                update(i, 1)

        ans = []
        for q in queries:
            if q[0] == 1:
                j = q[1]
                # Potential pairs affected: (j-1, j) and (j, j+1)
                for k in [j - 1, j]:
                    if 0 <= k < n - 1:
                        if s_list[k] == s_list[k+1]:
                            update(k, -1)
                
                # Flip character
                s_list[j] = 'B' if s_list[j] == 'A' else 'A'
                
                # Re-add if they are now identical
                for k in [j - 1, j]:
                    if 0 <= k < n - 1:
                        if s_list[k] == s_list[k+1]:
                            update(k, 1)
            else:
                _, l, r = q
                # Deletions needed for s[l..r] is sum of B[i] for i in [l, r-1]
                ans.append(get_sum(l, r - 1))
        
        return ans
# @lc code=end