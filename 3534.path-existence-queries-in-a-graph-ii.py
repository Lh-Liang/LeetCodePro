#
# @lc app=leetcode id=3534 lang=python3
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Sort nodes based on their values, keeping track of original indices
        nodes = sorted(zip(nums, range(n)))
        vals = [x[0] for x in nodes]
        
        # Map original index to rank in the sorted array
        rank = [0] * n
        for i, (_, orig_idx) in enumerate(nodes):
            rank[orig_idx] = i
            
        # Identify Connected Components
        # A gap > maxDiff between adjacent sorted values breaks the component
        comp_id = [0] * n
        cid = 0
        for i in range(n - 1):
            if vals[i+1] - vals[i] > maxDiff:
                cid += 1
            comp_id[i+1] = cid
            
        # Binary Lifting Precomputation
        # LOG = 20 is sufficient for N <= 10^5
        LOG = 20
        jump = [[0] * n for _ in range(LOG)]
        
        # Compute jump[0][i]: the furthest index reachable from i in 1 step
        # Since vals is sorted, we can use a sliding window
        right = 0
        for i in range(n):
            # Expand right while the difference is within maxDiff
            while right < n and vals[right] - vals[i] <= maxDiff:
                right += 1
            # The last valid index was right - 1
            jump[0][i] = right - 1
            
        # Fill the binary lifting table
        for k in range(1, LOG):
            for i in range(n):
                jump[k][i] = jump[k-1][jump[k-1][i]]
                
        results = []
        for u, v in queries:
            if u == v:
                results.append(0)
                continue
            
            ru, rv = rank[u], rank[v]
            
            # If nodes are in different connected components, they are unreachable
            if comp_id[ru] != comp_id[rv]:
                results.append(-1)
                continue
            
            # Ensure we are querying from left to right in the sorted array
            if ru > rv:
                ru, rv = rv, ru
            
            # Use binary lifting to find the minimum steps to reach or pass rv
            steps = 0
            curr = ru
            
            # Try to jump as far as possible without reaching rv
            for k in range(LOG - 1, -1, -1):
                if jump[k][curr] < rv:
                    curr = jump[k][curr]
                    steps += (1 << k)
            
            # One more jump is needed to reach the target (or beyond)
            results.append(steps + 1)
            
        return results
# @lc code=end