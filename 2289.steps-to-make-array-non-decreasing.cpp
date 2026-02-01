#
# @lc app=leetcode id=2289 lang=cpp
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    int totalSteps(vector<int>& nums) {
        int n = nums.size();
        int max_total_steps = 0;
        // Stack stores pairs of {value, steps_to_be_removed}
        stack<pair<int, int>> s;
        
        for (int x : nums) {
            int cur_steps = 0;
            // While current element is larger or equal, it 'outlasts' the elements on the stack.
            // We need to find the element to the left that is strictly greater than x.
            while (!s.empty() && s.top().first <= x) {
                cur_steps = max(cur_steps, s.top().second);
                s.pop();
            }
            
            int steps_for_x = 0;
            if (!s.empty()) {
                // x will be removed 1 step after the elements between it and its remover are gone.
                steps_for_x = cur_steps + 1;
            } else {
                // No larger element to the left, x stays forever.
                steps_for_x = 0;
            }
            
            max_total_steps = max(max_total_steps, steps_for_x);
            s.push({x, steps_for_x});
        }
        
        return max_total_steps;
    }
};
# @lc code=end