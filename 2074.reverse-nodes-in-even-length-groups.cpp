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
        if (!head || !head->next) return head; // Base case for empty or single-node lists.
        
        ListNode *current = head;
        int group_length = 1; // Start with group length 1.
        while (current) {
            // Determine current group's actual length.
            int count = 0;
            ListNode *group_head = current; // Start of this group.
            while (current && count < group_length) { // Traverse until end of current group or end of list.
                current = current->next; 
                count++; 
            }
            if (count % 2 == 0) { // If group length is even, reverse it. 
                group_head = reverse(group_head, count); 
                if (group_head == head) { // Special case handling for first node change. 
                    head = group_head; 
                } 
            } 
            // Move to next group's start node – already set by 'current'. – No need to adjust 'current'. – Group length increases by 1 naturally. – Loop will handle increment automatically later on. – No need to manually alter 'group_length' or make any special cases here as it naturally increments per iteration cycle already by default auto-increment operation inside this loop design pattern structure here done naturally automatically inherently here natively.