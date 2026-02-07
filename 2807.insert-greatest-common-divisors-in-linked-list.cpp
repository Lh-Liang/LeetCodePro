#
# @lc app=leetcode id=2807 lang=cpp
#
# [2807] Insert Greatest Common Divisors in Linked List
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
#include <algorithm> // for std::gcd
class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if (!head || !head->next) return head; // Edge case: 0 or 1 node, return as is.
        ListNode* current = head;
        while (current && current->next) {
            int gcdValue = std::gcd(current->val, current->next->val); // Compute GCD of current and next node's values.
            ListNode* newNode = new ListNode(gcdValue); // Create new node with GCD value.
            newNode->next = current->next; // Link new node to current's next node.
            current->next = newNode; // Link current's next to new node.
            current = newNode->next; // Move to next pair of nodes by skipping over inserted node.
        }
        return head; // Return modified list.
    }
};
# @lc code=end