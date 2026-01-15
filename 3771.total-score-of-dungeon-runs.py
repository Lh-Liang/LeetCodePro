#
# @lc app=leetcode id=3771 lang=python3
#
# [3771] Total Score of Dungeon Runs
#

# @lc code=start
class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        import bisect
        
        n = len(damage)
        
        # Compute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + damage[i]
        
        # V[j] = hp + prefix[j] (value for starting position j)
        # T[i] = requirement[i] + prefix[i + 1] (threshold for room i)
        V = [hp + prefix[j] for j in range(n)]
        T = [requirement[i] + prefix[i + 1] for i in range(n)]
        
        # Coordinate compression
        all_values = sorted(set(V + T))
        val_to_idx = {v: i + 1 for i, v in enumerate(all_values)}
        
        # Fenwick tree
        m = len(all_values)
        tree = [0] * (m + 1)
        
        def update(idx):
            while idx <= m:
                tree[idx] += 1
                idx += idx & (-idx)
        
        def query(idx):
            result = 0
            while idx > 0:
                result += tree[idx]
                idx -= idx & (-idx)
            return result
        
        total = 0
        for j in range(n - 1, -1, -1):
            # Insert T[j] first
            update(val_to_idx[T[j]])
            # Count T[i] values (for i >= j) that are <= V[j]
            pos = bisect.bisect_right(all_values, V[j])
            if pos > 0:
                total += query(pos)
        
        return total
# @lc code=end