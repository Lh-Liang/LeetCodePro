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
        n = len(vals)
        
        # Step 2: Build the tree using adjacency list representation
        tree = defaultdict(list)
        for child, parent in enumerate(par):
            if parent != -1:
                tree[parent].append(child)

        # Step 5: Helper function to check if digits in numbers are unique across a subset
        def has_unique_digits(subset_vals):
            digit_set = set()
            for val in subset_vals:
                digits = set(str(val))
                if digit_set & digits:
                    return False
                digit_set.update(digits)
            return True

        # Step 4 & Step 6: DFS function to compute maxScore for each subtree rooted at node u
        def dfs(node):
            current_subtree_vals = [vals[node]]
            max_sum = vals[node]
            for child in tree[node]:
                child_sum, child_vals = dfs(child)
                current_subtree_vals += child_vals
                max_sum = max(max_sum, child_sum)
            
            # Check if all nodes in current subtree form a good subset and calculate their score
            if has_unique_digits(current_subtree_vals):
                max_sum = sum(current_subtree_vals)
            
            return max_sum, current_subtree_vals
        
        # Calculate maxScore for subtree rooted at each node and sum them up for final result
        total_max_score = dfs(0)[0] % MOD
        return total_max_score
# @lc code=end