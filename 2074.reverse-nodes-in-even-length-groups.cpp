#
# @lc app=leetcode id=2074 lang=cpp
#
# [2074] Reverse Nodes in Even Length Groups
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
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        ListNode* curr = head;
        int group_size = 1;
        while (curr) {
            int cnt = 0;
            ListNode* group_head = curr;
            ListNode* temp = curr;
            // Count the actual group size
            while (cnt < group_size && temp) {
                cnt++;
                temp = temp->next;
            }
            ListNode* next_group = temp;
            // If even, reverse the group
            if (cnt % 2 == 0) {
                // Reverse cnt nodes
                ListNode* prev_rev = next_group;
                ListNode* node = group_head;
                for (int i = 0; i < cnt; ++i) {
                    ListNode* next = node->next;
                    node->next = prev_rev;
                    prev_rev = node;
                    node = next;
                }
                prev->next = prev_rev;
                prev = group_head;
            } else {
                // No reversal
                for (int i = 0; i < cnt; ++i) {
                    prev = curr;
                    curr = curr->next;
                }
                continue;
            }
            curr = next_group;
            group_size++;
        }
        return dummy.next;
    }
};
# @lc code=end