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
        unordered_set<int> numSet(nums.begin(), nums.end()); // Convert nums into a hash set for fast lookup.
        ListNode dummy(0); // Create a dummy node to handle edge cases easily.
        dummy.next = head;
        ListNode* prev = &dummy; // Initialize previous pointer as dummy node.
        while (head != nullptr) { // Iterate through linked list.
            if (numSet.count(head->val)) { // Check if current value is in nums.
                prev->next = head->next; // Skip current node if it needs removal.
            } else {
                prev = head; // Move prev pointer if current node is retained.
            }
            head = head->next; // Move to next node.
        }
        return dummy.next; // Return new head of modified list.
    }
};
# @lc code=end