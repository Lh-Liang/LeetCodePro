#
# @lc app=leetcode id=2074 lang=cpp
#
# [2074] Reverse Nodes in Even Length Groups
#

# @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        // Group 1 is always size 1 (odd), so we start processing from group 2.
        ListNode* prev = head;
        for (int len = 2; prev->next; len++) {
            ListNode* curr = prev->next;
            int count = 0;
            ListNode* temp = curr;
            
            // Count actual nodes in the current group
            while (temp && count < len) {
                temp = temp->next;
                count++;
            }
            
            if (count % 2 == 0) {
                // Reverse the even-length group
                ListNode* node = curr;
                ListNode* rev_prev = temp; // Reconnect tail of reversed group to next group head
                for (int i = 0; i < count; i++) {
                    ListNode* next_node = node->next;
                    node->next = rev_prev;
                    rev_prev = node;
                    node = next_node;
                }
                // Connect previous group to the new head of this reversed group
                prev->next = rev_prev;
                // The original 'curr' is now the end of this group
                prev = curr;
            } else {
                // Group length is odd, skip reversal
                for (int i = 0; i < count; i++) {
                    prev = prev->next;
                }
            }
        }
        return head;
    }
};
# @lc code=end