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
        // If the leading digit is >= 5, doubling it will create a new digit '1' at the front.
        if (head->val > 4) {
            head = new ListNode(0, head);
        }
        
        ListNode* curr = head;
        while (curr != nullptr) {
            // The current node's value becomes (val * 2) % 10.
            // We look ahead to the next node to see if it will produce a carry.
            int newValue = (curr->val * 2) % 10;
            
            if (curr->next != nullptr && curr->next->val > 4) {
                newValue += 1;
            }
            
            curr->val = newValue;
            curr = curr->next;
        }
        
        return head;
    }
};
# @lc code=end