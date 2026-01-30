#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)
        
        # Helper function to check if a minimum score is achievable
        def feasible(min_score: int) -> bool:
            # Calculate required visits for each index
            visits = [ (min_score + p - 1) // p for p in points ]
            total_visits = sum(visits)
            # Minimum moves needed:
            #  - Start at -1, must move to first visited index
            #  - Must traverse between indices for visits
            # The optimal is to visit indices in order, minimizing back-and-forth
            # The minimal path is: start at -1, go to first index, then traverse between visited indices, possibly visiting the same index multiple times.
            # Since we can increase or decrease index by 1 each move, visiting indices in order is optimal.
            # So, total moves = (first move to index 0) + (sum of all visits - 1) + (number of transitions between indices)
            # But actually, since we can distribute visits arbitrarily, the minimal number of moves required is: (total_visits - 1) + (last_index_visited + 1)
            # To minimize, we can assume we visit in order from 0 to n-1, so:
            # Start at -1, move to 0 (1 move), then distribute all visits: each visit is a move (except first, which is arrival), so total moves = total_visits + (n-1)
            # But we must consider that moves between non-consecutive indices cost more, but if we visit in order, it's minimal.
            # So, the minimal moves required = (total_visits - 1) + (last_index_visited + 1) if visiting in order.
            # Since we can only move to adjacent indices, the best is to visit indices in order, so moves = (sum(visits) - 1) + n
            # But each move increases/decreases index by 1, and every visit is a move, so total moves needed = (sum(visits) - 1) + n
            # Correction: For each visit, we need to move to that index, so total moves is at least sum(visits) + (n-1), as we need to traverse between indices.
            # Let's simulate visiting indices in order, starting from -1:
            moves = 0
            curr = -1
            for i in range(n):
                if visits[i] == 0:
                    continue
                moves += abs(i - curr) # move from current position to first needed index
                curr = i
                moves += visits[i] # all visits at this index
            # We need to make sure we do not exceed m moves
            return moves <= m
        
        left, right = 0, max(points) * m
        while left < right:
            mid = (left + right + 1) // 2
            if feasible(mid):
                left = mid
            else:
                right = mid - 1
        return left
# @lc code=end