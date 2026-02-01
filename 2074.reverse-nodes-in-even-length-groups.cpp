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
        if (!head || !head->next) return head;
        
        ListNode* prev = head;
        int groupSize = 2;
        
        while (prev->next) {
            ListNode* curr = prev->next;
            int actualLen = 0;
            ListNode* temp = curr;
            
            // Count nodes in the current group
            while (temp && actualLen < groupSize) {
                temp = temp->next;
                actualLen++;
            }
            
            if (actualLen % 2 == 0) {
                // Reverse the group of size actualLen
                ListNode* node = curr;
                ListNode* revPrev = temp; // Connect the tail of reversed group to the next group
                for (int i = 0; i < actualLen; ++i) {
                    ListNode* nextNode = node->next;
                    node->next = revPrev;
                    revPrev = node;
                    node = nextNode;
                }
                prev->next = revPrev; // Connect the previous group to the head of reversed group
                prev = curr; // Move prev to the end of the reversed group (which was the original head)
            } else {
                // Skip the group if it has odd length
                for (int i = 0; i < actualLen; ++i) {
                    prev = prev->next;
                }
            }
            groupSize++;
        }
        
        return head;
    }
};
# @lc code=end