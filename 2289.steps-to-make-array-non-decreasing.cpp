#
# @lc app=leetcode id=2289 lang=cpp
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int totalSteps(std::vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        // Stack stores pairs of {value, steps_to_be_removed}
        // Using a vector as a stack for efficiency
        std::vector<std::pair<int, int>> st;
        
        for (int x : nums) {
            int t = 0;
            // While current x is greater than or equal to stack top,
            // x 'covers' the removal process of those elements.
            while (!st.empty() && st.back().first <= x) {
                t = std::max(t, st.back().second);
                st.pop_back();
            }
            
            // If stack is empty, x has no larger element to its left to remove it.
            // Otherwise, x is removed at step t + 1.
            if (st.empty()) {
                t = 0;
            } else {
                t = t + 1;
            }
            
            ans = std::max(ans, t);
            st.push_back({x, t});
        }
        
        return ans;
    }
};
# @lc code=end