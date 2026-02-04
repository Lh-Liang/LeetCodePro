#
# @lc app=leetcode id=2816 lang=cpp
#
# [2816] Double a Number Represented as a Linked List
#

# @lc code=start
class Solution {
public:
    ListNode* doubleIt(ListNode* head) {
        if (!head) return head;
        ListNode* current = head;
        int carry = 0;
        while (current) {
            int sum = current->val * 2 + carry;
            current->val = sum % 10;
            carry = sum / 10;
            if (!current->next && carry > 0) {
                current->next = new ListNode(carry);
                break;
            }
            current = current->next;
        }
        return head;
    }
};
# @lc code=end