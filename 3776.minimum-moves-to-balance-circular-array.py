#
# @lc app=leetcode id=3776 lang=python3
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        total_sum = 0
        neg_index = -1
        
        # First pass: calculate sum and find the negative index
        for i, x in enumerate(balance):
            total_sum += x
            if x < 0:
                neg_index = i
        
        # If total balance is negative, impossible to balance
        if total_sum < 0:
            return -1
        
        # If no negative balance found, 0 moves needed
        if neg_index == -1:
            return 0
            
        deficit = -balance[neg_index]
        
        # Buckets to store total available balance at each distance
        # Max possible shortest distance in a circle is n // 2
        buckets = [0] * (n // 2 + 1)
        
        for i, x in enumerate(balance):
            if x > 0:
                # Calculate circular distance
                dist = abs(i - neg_index)
                shortest_dist = min(dist, n - dist)
                buckets[shortest_dist] += x
                
        moves = 0
        # Greedily take from the closest sources
        for d in range(1, len(buckets)):
            if buckets[d] > 0:
                take = min(buckets[d], deficit)
                moves += take * d
                deficit -= take
                if deficit == 0:
                    return moves
                    
        return moves
# @lc code=end