#
# @lc app=leetcode id=2074 lang=python3
#
# [2074] Reverse Nodes in Even Length Groups
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        gsize = 1
        while prev.next:
            start = prev.next
            curr = start
            length = 0
            for _ in range(gsize):
                if curr is None:
                    break
                length += 1
                curr = curr.next
            group_end = start
            for _ in range(1, length):
                group_end = group_end.next
            next_start = group_end.next
            if length % 2 == 0:
                # reverse start to group_end
                prevv = None
                cur = start
                for _ in range(length):
                    nxt = cur.next
                    cur.next = prevv
                    prevv = cur
                    cur = nxt
                prev.next = prevv
                start.next = next_start  # start is now tail
                prev = start
            else:
                prev = group_end
            gsize += 1
        return dummy.next

# @lc code=end