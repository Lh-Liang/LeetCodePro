#
# @lc app=leetcode id=3776 lang=python3
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        
        # Find the index of the negative balance (if any)
        neg_idx = -1
        for i in range(n):
            if balance[i] < 0:
                neg_idx = i
                break
        
        # If no negative balance, all are already non-negative
        if neg_idx == -1:
            return 0
        
        # Check if the total sum is non-negative
        total = sum(balance)
        if total < 0:
            return -1
        
        # Calculate the deficit that needs to be covered
        deficit = -balance[neg_idx]
        
        # Compute distances and balances for all other positions
        positions = []
        for i in range(n):
            if i != neg_idx:
                # Calculate circular distance
                dist = min((neg_idx - i) % n, (i - neg_idx) % n)
                positions.append((dist, balance[i]))
        
        # Sort positions by distance (closer positions first)
        positions.sort()
        
        # Greedily take from closest positions first
        cost = 0
        remaining = deficit
        for dist, bal in positions:
            take = min(bal, remaining)
            cost += dist * take
            remaining -= take
            if remaining == 0:
                break
        
        return cost
# @lc code=end