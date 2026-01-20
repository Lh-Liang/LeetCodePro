class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        m = 1
        while m < n:
            m *= 2
        
        identity_prod = 1 % k
        identity_counts = [0] * k
        
        # tree[i] stores (product_modulo_k, counts_array)
        # counts_array[rem] stores the number of prefixes in the range with product % k == rem
        tree = [(identity_prod, list(identity_counts)) for _ in range(2 * m)]
        
        # Initialize leaves
        for i in range(n):
            val = nums[i]
            p = val % k
            c = [0] * k
            c[p] = 1
            tree[m + i] = (p, c)
            
        # Build tree
        for i in range(m - 1, 0, -1):
            lp, lc = tree[2 * i]
            rp, rc = tree[2 * i + 1]
            
            np = (lp * rp) % k
            nc = lc[:]
            for r, count in enumerate(rc):
                if count > 0:
                    nc[(lp * r) % k] += count
            
            tree[i] = (np, nc)
            
        results = []
        
        for index, value, start, x in queries:
            # Update point
            idx = m + index
            p = value % k
            c = [0] * k
            c[p] = 1
            tree[idx] = (p, c)
            
            # Propagate changes up
            curr = idx // 2
            while curr > 0:
                lp, lc = tree[2 * curr]
                rp, rc = tree[2 * curr + 1]
                
                np = (lp * rp) % k
                nc = lc[:]
                for r, count in enumerate(rc):
                    if count > 0:
                        nc[(lp * r) % k] += count
                
                tree[curr] = (np, nc)
                curr //= 2
            
            # Query range [start, n-1]
            l, r = m + start, m + n - 1
            
            la_p, la_c = identity_prod, list(identity_counts)
            ra_nodes = []
            
            while l <= r:
                if l % 2 == 1:
                    node_p, node_c = tree[l]
                    new_c = la_c[:]
                    for rem, count in enumerate(node_c):
                        if count > 0:
                            new_c[(la_p * rem) % k] += count
                    la_p = (la_p * node_p) % k
                    la_c = new_c
                    l += 1
                
                if r % 2 == 0:
                    ra_nodes.append(tree[r])
                    r -= 1
                
                l //= 2
                r //= 2
            
            # Merge right accumulator nodes in correct order
            curr_p, curr_c = la_p, la_c
            while ra_nodes:
                node_p, node_c = ra_nodes.pop()
                new_c = curr_c[:]
                for rem, count in enumerate(node_c):
                    if count > 0:
                        new_c[(curr_p * rem) % k] += count
                curr_p = (curr_p * node_p) % k
                curr_c = new_c
                
            results.append(curr_c[x])
            
        return results