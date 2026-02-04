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
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* curr = head;
        while (curr && curr->next) {
            int g = gcd(curr->val, curr->next->val);
            ListNode* newNode = new ListNode(g, curr->next);
            curr->next = newNode;
            // Verify connection: newNode should point to the original next node
            // Confirm inserted value matches GCD
            curr = newNode->next;
        }
        // Optionally, traverse the list here to ensure structure is correct
        return head;
    }
};
# @lc code=end