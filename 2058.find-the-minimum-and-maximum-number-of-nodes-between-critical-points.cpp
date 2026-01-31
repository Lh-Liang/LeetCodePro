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
        
        ListNode* prev = head;
        ListNode* curr = head->next;
        int index = 1;

        while (curr->next) {
            ListNode* next = curr->next;
            bool isCP = false;
            
            // Check for local maxima or local minima
            if ((curr->val > prev->val && curr->val > next->val) || 
                (curr->val < prev->val && curr->val < next->val)) {
                isCP = true;
            }

            if (isCP) {
                if (firstCP == -1) {
                    firstCP = index;
                } else {
                    minDist = min(minDist, index - prevCP);
                }
                prevCP = index;
            }

            prev = curr;
            curr = next;
            index++;
        }

        if (firstCP == -1 || prevCP == firstCP) {
            return {-1, -1};
        }

        return {minDist, prevCP - firstCP};
    }
};
# @lc code=end