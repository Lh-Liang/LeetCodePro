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
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        prev = head
        curr = head.next
        index = 1
        first_critical = last_critical = -1
        min_distance = float('inf')
        critical_points = []
        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                if first_critical == -1:
                    first_critical = index
                else:
                    min_distance = min(min_distance, index - last_critical)
                last_critical = index
                critical_points.append(index)
            prev = curr
            curr = curr.next
            index += 1
        if len(critical_points) < 2:
            return [-1, -1]
        max_distance = critical_points[-1] - critical_points[0]
        return [min_distance, max_distance]
# @lc code=end