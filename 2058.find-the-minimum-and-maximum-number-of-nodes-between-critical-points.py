#
# @lc app=leetcode id=2058 lang=python3
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
#

# @lc code=start
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        first_cp = None
        last_cp = None
        min_distance = float('inf')
        prev = head
        curr = head.next
        index = 1
        critical_points = []
        
        while curr.next:
            next_node = curr.next
            if (curr.val > prev.val and curr.val > next_node.val) or (curr.val < prev.val and curr.val < next_node.val):
                if first_cp is None:
                    first_cp = index
                if last_cp is not None:
                    min_distance = min(min_distance, index - last_cp)
                last_cp = index
                critical_points.append(index)
            prev = curr
            curr = next_node
            index += 1
        
        if len(critical_points) < 2:
            return [-1, -1]
        
        max_distance = critical_points[-1] - critical_points[0]
        return [min_distance, max_distance]
# @lc code=end