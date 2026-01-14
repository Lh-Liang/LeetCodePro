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
        critical_points = []
        
        prev = head
        curr = head.next
        index = 1
        
        while curr and curr.next:
            next_node = curr.next
            # Check if current is a local maxima or minima
            if (curr.val > prev.val and curr.val > next_node.val) or \
               (curr.val < prev.val and curr.val < next_node.val):
                critical_points.append(index)
            
            prev = curr
            curr = next_node
            index += 1
        
        if len(critical_points) < 2:
            return [-1, -1]
        
        # Max distance is between first and last critical point
        max_distance = critical_points[-1] - critical_points[0]
        
        # Min distance is minimum of differences between consecutive critical points
        min_distance = float('inf')
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i-1])
        
        return [min_distance, max_distance]
# @lc code=end