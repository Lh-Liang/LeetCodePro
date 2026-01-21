#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)
        
        def check(target):
            if target == 0:
                return True
            
            moves_used = 0
            v = [0] * n
            needed = [(target + p - 1) // p for p in points]
            
            for i in range(n):
                # Move from i-1 to i
                moves_used += 1
                v[i] += 1
                
                if moves_used > m:
                    return False
                
                # Satisfy index i if needed
                if v[i] < needed[i]:
                    k = needed[i] - v[i]
                    moves_used += 2 * k
                    v[i] += k
                    if i < n - 1:
                        v[i+1] += k
                
                if moves_used > m:
                    return False
                
                # Check if we can stop here: i must be the last element to satisfy
                # or i is n-2 and n-1 is already satisfied.
                if i == n - 1:
                    return True
                if i == n - 2 and v[n-1] >= needed[n-1]:
                    return True
            
            return False

        low = 0
        high = 10**15 # Max possible m * max points
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
# @lc code=end