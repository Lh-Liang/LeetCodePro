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
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        // A critical point needs a previous and a next node.
        // If list has less than 3 nodes, no critical points possible.
        if (!head || !head->next || !head->next->next) {
            return {-1, -1};
        }

        int firstIndex = -1;
        int prevIndex = -1;
        int minDist = INT_MAX;
        
        int index = 1; // Start from the second node (index 1)
        int prevVal = head->val;
        ListNode* curr = head->next;
        
        while (curr->next != nullptr) {
            int nextVal = curr->next->val;
            
            // Check if current node is a local maxima or minima
            if ((curr->val > prevVal && curr->val > nextVal) || 
                (curr->val < prevVal && curr->val < nextVal)) {
                
                if (firstIndex == -1) {
                    // First critical point found
                    firstIndex = index;
                } else {
                    // Update minimum distance between adjacent critical points
                    minDist = min(minDist, index - prevIndex);
                }
                // Update the last seen critical point index
                prevIndex = index;
            }
            
            // Move to the next node
            prevVal = curr->val;
            curr = curr->next;
            index++;
        }
        
        // If minDist was never updated, it means we found fewer than 2 critical points
        if (minDist == INT_MAX) {
            return {-1, -1};
        }
        
        // maxDistance is the distance between the first and last critical point
        return {minDist, prevIndex - firstIndex};
    }
};
# @lc code=end