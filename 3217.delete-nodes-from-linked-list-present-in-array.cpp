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
        // Use an unordered_set for O(1) lookups
        unordered_set<int> numSet(nums.begin(), nums.end());
        
        // Create a dummy node to handle edge cases easily (e.g., removing head)
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        
        ListNode* prev = dummy;
        ListNode* curr = head;
        
        while (curr != nullptr) {
            if (numSet.count(curr->val)) {
                // If current node's value is in the set, remove it
                prev->next = curr->next;
                // Move curr forward, but keep prev the same
                // (the next node might also need removal)
                curr = curr->next;
            } else {
                // If not removing, move both pointers
                prev = curr;
                curr = curr->next;
            }
        }
        
        return dummy->next;
    }
};
# @lc code=end