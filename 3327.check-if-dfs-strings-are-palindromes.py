#
# @lc app=leetcode id=3327 lang=python3
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
        
        # Sort children to ensure increasing order traversal
        # Since the problem statement says "Iterate over each child y of x in increasing order"
        # we need to make sure the adjacency list reflects that.
        # Although indices are usually added in order if the input is sorted, 
        # the problem gives parent array, so children order isn't guaranteed by input order.
        # Sorting takes O(N log N) in worst case (star graph).
        for i in range(n):
            adj[i].sort()
            
        # To store the DFS string logic mapping
        # The dfsStr for node i is a substring of the total post-order traversal string.
        # Let's verify this. 
        # dfs(x): for y in children: dfs(y); append s[x]
        # This constructs a string where the subtree's characters appear contiguously.
        
        dfs_order = []
        # range_map stores [start, end] indices in the dfs_order string for each node
        node_ranges = [[0, 0] for _ in range(n)]
        
        # Iterative DFS to avoid recursion depth issues
        # Stack stores: (node, child_index)
        stack = [0]
        # To emulate the post-order construction, we can track entry/exit
        # But simpler with explicit stack management or recursion limit increase
        # Given N=10^5, recursion limit is safer.
        
        import sys
        sys.setrecursionlimit(200000)
        
        # We need the global string T
        T = []
        
        def dfs(u):
            # The start index of the substring for node u in T
            start_idx = len(T)
            
            for v in adj[u]:
                dfs(v)
            
            T.append(s[u])
            # The end index of the substring for node u in T
            end_idx = len(T) - 1
            node_ranges[u] = [start_idx, end_idx]

        dfs(0)
        
        full_s = "".join(T)
        m = len(full_s)
        
        # Manacher's algorithm is O(N) and precise, but Manacher gives palindromes centered at indices.
        # Here we check arbitrary substrings. Hashing is better.
        # We need to check if full_s[start:end+1] is a palindrome.
        
        # Rolling Hash configuration
        MOD = 10**9 + 7
        BASE = 131 # A prime number greater than alphabet size
        
        # Precompute powers
        pow_base = [1] * (m + 1)
        for i in range(1, m + 1):
            pow_base[i] = (pow_base[i-1] * BASE) % MOD
            
        # Forward Hash
        h_fwd = [0] * (m + 1)
        for i in range(m):
            h_fwd[i+1] = (h_fwd[i] * BASE + ord(full_s[i])) % MOD
            
        # Backward Hash (Hash of the reversed string)
        # It's easier to check palindrome by comparing hash(S[i...j]) with hash(Reverse(S)[...])
        # or simply compute hash of substring in reverse direction.
        # Let's build a prefix hash for the reversed string.
        rev_s = full_s[::-1]
        h_bwd = [0] * (m + 1)
        for i in range(m):
            h_bwd[i+1] = (h_bwd[i] * BASE + ord(rev_s[i])) % MOD
            
        def get_hash(h_arr, l, r):
            # Returns hash of substring from index l to r (inclusive, 0-indexed)
            # Length is r - l + 1
            # H[r+1] - H[l] * B^(len)
            return (h_arr[r+1] - h_arr[l] * pow_base[r - l + 1]) % MOD
            
        ans = [False] * n
        for i in range(n):
            l, r = node_ranges[i]
            length = r - l + 1
            
            # Forward hash of T[l...r]
            fh = get_hash(h_fwd, l, r)
            
            # Backward hash corresponds to segment in rev_s.
            # T[l...r] reversed is rev_s[m-1-r ... m-1-l]
            # Let's map indices:
            # Index l in T corresponds to index m-1-l in rev_s
            # Index r in T corresponds to index m-1-r in rev_s
            # Since rev_s is reversed, the segment starts at m-1-r and ends at m-1-l
            rl, rr = m - 1 - r, m - 1 - l
            bh = get_hash(h_bwd, rl, rr)
            
            if fh == bh:
                ans[i] = True
                
        return ans
# @lc code=end