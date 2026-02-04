#
# @lc app=leetcode id=3217 lang=cpp
#
# [3217] Delete Nodes From Linked List Present in Array
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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        std::unordered_set<int> numSet(nums.begin(), nums.end()); // Step 1: Convert nums to set for quick lookup.
        ListNode dummy(0); // Step 2: Create a dummy node.
        dummy.next = head; // Point dummy node to head. 
        ListNode *prev = &dummy; // Step 3: Initialize prev pointer at dummy. 
        while (head != nullptr) { 
            if (numSet.count(head->val)) { 
                prev->next = head->next; // Skip node if value is in numSet. 
            } else { 
                prev = head; // Move prev pointer if no removal needed. 
            } 
            head = head->next; // Move forward in list. 
        } 
        return dummy.next; // Step 4: Return modified list starting from dummy.next. 
    } 
}; 
# @lc code=end