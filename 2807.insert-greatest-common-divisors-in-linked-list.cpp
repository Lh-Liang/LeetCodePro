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
    int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        
        ListNode* current = head;
        while (current->next) {
            int gcd_val = gcd(current->val, current->next->val);
            ListNode* newNode = new ListNode(gcd_val);
            
            newNode->next = current->next;
            current->next = newNode;
            
            current = newNode->next;
        }
        
        return head;
    }
};
# @lc code=end