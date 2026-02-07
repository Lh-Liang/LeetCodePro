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
        if (!head || !head->next || !head->next->next) return {-1, -1};
        vector<int> critical_points;
        ListNode *prev = head, *curr = head->next;
        int index = 1;
        while (curr->next) {
            if ((curr->val > prev->val && curr->val > curr->next->val) || 
                (curr->val < prev->val && curr->val < curr->next->val)) {
                critical_points.push_back(index);
            }
            prev = curr;
            curr = curr->next;
            index++;
        }
        if (critical_points.size() < 2) return {-1, -1}; 
        int min_dist = INT_MAX, max_dist = critical_points.back() - critical_points.front(); 
        for (size_t i = 1; i < critical_points.size(); ++i) { 
            min_dist = min(min_dist, critical_points[i] - critical_points[i-1]); 
        } 
        return {min_dist, max_dist}; 
    } 
}; 
lc code=end