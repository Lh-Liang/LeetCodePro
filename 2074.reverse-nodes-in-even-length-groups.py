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
    def reverseEvenLengthGroups(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev_tail = dummy
        cur = head
        k = 1
        
        while cur:
            # Determine boundaries of current k-group
            cnt = 0
            start = cur
            last_in_group = None
            
            # Traverse k nodes or until end
            while cur and cnt < k:
                cnt += 1
                last_in_group = cur
                cur = cur.next
            
            # cur now points to first node of next group
            
            if cnt % 2 == 0:
                # Reverse sublist from start up through last_in_group
                rev_prev = None
                rev_cur = start
                stop_node = cur
                
                while rev_cur != stop_node:
                    nxt_temp = rev_cur.next
                    rev_cur.next = rev_prev
                    rev_prev = rev_cur
                    rev_cur = nxt_temp
                
                # rev_prev now heads reversed segment
                # Connect previous part
                prev_tail.next = rev_prev
                # Connect reversed segment's tail (original start) onward
                start.next = cur
                
                # Update tracking variables
                prev_tail = start
            else:
                # No reversal needed
                # Simply move tracking variables forward
                # Note: connections remain intact
                
                # Update previous tail tracker directly using recorded last_in_group
                # Since no reversal occurred,
                # The existing chain already connects properly.
                
                # Move tracker forward along existing chain.
                # But careful not alter chain structure accidentally.
                
                # Advance tracker location accordingly.
                
                # Optionally could compute via walking forward,
                # But easier simply assign recorded value!
                
                # However ensure proper linking already established.
                
                # Since nothing changed structurally,
                # Simply assign tracker variable.
                
                
                
                
                
                
                
                
                
# @lc code=end