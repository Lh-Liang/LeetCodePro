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
#include <numeric> // for std::gcd

class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        
        ListNode* curr = head;
        while (curr != nullptr && curr->next != nullptr) {
            int val1 = curr->val;
            int val2 = curr->next->val;
            
            // Calculate GCD
            int gcdVal = std::gcd(val1, val2);
            
            // Create new node
            ListNode* newNode = new ListNode(gcdVal);
            
            // Insert node
            newNode->next = curr->next;
            curr->next = newNode;
            
            // Move to the next pair (skip the node we just inserted)
            curr = newNode->next;
        }
        
        return head;
    }
};
# @lc code=end