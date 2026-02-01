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
    int getGCD(int a, int b) {
        while (b) {
            a %= b;
            int temp = a;
            a = b;
            b = temp;
        }
        return a;
    }

    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if (!head || !head->next) return head;

        ListNode* curr = head;
        while (curr->next) {
            int gcdVal = getGCD(curr->val, curr->next->val);
            ListNode* newNode = new ListNode(gcdVal, curr->next);
            curr->next = newNode;
            curr = newNode->next;
        }
        return head;
    }
};
# @lc code=end