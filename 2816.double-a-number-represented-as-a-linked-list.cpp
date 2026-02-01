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
        // If the head's value is 5 or greater, the doubled value will have an extra digit.
        // We handle this by prepending a node with value 0.
        if (head->val > 4) {
            head = new ListNode(0, head);
        }

        ListNode* curr = head;
        while (curr != nullptr) {
            // Double the current value and keep only the last digit.
            curr->val = (curr->val * 2) % 10;

            // If the next node's original value is 5 or greater, it will produce a carry.
            // Since we haven't updated the next node yet, we can check its value directly.
            if (curr->next != nullptr && curr->next->val > 4) {
                curr->val++;
            }

            curr = curr->next;
        }

        return head;
    }
};
# @lc code=end