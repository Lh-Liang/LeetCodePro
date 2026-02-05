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
        vector<int> criticalIndices;
        ListNode* prev = head;
        ListNode* curr = head->next;
        int idx = 1;
        while (curr && curr->next) {
            if ((curr->val > prev->val && curr->val > curr->next->val) ||
                (curr->val < prev->val && curr->val < curr->next->val)) {
                criticalIndices.push_back(idx);
            }
            prev = curr;
            curr = curr->next;
            idx++;
        }
        if (criticalIndices.size() < 2) return {-1, -1};
        int minDist = INT_MAX, maxDist = criticalIndices.back() - criticalIndices.front();
        for (size_t i = 1; i < criticalIndices.size(); ++i) {
            minDist = min(minDist, criticalIndices[i] - criticalIndices[i-1]);
        }
        return {minDist, maxDist};
    }
};
# @lc code=end