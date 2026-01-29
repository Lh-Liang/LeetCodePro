#
# @lc app=leetcode id=3525 lang=python3
#
# [3525] Find X Value of Array II
#

# @lc code=start
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        size = 1
        while size < n: 
            size *= 2
        
        tree_prod = [1] * (2 * size)
        tree_counts = [[0] * k for _ in range(2 * size)]

        def merge_into(lc, lp, rc, target):
            # lc: left counts, lp: left total product, rc: right counts
            for i in range(k):
                target[i] = lc[i]
            for i in range(k):
                if rc[i] > 0:
                    target[(lp * i) % k] += rc[i]

        def update_node(idx):
            left = 2 * idx
            right = 2 * idx + 1
            tree_prod[idx] = (tree_prod[left] * tree_prod[right]) % k
            merge_into(tree_counts[left], tree_prod[left], tree_counts[right], tree_counts[idx])

        # Initial build
        for i in range(n):
            val = nums[i] % k
            tree_prod[size + i] = val
            tree_counts[size + i][val] = 1
        
        for i in range(size - 1, 0, -1):
            update_node(i)

        def update(idx, val):
            idx += size
            v = val % k
            tree_prod[idx] = v
            tree_counts[idx] = [0] * k
            tree_counts[idx][v] = 1
            while idx > 1:
                idx //= 2
                update_node(idx)

        def query(l, r):
            l += size
            r += size
            l_res_prod = 1
            l_res_counts = [0] * k
            
            # Collect indices for the right-side parts to merge in correct order
            r_parts = []
            while l <= r:
                if l % 2 == 1:
                    new_counts = [0] * k
                    merge_into(l_res_counts, l_res_prod, tree_counts[l], new_counts)
                    l_res_counts = new_counts
                    l_res_prod = (l_res_prod * tree_prod[l]) % k
                    l += 1
                if r % 2 == 0:
                    r_parts.append(r)
                    r -= 1
                l //= 2
                r //= 2
            
            for node_idx in reversed(r_parts):
                new_counts = [0] * k
                merge_into(l_res_counts, l_res_prod, tree_counts[node_idx], new_counts)
                l_res_counts = new_counts
                l_res_prod = (l_res_prod * tree_prod[node_idx]) % k
                
            return l_res_counts

        results = []
        for indexi, valuei, starti, xi in queries:
            update(indexi, valuei)
            res_counts = query(starti, n - 1)
            results.append(res_counts[xi])
            
        return results
# @lc code=end