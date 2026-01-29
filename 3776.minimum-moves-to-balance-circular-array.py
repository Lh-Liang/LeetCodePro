#
# @lc app=leetcode id=3776 lang=python3
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        total_sum = sum(balance)
        
        # If total balance is negative, it's impossible to make all non-negative
        if total_sum < 0:
            return -1
        
        # Find the index of the negative balance (the 'sink')
        sink_idx = -1
        for i in range(n):
            if balance[i] < 0:
                sink_idx = i
                break
        
        # If no negative balance exists, 0 moves are needed
        if sink_idx == -1:
            return 0
        
        deficit = -balance[sink_idx]
        sources = []
        
        # Identify all potential sources and their circular distance to the sink
        for i in range(n):
            if balance[i] > 0:
                # Circular distance formula
                diff = abs(i - sink_idx)
                dist = min(diff, n - diff)
                sources.append((dist, balance[i]))
        
        # Greedy: Sort sources by distance to pull from the closest ones first
        sources.sort(key=lambda x: x[0])
        
        total_moves = 0
        remaining_deficit = deficit
        
        for dist, available in sources:
            if remaining_deficit <= 0:
                break
            
            take = min(remaining_deficit, available)
            total_moves += take * dist
            remaining_deficit -= take
            
        return total_moves
# @lc code=end