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
        if (!head || !head->next) return head;

        ListNode* curr = head;
        while (curr->next) {
            // Calculate GCD of current node and next node
            int gcdVal = std::gcd(curr->val, curr->next->val);
            
            // Create and insert the new node
            ListNode* newNode = new ListNode(gcdVal);
            newNode->next = curr->next;
            curr->next = newNode;
            
            // Move to the next original node
            curr = newNode->next;
        }
        
        return head;
    }
};
# @lc code=end