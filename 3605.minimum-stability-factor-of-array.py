#
# @lc app=leetcode id=3605 lang=python3
#
# [3605] Minimum Stability Factor of Array
#

# @lc code=start
import math

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        # Local reference for speed
        gcd = math.gcd
        
        def check(K):
            # We want to ensure no stable subarray of length > K exists.
            # This is equivalent to breaking all stable subarrays of length L = K + 1.
            L = K + 1
            if L > n:
                return True
            
            # Two-stack queue to maintain sliding window GCD
            # stack_in stores (value, accumulated_gcd_from_bottom)
            stack_in = []
            # stack_out stores (value, accumulated_gcd_from_bottom)
            stack_out = []
            
            cost = 0
            current_len = 0
            
            for x in nums:
                # Push x into stack_in
                if not stack_in:
                    stack_in.append((x, x))
                else:
                    stack_in.append((x, gcd(x, stack_in[-1][1])))
                current_len += 1
                
                if current_len == L:
                    # Query the GCD of the current window
                    g = 0
                    if stack_in:
                        g = stack_in[-1][1]
                    if stack_out:
                        if g == 0:
                            g = stack_out[-1][1]
                        else:
                            g = gcd(g, stack_out[-1][1])
                    
                    if g >= 2:
                        # Found a stable subarray of length L
                        cost += 1
                        if cost > maxC:
                            return False
                        # Greedy strategy: modify the last element (current x) to break this window.
                        # This modification effectively invalidates the current window and allows us
                        # to skip overlapping windows starting within this range. 
                        # We reset the queue to simulate this skip.
                        stack_in.clear()
                        stack_out.clear()
                        current_len = 0
                    else:
                        # Window is not stable, slide forward by popping the oldest element
                        if not stack_out:
                            # Move elements from stack_in to stack_out
                            if stack_in:
                                val, _ = stack_in.pop()
                                stack_out.append((val, val))
                                while stack_in:
                                    val, _ = stack_in.pop()
                                    stack_out.append((val, gcd(val, stack_out[-1][1])))
                        if stack_out:
                            stack_out.pop()
                        current_len -= 1
            
            return True

        low, high = 0, n
        ans = n
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
# @lc code=end