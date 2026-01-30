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
        curr = head
        group_size = 1
        while curr:
            # Find the actual group size and the group's tail
            group_head = curr
            count = 0
            temp = curr
            for _ in range(group_size):
                if not temp:
                    break
                temp = temp.next
                count += 1
            group_tail = temp
            # If the group size is even, reverse the group
            if count % 2 == 0:
                prev_next = prev.next
                prev_sub = prev
                curr_sub = curr
                # Reverse 'count' nodes
                prev_node = group_tail
                for _ in range(count):
                    next_node = curr_sub.next
                    curr_sub.next = prev_node
                    prev_node = curr_sub
                    curr_sub = next_node
                prev.next = prev_node
                prev = prev_next
                curr = group_tail
            else:
                # Move prev and curr forward by 'count' nodes
                for _ in range(count):
                    prev = curr
                    curr = curr.next
            group_size += 1
        return dummy.next
# @lc code=end