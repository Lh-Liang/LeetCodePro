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
        if (!head || !head->next || !head->next->next) {
            return {-1, -1};
        }

        int firstPos = -1;
        int prevPos = -1;
        int minDist = 2147483647; // INT_MAX
        
        ListNode* prev = head;
        ListNode* curr = head->next;
        int currIdx = 1;

        while (curr->next != nullptr) {
            ListNode* next = curr->next;
            
            if ((curr->val > prev->val && curr->val > next->val) ||
                (curr->val < prev->val && curr->val < next->val)) {
                
                if (firstPos == -1) {
                    firstPos = currIdx;
                } else {
                    int d = currIdx - prevPos;
                    if (d < minDist) minDist = d;
                }
                prevPos = currIdx;
            }

            prev = curr;
            curr = next;
            currIdx++;
        }

        if (firstPos == -1 || firstPos == prevPos) {
            return {-1, -1};
        }

        return {minDist, prevPos - firstPos};
    }
};
# @lc code=end