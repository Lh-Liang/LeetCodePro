class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        # Check if a matching path starts at the current root,
        # or if it exists starting from any node in the left or right subtrees.
        return self.checkPath(head, root) or \
               self.isSubPath(head, root.left) or \
               self.isSubPath(head, root.right)

    def checkPath(self, head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
        # If we have reached the end of the linked list, we found a match.
        if not head:
            return True
        # If the tree ends before the linked list is fully matched.
        if not node:
            return False
        # If the values do not match, this path is not a valid match.
        if head.val != node.val:
            return False
        # Continue searching for the next node in the list within the tree's children.
        return self.checkPath(head.next, node.left) or self.checkPath(head.next, node.right)
