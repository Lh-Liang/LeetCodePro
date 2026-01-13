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
        cur = head.next
        idx = 1  # 0-based index of cur

        first_cp = -1
        last_cp = -1
        prev_cp = -1
        min_dist = float('inf')

        while cur and cur.next:
            nxt = cur.next
            is_max = cur.val > prev.val and cur.val > nxt.val
            is_min = cur.val < prev.val and cur.val < nxt.val

            if is_max or is_min:
                if first_cp == -1:
                    first_cp = idx
                if prev_cp != -1:
                    min_dist = min(min_dist, idx - prev_cp)
                prev_cp = idx
                last_cp = idx

            prev = cur
            cur = nxt
            idx += 1

        if first_cp == -1 or first_cp == last_cp:
            return [-1, -1]

        return [min_dist, last_cp - first_cp]
# @lc code=end
