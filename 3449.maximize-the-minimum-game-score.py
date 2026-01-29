class Solution:
    def maxScore(self, points: list[int], m: int) -> int:
        n = len(points)
        
        def check(X):
            if X == 0:
                return True
            
            moves_spent = 0
            # find the last index that actually needs to be reached to satisfy X
            # elements after last_idx only need to be visited if they don't reach X
            # during oscillations at earlier indices.
            last_idx = -1
            for i in range(n):
                if (X + points[i] - 1) // points[i] > 0:
                    last_idx = i
            
            if last_idx == -1: return True
            
            current_extra = 0
            total_moves = 0
            for i in range(last_idx + 1):
                # Move to index i
                total_moves += 1
                if total_moves > m: return False
                
                # Current score at i including previous visits
                # (Each oscillation i-1 <-> i adds points[i] once)
                # However, the standard greedy approach is to satisfy i 
                # by oscillating with i+1.
                needed = (X - 1) // points[i] + 1
                # We already have 1 visit from moving to i
                actual_needed = max(0, needed - 1 - current_extra)
                
                if i < last_idx:
                    # Oscillate between i and i+1
                    total_moves += 2 * actual_needed
                    current_extra = actual_needed
                else:
                    # At last_idx, we only care about satisfying last_idx
                    total_moves += 2 * actual_needed
                
                if total_moves > m: return False
            
            return total_moves <= m

        low, high = 0, 10**18
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans