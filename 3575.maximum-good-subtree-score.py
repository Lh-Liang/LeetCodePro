#
# @lc app=leetcode id=3575 lang=python3
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        from collections import defaultdict
        MOD = 10**9 + 7
        # Build tree from parent array
        tree = defaultdict(list)
        n = len(vals)
        for i in range(1, n):
            tree[par[i]].append(i)
        
        # Helper function to get digits as a set from a number
        def get_digits(num):
            return set(str(num))
        
        # DFS function to calculate maximum good subtree score
        def dfs(node):
            current_digits = get_digits(vals[node])
            current_score = vals[node]
            for child in tree[node]:
                child_score, child_digits = dfs(child)
                if not current_digits & child_digits: # If no common digits
                    current_score += child_score
                    current_digits |= child_digits # Union of digits sets if valid
            return current_score, current_digits
        
        # Calculate maxScore for each node starting from root (0) and sum it up
        total_sum = 0
        for i in range(n): # Calculate maxScore for each subtree rooted at i
            score, _ = dfs(i)
            total_sum += score % MOD # Sum up scores with modulo operation
total_sum %= MOD # Final mod operation after summing up all scores
return total_sum

# @lc code=end