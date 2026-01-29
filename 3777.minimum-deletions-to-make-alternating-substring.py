#
# @lc app=leetcode id=3777 lang=python3
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        ans = []
        N = n - 1

        def update(tree, size, idx, delta):
            while idx <= size:
                tree[idx] += delta
                idx += idx & -idx

        def prefix_sum(tree, idx):
            res = 0
            while idx > 0:
                res += tree[idx]
                idx -= idx & -idx
            return res

        tree = [0] * (N + 2)

        # Initialize
        if N > 0:
            prev = s[0]
            for i in range(1, n):
                curr = s[i]
                val = 1 if prev != curr else 0
                update(tree, N, i, val)
                prev = curr

        for q in queries:
            if q[0] == 1:
                j = q[1]
                if j > 0:
                    idx = j
                    curr_val = prefix_sum(tree, idx) - prefix_sum(tree, idx - 1)
                    delta = 1 - 2 * curr_val
                    update(tree, N, idx, delta)
                if j < n - 1:
                    idx = j + 1
                    curr_val = prefix_sum(tree, idx) - prefix_sum(tree, idx - 1)
                    delta = 1 - 2 * curr_val
                    update(tree, N, idx, delta)
            else:
                l, r = q[1], q[2]
                m = r - l + 1
                if m <= 1:
                    ans.append(0)
                    continue
                sum_changes = prefix_sum(tree, r) - prefix_sum(tree, l)
                deletions = m - 1 - sum_changes
                ans.append(deletions)
        return ans

# @lc code=end