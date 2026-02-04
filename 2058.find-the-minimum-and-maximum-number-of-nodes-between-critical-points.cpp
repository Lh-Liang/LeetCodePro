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
        int idx = 0;
        ListNode* prev = head;
        ListNode* curr = head ? head->next : nullptr;
        int pos = 1;
        while (curr && curr->next) {
            if ((curr->val > prev->val && curr->val > curr->next->val) ||
                (curr->val < prev->val && curr->val < curr->next->val)) {
                criticalIndices.push_back(pos);
            }
            prev = curr;
            curr = curr->next;
            ++pos;
        }
        if (criticalIndices.size() < 2) {
            return {-1, -1};
        }
        int minDist = INT_MAX;
        for (int i = 1; i < criticalIndices.size(); ++i) {
            minDist = min(minDist, criticalIndices[i] - criticalIndices[i-1]);
        }
        int maxDist = criticalIndices.back() - criticalIndices.front();
        return {minDist, maxDist};
    }
};
# @lc code=end