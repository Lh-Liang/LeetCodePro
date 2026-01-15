#
# @lc app=leetcode id=3525 lang=python3
#
# [3525] Find X Value of Array II
#

# @lc code=start
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        
        identity = ([0] * k, 1)
        tree = [None] * (4 * n)
        
        def merge(left_node, right_node):
            left_cnt, left_prod = left_node
            right_cnt, right_prod = right_node
            cnt = left_cnt[:]
            for rr in range(k):
                combined = (left_prod * rr) % k
                cnt[combined] += right_cnt[rr]
            prod = (left_prod * right_prod) % k
            return (cnt, prod)
        
        def build(node, start, end):
            if start == end:
                v = nums[start] % k
                cnt = [0] * k
                cnt[v] = 1
                tree[node] = (cnt, v)
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])
        
        def update(node, start, end, idx, val):
            if start == end:
                v = val % k
                cnt = [0] * k
                cnt[v] = 1
                tree[node] = (cnt, v)
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])
        
        def query(node, start, end, l, r):
            if l > end or r < start:
                return identity
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            left_result = query(2 * node, start, mid, l, r)
            right_result = query(2 * node + 1, mid + 1, end, l, r)
            return merge(left_result, right_result)
        
        build(1, 0, n - 1)
        
        result = []
        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)
            cnt, _ = query(1, 0, n - 1, start, n - 1)
            result.append(cnt[x])
        
        return result
# @lc code=end