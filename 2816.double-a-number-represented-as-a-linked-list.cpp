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
        // Step 1: Reverse list (LSD now at head)
        ListNode *prev = nullptr, *curr = head;
        while (curr != nullptr) {
            ListNode *next_node = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_node;
        }
        ListNode *l1 = prev;

        // Step 2: Double from LSD, propagate carry
        int carry = 0;
        ListNode *tail = nullptr;
        curr = l1;
        while (curr != nullptr) {
            int temp = curr->val * 2 + carry;
            curr->val = temp % 10;
            carry = temp / 10;
            tail = curr;
            curr = curr->next;
        }

        // Step 3: Append new node if carry remains
        if (carry != 0) {
            ListNode *new_node = new ListNode(carry);
            tail->next = new_node;
        }

        // Step 4: Reverse back (MSD now at head)
        prev = nullptr;
        curr = l1;
        while (curr != nullptr) {
            ListNode *next_node = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_node;
        }

        return prev;
    }
};
# @lc code=end