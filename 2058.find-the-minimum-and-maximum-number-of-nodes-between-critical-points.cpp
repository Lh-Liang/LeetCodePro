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
        if (!head || !head->next || !head->next->next) {
            return {-1, -1};
        }

        int firstCP = -1;
        int prevCP = -1;
        int minDist = INT_MAX;
        
        int prevVal = head->val;
        ListNode* curr = head->next;
        int currIdx = 1;

        while (curr->next != nullptr) {
            int currVal = curr->val;
            int nextVal = curr->next->val;

            // Check if curr is a local maxima or local minima
            if ((currVal > prevVal && currVal > nextVal) || (currVal < prevVal && currVal < nextVal)) {
                if (firstCP == -1) {
                    firstCP = currIdx;
                } else {
                    minDist = min(minDist, currIdx - prevCP);
                }
                prevCP = currIdx;
            }

            prevVal = currVal;
            curr = curr->next;
            currIdx++;
        }

        if (firstCP == prevCP) {
            return {-1, -1};
        }

        return {minDist, prevCP - firstCP};
    }
};
# @lc code=end