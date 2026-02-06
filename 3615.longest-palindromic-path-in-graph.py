#
# @lc app=leetcode id=3615 lang=python3
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        from collections import defaultdict, Counter
        
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def can_form_palindrome(counter):
            # A string can be rearranged as a palindrome if at most one character has an odd count
            odd_count = sum(1 for freq in counter.values() if freq % 2 != 0)
            return odd_count <= 1
        
        def dfs(node, visited, counter):
            max_len = 0
            counter[label[node]] += 1
            
            if can_form_palindrome(counter):
                max_len = len(visited) + 1 # +1 because current node is included as well
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    max_len = max(max_len, dfs(neighbor, visited, counter))
                    visited.remove(neighbor) # Backtrack
            
            counter[label[node]] -= 1 # Backtrack character count
            return max_len
        
        longest_path = 0
        for start_node in range(n):
            longest_path = max(longest_path, dfs(start_node, set([start_node]), Counter()))
        return longest_path
# @lc code=end