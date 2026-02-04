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
class Solution {
public:
    ListNode* modifiedList(std::vector<int>& nums, ListNode* head) {
        std::unordered_set<int> to_delete(nums.begin(), nums.end());
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        ListNode* curr = head;
        while (curr) {
            if (to_delete.count(curr->val)) {
                prev->next = curr->next;
                // Optionally delete curr to free memory if needed
            } else {
                prev = curr;
            }
            curr = curr->next;
        }
        return dummy.next;
    }
};
# @lc code=end