#
# @lc app=leetcode id=3534 lang=python3
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        if not nums:
            return []

        # 1. Map values to unique sorted positions
        unique_nums = sorted(list(set(nums)))
        m = len(unique_nums)
        val_to_idx = {v: i for i, v in enumerate(unique_nums)}
        node_to_pos = [val_to_idx[num] for num in nums]

        # 2. Pre-calculate components (connectivity check)
        comp = [0] * m
        curr_comp = 0
        for i in range(1, m):
            if unique_nums[i] - unique_nums[i-1] > maxDiff:
                curr_comp += 1
            comp[i] = curr_comp

        # 3. Build Binary Lifting table for greedy jumping
        # next_idx[i] = max index reachable from i in 1 jump
        next_idx = [0] * m
        r = 0
        for l in range(m):
            while r + 1 < m and unique_nums[r + 1] <= unique_nums[l] + maxDiff:
                r += 1
            next_idx[l] = r

        # Sparse table: up[k][i] is the index reached from i after 2^k jumps
        LOG = m.bit_length()
        up = [next_idx]
        for k in range(1, LOG):
            prev = up[-1]
            # Efficiency: use a local reference for the previous jump level
            curr_level = [prev[prev[i]] for i in range(m)]
            up.append(curr_level)

        ans = []
        for ui, vi in queries:
            if ui == vi:
                ans.append(0)
                continue
            
            u_pos, v_pos = node_to_pos[ui], node_to_pos[vi]
            if u_pos == v_pos:
                # Distinct nodes, same value: distance is 1 step
                ans.append(1)
                continue
            
            # Normalize: start is always the smaller index
            start, target = (u_pos, v_pos) if u_pos < v_pos else (v_pos, u_pos)
            
            if comp[start] != comp[target]:
                ans.append(-1)
                continue
            
            # Binary lifting to find min steps
            steps = 0
            curr = start
            for k in range(LOG - 1, -1, -1):
                if up[k][curr] < target:
                    curr = up[k][curr]
                    steps += (1 << k)
            
            # One final jump to reach or exceed target
            ans.append(steps + 1)
            
        return ans
# @lc code=end