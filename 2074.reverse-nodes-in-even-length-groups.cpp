//
// @lc app=leetcode id=2074 lang=cpp
//
// [2074] Reverse Nodes in Even Length Groups
//
// @lc code=start
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
        
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;
        
        int groupSize = 1;
        
        while (prev->next) {
            // Count actual nodes in this group
            int actualSize = 0;
            ListNode* curr = prev->next;
            while (curr && actualSize < groupSize) {
                actualSize++;
                curr = curr->next;
            }
            
            // If actual size is even, reverse this group
            if (actualSize % 2 == 0) {
                prev = reverseGroup(prev, actualSize);
            } else {
                // Move prev to the end of this group
                for (int i = 0; i < actualSize; i++) {
                    prev = prev->next;
                }
            }
            
            groupSize++;
        }
        
        return dummy->next;
    }
    
private:
    ListNode* reverseGroup(ListNode* prev, int size) {
        // prev is the node before the group to reverse
        // Returns the last node of the reversed group
        
        ListNode* groupTail = prev->next; // This will become the tail after reversal
        ListNode* curr = prev->next;
        ListNode* next = nullptr;
        
        // Reverse size nodes
        for (int i = 0; i < size; i++) {
            ListNode* temp = curr->next;
            curr->next = next;
            next = curr;
            curr = temp;
        }
        
        // Connect: prev -> reversed group -> rest
        prev->next = next; // Connect prev to new head of reversed group
        groupTail->next = curr; // Connect tail of reversed group to rest
        
        return groupTail; // Return the tail of the reversed group
    }
};
// @lc code=end