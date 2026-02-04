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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        while(head) {
            ListNode* next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
    ListNode* doubleIt(ListNode* head) {
        head = reverseList(head);
        ListNode* curr = head;
        int carry = 0;
        ListNode* prev = nullptr;
        while(curr) {
            int total = curr->val * 2 + carry;
            curr->val = total % 10;
            carry = total / 10;
            prev = curr;
            curr = curr->next;
        }
        if(carry) {
            prev->next = new ListNode(carry);
        }
        head = reverseList(head);
        return head;
    }
};
# @lc code=end