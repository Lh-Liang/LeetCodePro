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
        // A critical point requires at least 3 nodes (prev, curr, next)
        if (!head || !head->next || !head->next->next) {
            return {-1, -1};
        }

        int firstIdx = -1;
        int lastIdx = -1;
        int minDistance = INT_MAX;
        int currIdx = 1; // Starting index for the second node

        ListNode* prev = head;
        ListNode* curr = head->next;

        while (curr->next != nullptr) {
            ListNode* next = curr->next;
            bool isMax = (curr->val > prev->val && curr->val > next->val);
            bool isMin = (curr->val < prev->val && curr->val < next->val);

            if (isMax || isMin) {
                if (firstIdx == -1) {
                    // First critical point found
                    firstIdx = currIdx;
                } else {
                    // Update minimum distance between adjacent critical points
                    minDistance = min(minDistance, currIdx - lastIdx);
                }
                // Always update the last seen critical point index
                lastIdx = currIdx;
            }

            // Move pointers forward
            prev = curr;
            curr = next;
            currIdx++;
        }

        // If we found fewer than 2 critical points, minDistance will still be INT_MAX
        if (minDistance == INT_MAX) {
            return {-1, -1};
        }

        return {minDistance, lastIdx - firstIdx};
    }
};
# @lc code=end