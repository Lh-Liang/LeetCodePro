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
        // A critical point needs a previous and next node, so we need at least 3 nodes.
        if (!head || !head->next || !head->next->next) {
            return {-1, -1};
        }

        int firstCriticalIdx = -1;
        int lastCriticalIdx = -1;
        int minDistance = INT_MAX;
        
        ListNode* prev = head;
        ListNode* curr = head->next;
        int currentIndex = 1; // 0-indexed or 1-indexed doesn't matter for distance

        while (curr->next != nullptr) {
            ListNode* next = curr->next;
            bool isMaxima = (curr->val > prev->val && curr->val > next->val);
            bool isMinima = (curr->val < prev->val && curr->val < next->val);

            if (isMaxima || isMinima) {
                if (firstCriticalIdx == -1) {
                    firstCriticalIdx = currentIndex;
                } else {
                    // Update minimum distance using the gap between consecutive critical points
                    minDistance = min(minDistance, currentIndex - lastCriticalIdx);
                }
                lastCriticalIdx = currentIndex;
            }

            prev = curr;
            curr = next;
            currentIndex++;
        }

        // If we found fewer than two critical points
        if (firstCriticalIdx == -1 || lastCriticalIdx == firstCriticalIdx) {
            return {-1, -1};
        }

        // Max distance is always the distance between the first and last critical points found
        return {minDistance, lastCriticalIdx - firstCriticalIdx};
    }
};
# @lc code=end