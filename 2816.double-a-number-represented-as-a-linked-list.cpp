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
        // If the head is >= 5, doubling it will create a carry to a new leading digit.
        if (head->val >= 5) {
            head = new ListNode(0, head);
        }
        
        ListNode* curr = head;
        while (curr != nullptr) {
            // Double the current value and keep the unit digit
            curr->val = (curr->val * 2) % 10;
            
            // Look ahead: if the next digit is >= 5, it will produce a carry of 1
            if (curr->next != nullptr && curr->next->val >= 5) {
                curr->val += 1;
            }
            
            curr = curr->next;
        }
        
        return head;
    }
};
# @lc code=end