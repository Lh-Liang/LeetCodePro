#
# @lc app=leetcode id=3762 lang=python3
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        y = [x // k for x in nums]
        rems = [x % k for x in nums]
        
        # Prefix sum to check if all elements in nums[li...ri] have same remainder mod k
        diff_rem = [0] * n
        for i in range(1, n):
            diff_rem[i] = diff_rem[i-1] + (1 if rems[i] != rems[i-1] else 0)
            
        # Coordinate compression for y values
        sorted_y = sorted(list(set(y)))
        rank_map = {val: i for i, val in enumerate(sorted_y)}
        m = len(sorted_y)
        
        # Persistent Segment Tree: store count and sum of y values
        tree_cnt = [0] * (n * 35)
        tree_sum = [0] * (n * 35)
        L = [0] * (n * 35)
        R = [0] * (n * 35)
        roots = [0] * (n + 1)
        node_ptr = 0
        
        def update(prev, l, r, val_idx, val):
            nonlocal node_ptr
            node_ptr += 1
            curr = node_ptr
            tree_cnt[curr] = tree_cnt[prev] + 1
            tree_sum[curr] = tree_sum[prev] + val
            L[curr] = L[prev]
            R[curr] = R[prev]
            if l == r:
                return curr
            mid = (l + r) // 2
            if val_idx <= mid:
                L[curr] = update(L[prev], l, mid, val_idx, val)
            else:
                R[curr] = update(R[prev], mid + 1, r, val_idx, val)
            return curr

        for i in range(n):
            roots[i+1] = update(roots[i], 0, m - 1, rank_map[y[i]], y[i])
            
        # Single pass to find median and calculate operations
        def query_ops(node_l, node_r, l, r, k_th, total_sum, total_cnt):
            if l == r:
                median = sorted_y[l]
                # All elements in this range are equal to median
                return median
            
            mid = (l + r) // 2
            cnt_l = tree_cnt[L[node_r]] - tree_cnt[L[node_l]]
            sum_l = tree_sum[L[node_r]] - tree_sum[L[node_l]]
            
            if k_th <= cnt_l:
                return query_ops(L[node_l], L[node_r], l, mid, k_th, total_sum, total_cnt)
            else:
                # Median is in the right child. We know everything in left child is < median.
                # We pass down the logic or just return median and calculate outside.
                return query_ops(R[node_l], R[node_r], mid + 1, r, k_th - cnt_l, total_sum, total_cnt)

        def get_stats(node_l, node_r, l, r, q_rank):
            # Returns (count, sum) of elements with rank <= q_rank
            if r <= q_rank:
                return tree_cnt[node_r] - tree_cnt[node_l], tree_sum[node_r] - tree_sum[node_l]
            mid = (l + r) // 2
            c, s = get_stats(L[node_l], L[node_r], l, mid, q_rank)
            if q_rank > mid:
                c2, s2 = get_stats(R[node_l], R[node_r], mid + 1, r, q_rank)
                c += c2
                s += s2
            return c, s

        ans = []
        for li, ri in queries:
            # Check if all elements in nums[li...ri] have same remainder
            if diff_rem[ri] - diff_rem[li] > 0:
                ans.append(-1)
                continue
            
            size = ri - li + 1
            mid_rank_in_window = (size + 1) // 2
            median = query_ops(roots[li], roots[ri+1], 0, m - 1, mid_rank_in_window, 0, 0)
            
            # Calculate sum of |y_i - median|
            # ops = (cnt_le * median - sum_le) + (sum_gt - cnt_gt * median)
            med_idx = rank_map[median]
            cnt_le, sum_le = get_stats(roots[li], roots[ri+1], 0, m - 1, med_idx)
            
            total_sum = tree_sum[roots[ri+1]] - tree_sum[roots[li]]
            sum_gt = total_sum - sum_le
            cnt_gt = size - cnt_le
            
            res = (cnt_le * median - sum_le) + (sum_gt - cnt_gt * median)
            ans.append(res)
            
        return ans
# @lc code=end