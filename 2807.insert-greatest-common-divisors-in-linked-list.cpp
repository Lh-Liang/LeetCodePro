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
class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        
        ListNode* current = head;
        
        while (current != nullptr && current->next != nullptr) {
            int gcdVal = __gcd(current->val, current->next->val);
            ListNode* newNode = new ListNode(gcdVal);
            newNode->next = current->next;
            current->next = newNode;
            current = newNode->next; // Move to the original next node
        }
        
        return head;
    }
};
# @lc code=end