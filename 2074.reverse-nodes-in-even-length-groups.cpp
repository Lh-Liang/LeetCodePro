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
        
        ListNode* prevGroupTail = head;
        int expectedLen = 2;
        
        while (prevGroupTail->next) {
            // Count actual nodes in the current group
            int actualLen = 0;
            ListNode* curr = prevGroupTail->next;
            while (curr && actualLen < expectedLen) {
                curr = curr->next;
                actualLen++;
            }
            
            if (actualLen % 2 == 0) {
                // Reverse the nodes in this even-length group
                ListNode* node_curr = prevGroupTail->next;
                ListNode* node_prev = nullptr;
                ListNode* groupTail = node_curr; 
                
                for (int i = 0; i < actualLen; ++i) {
                    ListNode* nextTemp = node_curr->next;
                    node_curr->next = node_prev;
                    node_prev = node_curr;
                    node_curr = nextTemp;
                }
                
                // Reconnect reversed group
                prevGroupTail->next = node_prev;
                groupTail->next = node_curr;
                
                // Update prevGroupTail to the end of the processed group
                prevGroupTail = groupTail;
            } else {
                // Skip the nodes in this odd-length group
                for (int i = 0; i < actualLen; ++i) {
                    prevGroupTail = prevGroupTail->next;
                }
            }
            
            expectedLen++;
        }
        
        return head;
    }
};
# @lc code=end