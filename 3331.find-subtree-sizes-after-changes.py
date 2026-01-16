#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        
        # Build initial children list
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        
        # New parent array after changes
        new_parent = parent[:]
        
        # For each character, keep track of the path from root
        char_to_path = {}
        
        def dfs(node):
            char = s[node]
            
            # Save the previous state for this character
            prev_path = char_to_path.get(char, [])
            
            # Update the path for this character
            char_to_path[char] = prev_path + [node]
            
            # Process all children
            for child in children[node]:
                # Find the closest ancestor with same character
                if len(char_to_path[char]) >= 2:  # At least one ancestor other than itself
                    # The closest one is the last one in the path except current node
                    new_parent[child] = char_to_path[char][-2]
                dfs(child)
            
            # Restore the path for this character (backtrack)
            char_to_path[char] = prev_path
        
        # Start DFS from root (node 0)
        dfs(0)
        
        # Build new children list based on new_parent
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)
        
        # Calculate subtree sizes
        answer = [0] * n
        
        def calculate_size(node):
            size = 1  # Count the node itself
            for child in new_children[node]:
                size += calculate_size(child)
            answer[node] = size
            return size
        
        calculate_size(0)
        
        return answer
# @lc code=end