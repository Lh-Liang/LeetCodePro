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

        int first_cp = -1;
        int prev_cp = -1;
        int min_dist = 2147483647; // INT_MAX
        
        ListNode* prev = head;
        ListNode* curr = head->next;
        int index = 1;

        while (curr->next) {
            bool is_maxima = (curr->val > prev->val && curr->val > curr->next->val);
            bool is_minima = (curr->val < prev->val && curr->val < curr->next->val);

            if (is_maxima || is_minima) {
                if (first_cp == -1) {
                    first_cp = index;
                } else {
                    int current_dist = index - prev_cp;
                    if (current_dist < min_dist) {
                        min_dist = current_dist;
                    }
                }
                prev_cp = index;
            }

            prev = curr;
            curr = curr->next;
            index++;
        }

        if (first_cp == -1 || first_cp == prev_cp) {
            return {-1, -1};
        }

        return {min_dist, prev_cp - first_cp};
    }
};
# @lc code=end