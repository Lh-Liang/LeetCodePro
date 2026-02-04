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
        vector<int> criticalPoints; // To store indices of critical points.
        ListNode *prev = nullptr, *curr = head;
        int index = 0; // Current index in the linked list. 
        while (curr && curr->next) { // Traverse through the linked list. 
            if (prev && ((curr->val > prev->val && curr->val > curr->next->val) || 
                        (curr->val < prev->val && curr->val < curr->next->val))) { // Check for local maxima/minima. 
                criticalPoints.push_back(index); // Record index if a critical point is found. 
            } 
            prev = curr; // Move to the next node. 
            curr = curr->next; 
            index++; // Increment index. 
        } 
        if (criticalPoints.size() < 2) return {-1, -1}; // Return [-1, -1] if less than two critical points exist. 
        int minDistance = INT_MAX, maxDistance = criticalPoints.back() - criticalPoints.front(); 
        for (int i = 1; i < criticalPoints.size(); ++i) { 
            minDistance = min(minDistance, criticalPoints[i] - criticalPoints[i - 1]); // Calculate minimum distance between consecutive critical points. 
        } 
        return {minDistance, maxDistance}; // Return minimum and maximum distances found. 
    }
};
# @lc code=end