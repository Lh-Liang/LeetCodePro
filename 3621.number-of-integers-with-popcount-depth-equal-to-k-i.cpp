#
# @lc app=leetcode id=3621 lang=cpp
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#
# @lc code=start
class Solution {
public:
    long long popcountDepth(long long n, int k) {
        // Step 1: Initialize DP table and define recursive function
        vector<vector<long long>> dp(64, vector<long long>(6, -1)); // Supports up to 64 bits and depths up to 5
        
        function<long long(int, int)> dfs = [&](int bits, int depth) {
            if (depth > k) return 0LL; // No need if depth exceeds k
            if (bits == 0) return depth == k ? 1LL : 0LL; // Base case for reaching popcount-depth k
            if (dp[bits][depth] != -1) return dp[bits][depth];
            
            long long count = 0;
            for (int i = 0; i <= bits; ++i) {
                count += dfs(i, depth + 1); // Explore all possible next steps in sequence
            }
            return dp[bits][depth] = count;
        };
        
        // Step 2: Calculate total numbers with exact popcount-depth k
        long long result = dfs(__builtin_popcountll(n), 0);
        
        return result;
    }
};
# @lc code=end