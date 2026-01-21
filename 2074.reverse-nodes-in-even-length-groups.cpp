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
        
        ListNode* prev = head; // Node before the current group
        int groupSize = 2; // Start from group 2 (group 1 with size 1 is always odd)
        
        while (prev->next) {
            // Count actual nodes in this group
            ListNode* curr = prev->next;
            int count = 0;
            while (curr && count < groupSize) {
                count++;
                curr = curr->next;
            }
            
            // If actual count is even, reverse
            if (count % 2 == 0) {
                // Reverse 'count' nodes starting from prev->next
                ListNode* tail = prev->next; // This will become the tail after reversal
                ListNode* current = prev->next;
                ListNode* prevNode = nullptr;
                
                for (int i = 0; i < count; i++) {
                    ListNode* nextNode = current->next;
                    current->next = prevNode;
                    prevNode = current;
                    current = nextNode;
                }
                
                // prevNode is now the new head of reversed portion
                // current is the node after the reversed portion
                prev->next = prevNode;
                tail->next = current;
                prev = tail;
            } else {
                // Skip 'count' nodes
                for (int i = 0; i < count; i++) {
                    prev = prev->next;
                }
            }
            
            groupSize++;
        }
        
        return head;
    }
};
# @lc code=end