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
        // Step 1: Store elements of nums in a hash set for O(1) lookup
        unordered_set<int> numSet(nums.begin(), nums.end());

        // Step 2: Use a dummy node to handle cases where the head needs to be removed
        ListNode dummy(0, head);
        ListNode* curr = &dummy;

        // Step 3: Traverse the list and remove nodes present in numSet
        while (curr->next != nullptr) {
            if (numSet.count(curr->next->val)) {
                // Node needs removal
                ListNode* temp = curr->next;
                curr->next = curr->next->next;
                delete temp; // Free memory
            } else {
                // Move to the next node
                curr = curr->next;
            }
        }

        return dummy.next;
    }
};
# @lc code=end