#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
from typing import Optional, List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubPath(self, head: Optional['ListNode'], root: Optional['TreeNode']) -> bool:
        if not head:
            return True
        if not root:
            return False

        # Build pattern from linked list
        pat: List[int] = []
        cur = head
        while cur:
            pat.append(cur.val)
            cur = cur.next
        m = len(pat)

        # Build LPS (KMP failure function)
        lps = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pat[i] != pat[j]:
                j = lps[j - 1]
            if pat[i] == pat[j]:
                j += 1
                lps[i] = j

        # Iterative DFS with KMP state
        stack = [(root, 0)]  # (tree_node, matched_length)
        while stack:
            node, j = stack.pop()
            if not node:
                continue

            while j > 0 and node.val != pat[j]:
                j = lps[j - 1]
            if node.val == pat[j]:
                j += 1
                if j == m:
                    return True

            stack.append((node.left, j))
            stack.append((node.right, j))

        return False
# @lc code=end
