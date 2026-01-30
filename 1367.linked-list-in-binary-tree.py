#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(tree_node, list_node):
            if not list_node: return True
            if not tree_node: return False
            if tree_node.val == list_node.val:
                return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)
            return False
        
        def traverse_tree(node):
            if not node: return False
            return (dfs(node, head) or 
                    traverse_tree(node.left) or 
                    traverse_tree(node.right))
        
        return traverse_tree(root)
# @lc code=end