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
        std::unordered_set<int> s(nums.begin(), nums.end());
        ListNode dummy(0, head);
        ListNode* curr = &dummy;
        
        while (curr->next) {
            if (s.find(curr->next->val) != s.end()) {
                ListNode* temp = curr->next;
                curr->next = curr->next->next;
                // Note: In a real environment, we might delete temp here if not using a GC-like system,
                // but for LeetCode standard solutions, pointer redirection is the focus.
            } else {
                curr = curr->next;
            }
        }
        return dummy.next;
    }
};
# @lc code=end