# 
# @lc app=leetcode id=2058 lang=cpp
# 
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
# 

# @lc code=start
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        if (!head || !head->next || !head->next->next) return {-1, -1};
        vector<int> criticalPoints;
        ListNode *previousNode = head;
        ListNode *currentNode = head->next;
        int index = 1; // Starting from second node as head is index 0.
        while (currentNode && currentNode->next) {
            ListNode *nextNode = currentNode->next;
            if ((currentNode->val > previousNode->val && currentNode->val > nextNode->val) || // Local maxima
                (currentNode->val < previousNode->val && currentNode->val < nextNode->val)) { // Local minima
                criticalPoints.push_back(index);
            }
            previousNode = currentNode;
            currentNode = nextNode;
            ++index;
        }
        if (criticalPoints.size() < 2) return {-1, -1};
        int minDistance = INT_MAX;
        for (size_t i = 1; i < criticalPoints.size(); ++i) {
            minDistance = min(minDistance, criticalPoints[i] - criticalPoints[i - 1]);
        }
        int maxDistance = criticalPoints.back() - criticalPoints.front();
        return {minDistance, maxDistance};
    }
};
# @lc code=end