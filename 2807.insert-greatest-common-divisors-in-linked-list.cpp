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
        // If the list is empty or has only one node, no adjacent pairs exist.
        if (!head || !head->next) {
            return head;
        }

        ListNode* curr = head;
        // Traverse the list as long as there is an adjacent pair.
        while (curr && curr->next) {
            // Calculate GCD of current node and the next node values.
            int gcdVal = std::gcd(curr->val, curr->next->val);
            
            // Create and insert the new GCD node.
            ListNode* newNode = new ListNode(gcdVal, curr->next);
            curr->next = newNode;
            
            // Jump to the original 'next' node, which is now two steps ahead.
            curr = newNode->next;
        }
        
        return head;
    }
};
# @lc code=end