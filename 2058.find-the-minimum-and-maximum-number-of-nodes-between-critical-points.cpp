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
        int index = 0;
        int firstCritical = -1; 
        int lastCritical = -1; 
        vector<int> criticalIndices; 
        ListNode* prev = nullptr; 
        ListNode* curr = head; 
        while (curr && curr->next) { 
            if (prev && ((curr->val > prev->val && curr->val > curr->next->val) || (curr->val < prev->val && curr->val < curr->next->val))) { 
                if (firstCritical == -1) firstCritical = index; 
                lastCritical = index; 
                criticalIndices.push_back(index); 
            } 
            prev = curr; 
            curr = curr->next; 
            index++; 
        } 
        if (criticalIndices.size() < 2) return {-1, -1}; 
        int minDistance = INT_MAX; 
        for (int i = 1; i < criticalIndices.size(); ++i) { 
            minDistance = min(minDistance, criticalIndices[i] - criticalIndices[i-1]); 
        } 
        int maxDistance = lastCritical - firstCritical; 
        return {minDistance, maxDistance}; 
    }
};
# @lc code=end