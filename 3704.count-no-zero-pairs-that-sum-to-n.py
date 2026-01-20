#
# @lc app=leetcode id=3704 lang=python3
#
# [3704] Count No-Zero Pairs That Sum to N
#

# @lc code=start
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s_n = str(n)[::-1]
        L = len(s_n)
        
        # Memoization dictionary
        memo = {}

        def dp(idx, carry, a_done, b_done):
            # Base case: processed all digits of n
            if idx == L:
                # Valid if no carry left, and both numbers have finished forming
                return 1 if carry == 0 and a_done and b_done else 0
            
            state = (idx, carry, a_done, b_done)
            if state in memo:
                return memo[state]
            
            res = 0
            target = int(s_n[idx])
            
            # Try both possible next_carry values (0 or 1)
            for next_carry in (0, 1):
                # We need: d_a + d_b + carry = target + 10 * next_carry
                # So: d_a + d_b = target + 10 * next_carry - carry
                S = target + 10 * next_carry - carry
                
                # Case 1: Both a and b have already finished
                if a_done and b_done:
                    # d_a = 0, d_b = 0 implies sum must be 0
                    if S == 0:
                        res += dp(idx + 1, next_carry, True, True)
                
                # Case 2: a finished, b still active
                elif a_done and not b_done:
                    # d_a = 0. We need d_b = S. d_b must be in [1, 9]
                    if 1 <= S <= 9:
                        # Option A: b finishes at this digit
                        res += dp(idx + 1, next_carry, True, True)
                        # Option B: b continues
                        res += dp(idx + 1, next_carry, True, False)
                
                # Case 3: b finished, a active
                elif not a_done and b_done:
                    # d_b = 0. We need d_a = S. d_a must be in [1, 9]
                    if 1 <= S <= 9:
                        # Option A: a finishes at this digit
                        res += dp(idx + 1, next_carry, True, True)
                        # Option B: a continues
                        res += dp(idx + 1, next_carry, False, True)
                
                # Case 4: Both active
                else:
                    # We need d_a + d_b = S where d_a, d_b in [1, 9]
                    # Count pairs (x, y) such that x + y = S, 1 <= x, y <= 9
                    # Range for x: max(1, S-9) <= x <= min(9, S-1)
                    low = max(1, S - 9)
                    high = min(9, S - 1)
                    
                    if low <= high:
                        count = high - low + 1
                        # For each valid pair, we have 4 branching possibilities for the "done" states
                        # 1. Both finish
                        w1 = dp(idx + 1, next_carry, True, True)
                        # 2. a finishes, b continues
                        w2 = dp(idx + 1, next_carry, True, False)
                        # 3. a continues, b finishes
                        w3 = dp(idx + 1, next_carry, False, True)
                        # 4. Both continue
                        w4 = dp(idx + 1, next_carry, False, False)
                        
                        res += count * (w1 + w2 + w3 + w4)
            
            memo[state] = res
            return res

        # Initial call: index 0, carry 0, neither a nor b finished
        # Since a, b must be positive, they can't be finished at start.
        return dp(0, 0, False, False)
# @lc code=end