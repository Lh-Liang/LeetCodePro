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
        if (!head || !head->next) return head;

        ListNode* curr = head;
        ListNode* prev = nullptr;
        int group_len = 1;

        while (curr != nullptr) {
            // Count the actual number of nodes available in the current group
            int count = 0;
            ListNode* temp = curr;
            while (count < group_len && temp != nullptr) {
                temp = temp->next;
                count++;
            }

            // If the actual length of the group is even, reverse it
            if (count % 2 == 0) {
                ListNode* rev_prev = temp; // The node after the current group
                ListNode* rev_curr = curr;
                for (int i = 0; i < count; ++i) {
                    ListNode* next_node = rev_curr->next;
                    rev_curr->next = rev_prev;
                    rev_prev = rev_curr;
                    rev_curr = next_node;
                }
                // Connect the previous group's tail to the new head of this group
                if (prev) prev->next = rev_prev;
                // After reversal, the original 'curr' becomes the tail of the group
                prev = curr;
                curr = temp;
            } else {
                // If the length is odd, skip the reversal and move pointers past the group
                for (int i = 0; i < count; ++i) {
                    prev = curr;
                    curr = curr->next;
                }
            }
            // Prepare for the next group with an incremented target length
            group_len++;
        }

        return head;
    }
};
# @lc code=end