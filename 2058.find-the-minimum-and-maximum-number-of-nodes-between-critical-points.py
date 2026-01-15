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
        # Edge case: less than 3 nodes cannot have critical points
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        # Traverse linked list to find critical point indices
        critical_points = []
        prev = head
        curr = head.next
        next_node = head.next.next
        index = 1  # Current node's position (0-indexed would work too)
        
        while next_node:
            # Check if current node is critical
            if (curr.val > prev.val and curr.val > next_node.val) or \
               (curr.val < prev.val and curr.val < next_node.val):
                critical_points.append(index)
            
            # Move pointers forward
            prev = curr
            curr = next_node
            next_node = next_node.next
            index += 1
        
        # Check if we have at least two critical points
        if len(critical_points) < 2:
            return [-1, -1]
        
        # Calculate min and max distances
        min_dist = float('inf')
        max_dist = critical_points[-1] - critical_points[0]
        
        # Minimum distance is between consecutive critical points
        for i in range(1, len(critical_points)):
            diff = critical_points[i] - critical_points[i-1]
            min_dist = min(min_dist, diff)
        
        return [min_dist, max_dist]
# @lc code=end