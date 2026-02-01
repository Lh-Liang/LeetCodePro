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
        int maxSteps = 0;
        // Stack stores pairs of {value, steps_until_removed}
        stack<pair<int, int>> st;
        
        for (int num : nums) {
            int currentSteps = 0;
            // While current num is greater than or equal to elements on stack,
            // it means those elements would be removed 'under' a larger element
            // to the left before this num can be removed.
            while (!st.empty() && st.top().first <= num) {
                currentSteps = max(currentSteps, st.top().second);
                st.pop();
            }
            
            if (st.empty()) {
                // No larger element to the left exists to trigger removal.
                currentSteps = 0;
            } else {
                // The element on top is strictly greater than num.
                // Num will be removed 1 step after the elements between it and the top are gone.
                currentSteps++;
            }
            
            maxSteps = max(maxSteps, currentSteps);
            st.push({num, currentSteps});
        }
        
        return maxSteps;
    }
};
# @lc code=end