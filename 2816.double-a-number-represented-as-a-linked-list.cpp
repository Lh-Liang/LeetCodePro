#
# @lc app=leetcode id=2816 lang=cpp
#
# [2816] Double a Number Represented as a Linked List
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
    ListNode* doubleIt(ListNode* head) {
        int carry = 0; // Initialize carry to zero for any overflow during doubling
        ListNode* current = head; // Start at head of linked list
        while (current != nullptr) { // Traverse each node in list
            int newVal = current->val * 2 + carry; // Double current value and add carry
            current->val = newVal % 10; // Update current node with the single digit result
            carry = newVal / 10; // Calculate new carry for next iteration if any overflow occurred
            if (!current->next && carry > 0) { // If at end, check if an extra node is needed for remaining carry
                current->next = new ListNode(carry); // Append new node with remaining carry value
                break; 
            }
            current = current->next; // Move to next node in list for further processing
        }
        return head; // Return modified list representing doubled number
    }
};
# @lc code=end