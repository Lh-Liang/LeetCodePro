#
# @lc app=leetcode id=3704 lang=python3
#
# [3704] Count No-Zero Pairs That Sum to N
#

# @lc code=start
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s = str(n)[::-1]
        L = len(s)
        memo = {}

        def solve(idx, carry, active_a, active_b):
            # active_a/b: True means we can still pick digits 1-9. 
            # False means this number has 'ended' and must contribute 0.
            state = (idx, carry, active_a, active_b)
            if state in memo: return memo[state]
            
            if idx == L + 1: # Check slightly beyond L to ensure carry is cleared
                return 1 if carry == 0 and not active_a and not active_b else 0
            
            target = int(s[idx]) if idx < L else 0
            res = 0
            
            # For each number, we pick a digit d. 
            # If active, d in [1..9]. We can also choose to 'deactivate' (d=0 for this and all future).
            # If already inactive, d must be 0.
            
            choices_a = [(d, True) for d in range(1, 10)] + [(0, False)] if active_a else [(0, False)]
            choices_b = [(d, True) for d in range(1, 10)] + [(0, False)] if active_b else [(0, False)]
            
            for da, next_a in choices_a:
                for db, next_b in choices_b:
                    if (da + db + carry) % 10 == target:
                        res += solve(idx + 1, (da + db + carry) // 10, next_a, next_b)
            
            memo[state] = res
            return res

        # a and b must be positive, so they must start with a digit in [1..9] at idx=0.
        # We force them to be active and iterate 1..9 for the first step to avoid a=0 or b=0.
        total = 0
        target0 = int(s[0])
        for da in range(1, 10):
            for db in range(1, 10):
                if (da + db) % 10 == target0:
                    total += solve(1, (da + db) // 10, True, True)
        return total
# @lc code=end