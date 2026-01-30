#
# @lc app=leetcode id=2058 lang=python3
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        indices = []
        prev = head
        curr = head.next
        idx = 1
        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                indices.append(idx)
            prev = curr
            curr = curr.next
            idx += 1
        if len(indices) < 2:
            return [-1, -1]
        min_dist = min(indices[i+1] - indices[i] for i in range(len(indices)-1))
        max_dist = indices[-1] - indices[0]
        return [min_dist, max_dist]
# @lc code=end