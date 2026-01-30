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
#include <unordered_set>
#include <vector>

class Solution {
public:
    ListNode* modifiedList(std::vector<int>& nums, ListNode* head) {
        std::unordered_set<int> numSet(nums.begin(), nums.end());
        ListNode dummy(0, head);
        ListNode* curr = &dummy;

        while (curr->next != nullptr) {
            if (numSet.find(curr->next->val) != numSet.end()) {
                // The next node should be deleted
                ListNode* temp = curr->next;
                curr->next = curr->next->next;
                // In a real environment, we might delete temp here if not using a GC-like system
            } else {
                // Move to the next node
                curr = curr->next;
            }
        }

        return dummy.next;
    }
};
# @lc code=end