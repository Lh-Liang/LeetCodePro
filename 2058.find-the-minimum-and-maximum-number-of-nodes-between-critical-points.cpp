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

        int first_cp = -1;
        int prev_cp = -1;
        int min_dist = INT_MAX;
        
        ListNode* prev = head;
        ListNode* curr = head->next;
        int idx = 1;

        while (curr->next) {
            ListNode* next = curr->next;
            bool is_cp = false;
            
            // Check local maxima or local minima
            if ((curr->val > prev->val && curr->val > next->val) || 
                (curr->val < prev->val && curr->val < next->val)) {
                is_cp = true;
            }

            if (is_cp) {
                if (first_cp == -1) {
                    first_cp = idx;
                } else {
                    min_dist = min(min_dist, idx - prev_cp);
                }
                prev_cp = idx;
            }

            prev = curr;
            curr = next;
            idx++;
        }

        // If we found fewer than 2 critical points
        if (first_cp == -1 || prev_cp == first_cp) {
            return {-1, -1};
        }

        return {min_dist, prev_cp - first_cp};
    }
};
# @lc code=end