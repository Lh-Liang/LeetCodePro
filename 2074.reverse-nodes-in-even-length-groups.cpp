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

        // The first group (size 1) is always odd, so we start with prev at head.
        ListNode* prev = head;
        int expected_group_size = 2;

        while (prev->next) {
            ListNode* curr = prev->next;
            int actual_count = 0;

            // Count nodes available for the current group
            while (actual_count < expected_group_size && curr) {
                actual_count++;
                curr = curr->next;
            }

            if (actual_count % 2 == 0) {
                // Reverse the group of actual_count nodes
                ListNode* group_start = prev->next;
                ListNode* node = group_start;
                ListNode* p = curr; // Node after the group

                for (int i = 0; i < actual_count; ++i) {
                    ListNode* next_temp = node->next;
                    node->next = p;
                    p = node;
                    node = next_temp;
                }

                // Reconnect previous node to the new head of reversed group
                prev->next = p;
                // Move prev to the end of the reversed group (the original start)
                prev = group_start;
            } else {
                // Skip the odd-length group
                for (int i = 0; i < actual_count; ++i) {
                    prev = prev->next;
                }
            }

            expected_group_size++;
        }

        return head;
    }
};
# @lc code=end