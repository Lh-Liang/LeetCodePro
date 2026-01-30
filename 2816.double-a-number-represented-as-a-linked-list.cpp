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
        // If the head's value is 5 or more, doubling it will result in a carry
        // that creates a new most-significant digit.
        if (head->val >= 5) {
            head = new ListNode(0, head);
        }

        ListNode* curr = head;
        while (curr != nullptr) {
            // Update current node: double it and take modulo 10.
            curr->val = (curr->val * 2) % 10;

            // Look ahead to the next node. If it will produce a carry (val >= 5),
            // increment the current node.
            if (curr->next != nullptr && curr->next->val >= 5) {
                curr->val += 1;
            }

            curr = curr->next;
        }

        return head;
    }
};
# @lc code=end