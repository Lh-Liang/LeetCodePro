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
        // If the list has 0 or 1 nodes, no GCD can be inserted between pairs.
        if (!head || !head->next) {
            return head;
        }

        ListNode* curr = head;

        // Traverse until the second to last node.
        while (curr != nullptr && curr->next != nullptr) {
            // Calculate GCD of the current node and the next node.
            int commonDivisor = std::gcd(curr->val, curr->next->val);

            // Create the new node and insert it between curr and curr->next.
            ListNode* newNode = new ListNode(commonDivisor, curr->next);
            curr->next = newNode;

            // Skip the newly inserted node to move to the next original pair.
            curr = newNode->next;
        }

        return head;
    }
};
# @lc code=end