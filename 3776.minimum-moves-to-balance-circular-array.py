#
# @lc app=leetcode id=3776 lang=python3
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
class Solution:
    def minMoves(self, balance: List[int]) -> int:
        # Step 1: Check for impossibility
        total = sum(balance)
        if total < 0:
            return -1
        if min(balance) >= 0:
            return 0
        n = len(balance)
        # Step 2: Find the index with negative balance
        neg_idx = next((i for i, v in enumerate(balance) if v < 0), -1)
        need = -balance[neg_idx]
        # Step 3: Simulate the movement chain according to adjacency constraints
        temp = balance[:]
        moves = 0
        left = (neg_idx - 1) % n
        right = (neg_idx + 1) % n
        left_steps = 1
        right_steps = 1
        while need > 0:
            # Find which side can provide a positive unit, in order of increasing distance
            l_idx = (neg_idx - left_steps) % n
            r_idx = (neg_idx + right_steps) % n
            l_val = temp[l_idx] if left_steps < n else 0
            r_val = temp[r_idx] if right_steps < n else 0
            # Choose the closer available positive unit
            if (l_val > 0 and (l_val >= r_val or r_val <= 0)) or (r_val <= 0):
                take = min(l_val, need)
                moves += take * left_steps
                temp[l_idx] -= take
                need -= take
                left_steps += 1
            elif r_val > 0:
                take = min(r_val, need)
                moves += take * right_steps
                temp[r_idx] -= take
                need -= take
                right_steps += 1
            else:
                # No more positive balances to use
                break
        if need > 0:
            return -1
        return moves
# @lc code=end