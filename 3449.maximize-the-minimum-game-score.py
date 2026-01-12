#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)

        def check(X):
            if X == 0:
                return True
            
            needed = [(X + p - 1) // p for p in points]
            v = [0] * n
            total_m = 0
            last_undone = n - 1
            
            # Initialize last_undone to the last index that needs more visits
            while last_undone >= 0 and v[last_undone] >= needed[last_undone]:
                last_undone -= 1
            
            for i in range(n):
                # Move from i-1 to i
                total_m += 1
                if total_m > m:
                    return False
                v[i] += 1
                
                # If current index needs more visits, do round trips with next index
                if v[i] < needed[i]:
                    rem = needed[i] - v[i]
                    if i < n - 1:
                        v[i] += rem
                        v[i + 1] += rem
                        total_m += 2 * rem
                    else:
                        # Last element, must go back to n-2 and return to n-1
                        v[i] += rem
                        total_m += 2 * rem
                    
                    if total_m > m:
                        return False
                
                # Update the last_undone pointer
                while last_undone >= 0 and v[last_undone] >= needed[last_undone]:
                    last_undone -= 1
                
                # If all indices are satisfied, we can stop here
                if last_undone < 0:
                    return total_m <= m
            
            return False

        low = 0
        high = 10**15 # Safe upper bound based on constraints
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