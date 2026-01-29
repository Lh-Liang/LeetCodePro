#
# @lc app=leetcode id=3525 lang=python3
#
# [3525] Find X Value of Array II
#

# @lc code=start
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # Each node: [total_product_mod_k, counts_array_of_size_k]
        tree_prod = [1] * (4 * n)
        tree_counts = [[0] * k for _ in range(4 * n)]

        def merge(left_prod, left_counts, right_prod, right_counts):
            new_prod = (left_prod * right_prod) % k
            new_counts = list(left_counts)
            for i in range(k):
                if right_counts[i] > 0:
                    target = (left_prod * i) % k
                    new_counts[target] += right_counts[i]
            return new_prod, new_counts

        def build(node, start, end):
            if start == end:
                val = nums[start] % k
                tree_prod[node] = val
                tree_counts[node][val] = 1
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree_prod[node], tree_counts[node] = merge(
                tree_prod[2 * node], tree_counts[2 * node],
                tree_prod[2 * node + 1], tree_counts[2 * node + 1]
            )

        def update(node, start, end, idx, val):
            if start == end:
                v = val % k
                tree_prod[node] = v
                tree_counts[node] = [0] * k
                tree_counts[node][v] = 1
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree_prod[node], tree_counts[node] = merge(
                tree_prod[2 * node], tree_counts[2 * node],
                tree_prod[2 * node + 1], tree_counts[2 * node + 1]
            )

        def query(node, start, end, l, r):
            if l <= start and end <= r:
                return tree_prod[node], tree_counts[node]
            mid = (start + end) // 2
            if r <= mid:
                return query(2 * node, start, mid, l, r)
            if l > mid:
                return query(2 * node + 1, mid + 1, end, l, r)
            
            lp, lc = query(2 * node, start, mid, l, mid)
            rp, rc = query(2 * node + 1, mid + 1, end, mid + 1, r)
            return merge(lp, lc, rp, rc)

        build(1, 0, n - 1)
        results = []
        for idx, val, start_i, x_i in queries:
            update(1, 0, n - 1, idx, val)
            _, counts = query(1, 0, n - 1, start_i, n - 1)
            results.append(counts[x_i])
        return results
# @lc code=end