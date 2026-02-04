#@lc app=leetcode id=2289 lang=cpp
#
# [2289] Steps to Make Array Non-decreasing
#
# @lc code=start
class Solution {
public:
    int totalSteps(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 0); // dp array to store steps for each element
        stack<int> stk;
        int maxSteps = 0;
        
        // Iterate over each number in nums
        for (int i = 0; i < n; ++i) {
            while (!stk.empty() && nums[stk.top()] <= nums[i]) {
                dp[i] = max(dp[i], dp[stk.top()] + 1); // Calculate steps required for current element
                stk.pop(); // Pop elements that are less than or equal to current element from stack
            }
            stk.push(i); // Push current index onto stack
            maxSteps = max(maxSteps, dp[i]); // Update maxSteps if current dp[i] is greater than maxSteps so far
        }
        return maxSteps; // Return maximum steps required for entire array to be non-decreasing 
    } 
}; 
# @lc code=end