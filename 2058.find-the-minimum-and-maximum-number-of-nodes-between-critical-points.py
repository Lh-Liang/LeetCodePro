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
        first_cp = last_cp = -1
        min_dist = float('inf')
        index = 1
        prev, curr, next_node = head, head.next, head.next.next
        critical_points = []
        while next_node:
            if (curr.val > prev.val and curr.val > next_node.val) or (curr.val < prev.val and curr.val < next_node.val):
                if first_cp == -1:
                    first_cp = index
                else:
                    min_dist = min(min_dist, index - last_cp)
                last_cp = index
                critical_points.append(index)
            prev, curr = curr, next_node
            next_node = next_node.next
            index += 1
        if len(critical_points) < 2:
            return [-1, -1]
        max_dist = critical_points[-1] - critical_points[0]
        return [min_dist, max_dist]
# @lc code=end