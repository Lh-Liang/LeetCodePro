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
#include <numeric>

class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        // If the list is empty or has only one node, no pairs exist.
        if (!head || !head->next) {
            return head;
        }

        ListNode* curr = head;
        
        // Iterate through the list while there is a pair of nodes.
        while (curr && curr->next) {
            // Calculate GCD of current node and next node values.
            int commonDivisor = std::gcd(curr->val, curr->next->val);
            
            // Create a new node with the GCD value.
            // Link it to the current next node.
            ListNode* newNode = new ListNode(commonDivisor, curr->next);
            
            // Insert the new node after the current node.
            curr->next = newNode;
            
            // Move curr to the original next node (skip the inserted node).
            curr = newNode->next;
        }
        
        return head;
    }
};
# @lc code=end