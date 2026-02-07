#
# @lc app=leetcode id=3743 lang=cpp
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
class Solution {
public:
    long long maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        long long max_score = 0;
        // Dynamic programming table for storing maximum scores based on partition points
        vector<vector<long long>> dp(n, vector<long long>(k + 1, 0));
        // Iterate over each possible starting point in original `nums`
        for (int start = 0; start < n; ++start) {
            int max_val = INT_MIN, min_val = INT_MAX;
            // Use deque for efficient range queries (maintaining max/min)
            deque<int> maxDeque, minDeque;
            // Extend window up to n elements from start (handle wrap-around using modulo)
            for (int end = start; end < start + n; ++end) {
                int idx = end % n;
                // Maintain max/min using deque
                while (!maxDeque.empty() && nums[maxDeque.back()] <= nums[idx]) {
                    maxDeque.pop_back();
                }
                while (!minDeque.empty() && nums[minDeque.back()] >= nums[idx]) {
                    minDeque.pop_back();
                }
                maxDeque.push_back(idx);
                minDeque.push_back(idx);
                // Calculate range from deques' front elements
                int currentRange = nums[maxDeque.front()] - nums[minDeque.front()];
                if ((end - start + 1) <= k) { // Valid partition size check
                    dp[start][end - start + 1] = std::max(dp[start][end - start + 1], currentRange);
                    if (start > 0) {
                        dp[start][end - start + 1] += dp[start - 1][k];
                    }
                    max_score = std::max(max_score, dp[start][end - start + 1]);
                }
                // Remove out-of-window elements from deques
                if (!maxDeque.empty() && maxDeque.front() == idx - k) {
                    maxDeque.pop_front();
                }
                if (!minDeque.empty() && minDeque.front() == idx - k) {
                    minDeque.pop_front();
                }
            }
        }
        return max_score;
    }
};
# @lc code=end