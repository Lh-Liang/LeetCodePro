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

from typing import List, Optional

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next:
            return [-1, -1]
        critical_points = []
        prev = head
        curr = head.next
        index = 2
        while curr.next:
            nxt = curr.next
            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):
                critical_points.append(index)
            prev = curr
            curr = nxt
            index += 1
        if len(critical_points) < 2:
            return [-1, -1]
        min_distance = min(critical_points[i+1] - critical_points[i] for i in range(len(critical_points)-1))
        max_distance = critical_points[-1] - critical_points[0]
        return [min_distance, max_distance]
# @lc code=end