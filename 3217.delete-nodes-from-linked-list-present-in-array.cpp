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
        // Convert nums to a set for O(1) lookup
        unordered_set<int> toRemove(nums.begin(), nums.end());
        
        // Create a dummy node to simplify head handling
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        
        ListNode* prev = dummy;
        ListNode* curr = head;
        
        while (curr != nullptr) {
            if (toRemove.count(curr->val)) {
                // Remove current node by skipping it
                prev->next = curr->next;
            } else {
                // Move prev forward
                prev = curr;
            }
            // Always move curr forward
            curr = curr->next;
        }
        
        return dummy->next;
    }
};
# @lc code=end