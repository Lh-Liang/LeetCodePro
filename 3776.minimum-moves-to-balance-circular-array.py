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
        
        # If the total sum is negative, it's impossible to balance the array.
        if total_sum < 0:
            return -1
        
        # Find the index with the negative balance.
        k = -1
        for i in range(n):
            if balance[i] < 0:
                k = i
                break
        
        # If no index is negative, no moves are needed.
        if k == -1:
            return 0
        
        X = -balance[k]
        ans = 0
        
        # Use a greedy approach by taking balance from the closest neighbors first.
        # Circular distance d goes from 1 up to n // 2.
        for d in range(1, n // 2 + 1):
            # Check index clockwise at distance d
            i1 = (k + d) % n
            if balance[i1] > 0:
                take = min(X, balance[i1])
                ans += take * d
                X -= take
                if X == 0:
                    return ans
            
            # Check index counter-clockwise at distance d
            i2 = (k - d) % n
            # Ensure we don't process the same index twice if n is even and d = n/2
            if i2 != i1 and balance[i2] > 0:
                take = min(X, balance[i2])
                ans += take * d
                X -= take
                if X == 0:
                    return ans
                    
        return ans
# @lc code=end