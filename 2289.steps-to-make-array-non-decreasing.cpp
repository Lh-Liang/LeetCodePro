#
# @lc app=leetcode id=2289 lang=cpp
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
#include <vector>
#include <stack>
#include <algorithm>
#include <utility>

using namespace std;

class Solution {
public:
    int totalSteps(vector<int>& nums) {
        int n = nums.size();
        int maxSteps = 0;
        // Stack stores pairs of {value, steps_to_be_removed}
        stack<pair<int, int>> st;
        
        for (int i = 0; i < n; ++i) {
            int currentElementSteps = 0;
            
            // Pop elements that are smaller than or equal to current. 
            // They don't block the current element from being removed by a larger one further left.
            while (!st.empty() && nums[i] >= st.top().first) {
                currentElementSteps = max(currentElementSteps, st.top().second);
                st.pop();
            }
            
            if (st.empty()) {
                // No element to the left is larger; this element stays forever.
                st.push({nums[i], 0});
            } else {
                // The element at the top of the stack is the one that will remove nums[i].
                // It takes 1 step more than the time taken to clear the elements between them.
                int steps = currentElementSteps + 1;
                maxSteps = max(maxSteps, steps);
                st.push({nums[i], steps});
            }
        }
        
        return maxSteps;
    }
};
# @lc code=end