#
# @lc app=leetcode id=2816 lang=cpp
#
# [2816] Double a Number Represented as a Linked List
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
    ListNode* doubleIt(ListNode* head) {
        // If the first digit >= 5, when doubled it becomes >= 10, so need a new head
        if (head->val >= 5) {
            head = new ListNode(0, head);
        }
        
        ListNode* curr = head;
        while (curr) {
            // Double current value and take mod 10
            curr->val = (curr->val * 2) % 10;
            // If next node's value >= 5, it will generate a carry when doubled
            if (curr->next && curr->next->val >= 5) {
                curr->val += 1;
            }
            curr = curr->next;
        }
        
        return head;
    }
};
# @lc code=end