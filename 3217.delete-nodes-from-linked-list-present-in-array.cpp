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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        std::unordered_set<int> val_set(nums.begin(), nums.end());
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        while (prev->next) {
            if (val_set.count(prev->next->val)) {
                ListNode* tmp = prev->next;
                prev->next = tmp->next;
                delete tmp;
            } else {
                prev = prev->next;
            }
        }
        return dummy.next;
    }
};
# @lc code=end