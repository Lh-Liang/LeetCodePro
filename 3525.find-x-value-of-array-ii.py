#
# @lc app=leetcode id=3525 lang=python3
#
# [3525] Find X Value of Array II
#

# @lc code=start
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        size = 1 << (n - 1).bit_length()
        tree_prod = [1 % k] * (2 * size)
        tree_cnt = [0] * (2 * size * k)

        def update(i, val):
            idx = i + size
            val %= k
            tree_prod[idx] = val
            base = idx * k
            for j in range(k):
                tree_cnt[base + j] = 0
            tree_cnt[base + val] = 1
            while idx > 1:
                idx >>= 1
                left = 2 * idx
                right = 2 * idx + 1
                l_p = tree_prod[left]
                r_p = tree_prod[right]
                tree_prod[idx] = (l_p * r_p) % k
                
                curr_base = idx * k
                l_base = left * k
                r_base = right * k
                for j in range(k):
                    tree_cnt[curr_base + j] = tree_cnt[l_base + j]
                for j in range(k):
                    if tree_cnt[r_base + j]:
                        tree_cnt[curr_base + (l_p * j) % k] += tree_cnt[r_base + j]

        for i, v in enumerate(nums):
            update(i, v)

        results = []
        for idx, val, start, x_val in queries:
            update(idx, val)
            
            # Query range [start, n-1]
            l, r = start + size, n + size
            res_l_p, res_l_c = 1 % k, [0] * k
            res_r_p, res_r_c = 1 % k, [0] * k
            
            while l < r:
                if l & 1:
                    # Merge res_l and tree[l]
                    new_l_c = list(res_l_c)
                    l_base = l * k
                    for j in range(k):
                        if tree_cnt[l_base + j]:
                            new_l_c[(res_l_p * j) % k] += tree_cnt[l_base + j]
                    res_l_p = (res_l_p * tree_prod[l]) % k
                    res_l_c = new_l_c
                    l += 1
                if r & 1:
                    r -= 1
                    # Merge tree[r] and res_r
                    new_r_c = [0] * k
                    r_base = r * k
                    for j in range(k):
                        new_r_c[j] = tree_cnt[r_base + j]
                    r_p = tree_prod[r]
                    for j in range(k):
                        if res_r_c[j]:
                            new_r_c[(r_p * j) % k] += res_r_c[j]
                    res_r_p = (r_p * res_r_p) % k
                    res_r_c = new_r_c
                l >>= 1
                r >>= 1
            
            # Final merge of res_l and res_r
            final_ans = res_l_c[x_val]
            for j in range(k):
                if (res_l_p * j) % k == x_val:
                    final_ans += res_r_c[j]
            results.append(final_ans)
            
        return results
# @lc code=end