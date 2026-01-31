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
        // The first group has length 1, which is odd, so it's never reversed.
        // We start processing from the second group.
        if (!head || !head->next) return head;
        
        ListNode* prev = head;
        int groupLen = 2;
        
        while (prev->next) {
            ListNode* curr = prev->next;
            ListNode* temp = curr;
            int count = 0;
            
            // Count the actual number of nodes in the current group
            while (count < groupLen && temp) {
                temp = temp->next;
                count++;
            }
            
            if (count % 2 == 0) {
                // Reverse the 'count' nodes starting from 'curr'
                ListNode* node = curr;
                ListNode* p = temp; // 'p' will eventually be the new head of this reversed segment
                for (int i = 0; i < count; ++i) {
                    ListNode* nextNode = node->next;
                    node->next = p;
                    p = node;
                    node = nextNode;
                }
                // Connect the previous group to the new head of the reversed segment
                prev->next = p;
                // Move 'prev' to the tail of the reversed segment (which was the original 'curr')
                prev = curr;
            } else {
                // No reversal needed, move 'prev' to the last node of the current group
                for (int i = 0; i < count; ++i) {
                    prev = prev->next;
                }
            }
            groupLen++;
        }
        
        return head;
    }
};
# @lc code=end