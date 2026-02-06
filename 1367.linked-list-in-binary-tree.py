#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head: return True # An empty list is always a subpath
        if not root: return False # Non-empty list cannot be matched by an empty tree
        
        def doesPathMatch(head: ListNode, root: TreeNode) -> bool:
            if not head: return True # All nodes in the list are matched
            if not root or root.val != head.val: return False # Mismatch in value or end of path in tree reached without matching all nodes in list
            # Match head against root; recursively check both children paths with next of head
            return doesPathMatch(head.next, root.left) or doesPathMatch(head.next, root.right)
        
        # Perform DFS on each node along with checking if path matches starting from that node
        return doesPathMatch(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right) # Check all possible paths in the binary tree for match\# @lc code=end