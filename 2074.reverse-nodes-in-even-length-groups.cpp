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
        if (!head || !head->next) return head; // Early return for trivial cases
        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;
        int groupSize = 1;
        while (prev->next) {
            ListNode* start = prev->next;
            ListNode* end = start;
            int count = 0;
            // Determine the length of the current group
            while (end && count < groupSize) {
                end = end->next;
                count++;
            }
            // Reverse nodes if the group size is even
            if (count % 2 == 0) {
                ListNode* current = start->next;
                ListNode* tail = start; 
                tail->next = end; 
                // Perform reversal within the current group
                while (current != end) {
                    ListNode* temp = current->next;
                    current->next = prev->next;
                    prev->next = current;
                    current = temp;
                }
            } else {
                prev = start; // Move prev only if no reversal occurs
            }
            groupSize++; // Increment expected group size for next iteration
        }
        return dummy.next; // Return new head after all operations
    }
};
# @lc code=end