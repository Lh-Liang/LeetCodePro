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
#include <algorithm> // For std::gcd function
class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if (!head || !head->next) return head; // Check if list has fewer than two nodes; return early as no GCD insertion is possible.
        ListNode* current = head;
        while (current && current->next) {
            int gcdValue = std::gcd(current->val, current->next->val); // Compute GCD of current pair of nodes' values.
            ListNode* gcdNode = new ListNode(gcdValue); // Create a new node with this GCD value.
            gcdNode->next = current->next; // Link new node to next node.
            current->next = gcdNode; // Insert new node after current node.
            current = gcdNode->next; // Move to the next pair of nodes, skipping over newly inserted node.
        }
        return head; // Return modified list starting from head after all insertions.
    }
};
# @lc code=end