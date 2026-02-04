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
        std::unordered_set<int> numSet(nums.begin(), nums.end()); // Step 1: Initialize hash set.
        ListNode dummy(0); // Step 2: Create dummy node.
        dummy.next = head;
        ListNode* prev = &dummy;
        while (head != nullptr) { // Step 3: Traverse using two pointers.
            if (numSet.find(head->val) != numSet.end()) { // Step 4: Check if current node's value is in hash set.
                prev->next = head->next; // Remove current node.
            } else {
                prev = head; // Move prev only if current node is not removed.
            }
            head = head->next; // Move current pointer forward (Step 5).
        }
        return dummy.next; // Step 6: Return new head of modified list.
    }
};
# @lc code=end