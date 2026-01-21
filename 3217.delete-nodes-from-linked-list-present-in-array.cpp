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
        unordered_set<int> s(nums.begin(), nums.end());
        ListNode** cur = &head;
        while (*cur) {
            if (s.count((*cur)->val)) {
                *cur = (*cur)->next;
            } else {
                cur = &((*cur)->next);
            }
        }
        return head;
    }
};
# @lc code=end