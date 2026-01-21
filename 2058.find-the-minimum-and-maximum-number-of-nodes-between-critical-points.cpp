#
# @lc app=leetcode id=2058 lang=cpp
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
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
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        // Need at least 3 nodes for any critical point to exist
        if (!head || !head->next || !head->next->next) {
            return {-1, -1};
        }
        
        int firstCritical = -1;
        int lastCritical = -1;
        int minDistance = INT_MAX;
        
        ListNode* prev = head;
        ListNode* curr = head->next;
        int index = 1;
        
        while (curr->next) {
            int prevVal = prev->val;
            int currVal = curr->val;
            int nextVal = curr->next->val;
            
            // Check if current node is a critical point (local maxima or minima)
            if ((currVal > prevVal && currVal > nextVal) || 
                (currVal < prevVal && currVal < nextVal)) {
                if (firstCritical == -1) {
                    firstCritical = index;
                } else {
                    minDistance = min(minDistance, index - lastCritical);
                }
                lastCritical = index;
            }
            
            prev = curr;
            curr = curr->next;
            index++;
        }
        
        // If fewer than 2 critical points
        if (firstCritical == lastCritical) {
            return {-1, -1};
        }
        
        return {minDistance, lastCritical - firstCritical};
    }
};
# @lc code=end