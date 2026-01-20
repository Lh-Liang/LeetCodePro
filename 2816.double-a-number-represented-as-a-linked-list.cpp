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
        // If the head is greater than 4, doubling it will result in a carry
        // that creates a new most significant digit.
        if (head->val > 4) {
            head = new ListNode(0, head);
        }

        ListNode* curr = head;
        while (curr != nullptr) {
            // Double the current value modulo 10
            curr->val = (curr->val * 2) % 10;

            // If the next digit is > 4, it will produce a carry when doubled,
            // so we add 1 to the current digit.
            if (curr->next != nullptr && curr->next->val > 4) {
                curr->val += 1;
            }

            curr = curr->next;
        }

        return head;
    }
};
# @lc code=end