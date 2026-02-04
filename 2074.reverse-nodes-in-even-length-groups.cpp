#
# @lc app=leetcode id=2074 lang=cpp
#
# [2074] Reverse Nodes in Even Length Groups
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
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode *current = head, *prevTail = nullptr;
        int groupSize = 1;
        while (current) {
            int count = 0;
            ListNode *groupHead = current; 
            while (current && count < groupSize) { 
                current = current->next; 
                count++; 
            }
            if (count % 2 == 0) { // reverse if even length group
                ListNode* prev = nullptr;
                ListNode* node = groupHead;
                for (int i = 0; i < count; ++i) {
                    ListNode* nextNode = node->next;
                    node->next = prev;
                    prev = node;
                    node = nextNode;
                }
                if (prevTail) {
                    prevTail->next = prev;
                } else {
                    head = prev; // update head if first group is reversed
                }
                groupHead->next = current; // connect tail of reversed segment
                prevTail = groupHead;
            } else {
                prevTail = groupHead; // move prevTail to the end of non-reversed segment
            }
            groupSize++;
        }
        return head;
    }
};
# @lc code=end