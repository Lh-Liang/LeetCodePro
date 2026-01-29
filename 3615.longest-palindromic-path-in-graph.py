#
# @lc app=leetcode id=3615 lang=python3
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        pop = [bin(i).count('1') for i in range(1 << n)]
        ans = 1
        SHIFT = 1 << n
        SIZE = n * n * SHIFT
        def compute_maxk(s_ul, s_ur, s_mask, centers):
            visited = bytearray(SIZE)
            local_maxk = [0]
            def _dfs(ul, ur, mask):
                idx = ((ul * n + ur) * SHIFT) + mask
                if visited[idx]:
                    return
                visited[idx] = 1
                used = pop[mask]
                k = (used - centers) // 2
                if k > local_maxk[0]:
                    local_maxk[0] = k
                for nl in adj[ul]:
                    if (mask & (1 << nl)) == 0:
                        chl = label[nl]
                        for nr in adj[ur]:
                            if (mask & (1 << nr)) == 0 and nl != nr and label[nr] == chl:
                                new_mask = mask | (1 << nl) | (1 << nr)
                                _dfs(nl, nr, new_mask)
            _dfs(s_ul, s_ur, s_mask)
            return local_maxk[0]
        # odd lengths
        for c in range(n):
            mk = compute_maxk(c, c, 1 << c, 1)
            ans = max(ans, 1 + 2 * mk)
        # even lengths
        for u in range(n):
            for v in adj[u]:
                if u < v and label[u] == label[v]:
                    mk = compute_maxk(u, v, (1 << u) | (1 << v), 2)
                    ans = max(ans, 2 + 2 * mk)
        return ans

# @lc code=end