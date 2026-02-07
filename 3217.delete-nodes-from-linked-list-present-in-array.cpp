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
    ListNode* modifiedList(std::vector<int>& nums, ListNode* head) {
        std::unordered_set<int> num_set(nums.begin(), nums.end());
        ListNode dummy(0);
        dummy.next = head;
        ListNode* current = &dummy;
        while (current->next != nullptr) {
            if (num_set.count(current->next->val)) {
                current->next = current->next->next;
            } else {
                current = current->next;
            }
        }
        return dummy.next;
    }
};
# @lc code=end