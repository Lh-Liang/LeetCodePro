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
        // If the head will result in a carry, prepend a dummy node
        if (head->val >= 5) {
            head = new ListNode(0, head);
        }
        
        ListNode* curr = head;
        while (curr != nullptr) {
            // Double the current digit and handle carry-out from the next node
            int newVal = (curr->val * 2) % 10;
            if (curr->next != nullptr && curr->next->val >= 5) {
                newVal += 1;
            }
            curr->val = newVal;
            curr = curr->next;
        }
        
        return head;
    }
};
# @lc code=end