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
        if (!head || !head->next) return {-1, -1};

        ListNode* prev = head;
        ListNode* cur = head->next;
        int idx = 2; // 1-based index of cur

        int firstCritical = -1;
        int lastCritical = -1;
        int prevCritical = -1;
        int minDist = INT_MAX;
        int criticalCount = 0;

        while (cur && cur->next) {
            ListNode* nxt = cur->next;
            bool isMax = (cur->val > prev->val && cur->val > nxt->val);
            bool isMin = (cur->val < prev->val && cur->val < nxt->val);

            if (isMax || isMin) {
                criticalCount++;
                if (firstCritical == -1) firstCritical = idx;
                lastCritical = idx;

                if (prevCritical != -1) {
                    minDist = min(minDist, idx - prevCritical);
                }
                prevCritical = idx;
            }

            prev = cur;
            cur = nxt;
            idx++;
        }

        if (criticalCount < 2) return {-1, -1};
        return {minDist, lastCritical - firstCritical};
    }
};
# @lc code=end
