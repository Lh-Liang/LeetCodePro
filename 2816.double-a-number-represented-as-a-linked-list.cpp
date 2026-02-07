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
        if (!head) return nullptr; // Edge case handled but not needed per constraints
        int carry = 0; // Initialize carry to handle overflow
        ListNode *current = head; // Pointer to traverse the list
        while (current != nullptr) { // Traverse each node in the list
            int newVal = current->val * 2 + carry; // Double current value and add carry
            current->val = newVal % 10; // Update node value with last digit of newVal
            carry = newVal / 10; // Update carry for overflow
            if (current->next == nullptr && carry > 0) { // If at last node and have a carry
                current->next = new ListNode(carry); // Add new node for remaining carry
                break;
            }
            current = current->next; // Move to next node
        }
        return head; // Return modified list head
    }
}; 
# @lc code=end