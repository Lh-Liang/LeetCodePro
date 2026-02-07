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
        // Reverse the linked list first.
        head = reverseList(head);
        
        // Traverse reversed list, double each node's value, and manage carry.
        ListNode *cur = head;
        int carry = 0;
        while (cur != nullptr) {
            int newVal = cur->val * 2 + carry; // Double current node's value and add carry from previous operation.
            cur->val = newVal % 10; // Set current node's value to remainder of division by 10.
            carry = newVal / 10; // Update carry for next node.
            if (cur->next == nullptr && carry > 0) { // If at last node and there's a remaining carry. Add new node if needed. 
                cur->next = new ListNode(carry); 
                break; 	// Break since we handled extra digit.	 			 } 	 cur = cur->next; } 			// Reverse back to restore original order after processing. return reverseList(head); } private: ListNode* reverseList(ListNode* head) { if (!head || !head->next) return head; 				ListNode *prev = nullptr, *curr = head, *next = nullptr; while (curr != nullptr) { next = curr->next; curr->next = prev; prev = curr; curr = next;} return prev;} }; # @lc code=end