#
# @lc app=leetcode id=3725 lang=cpp
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
#include <vector>
#include <numeric>
#include <map>

using namespace std;

class Solution {
public:
    int countCoprime(vector<vector<int>>& mat) {
        int m = mat.size();
        int MOD = 1e9 + 7;
        int MAX_VAL = 0;
        
        // Find the maximum possible value to size our DP array, though 150 is the constraint limit.
        // The constraints say values <= 150.
        for(const auto& row : mat) {
            for(int val : row) {
                MAX_VAL = max(MAX_VAL, val);
            }
        }
        
        // dp[g] stores the number of ways to pick numbers from processed rows
        // such that their running GCD is g.
        vector<long long> dp(MAX_VAL + 1, 0);
        
        // Initialize for the first row
        // We use a map or frequency array to handle duplicates in the row.
        // Since we need to pick exactly one from the row, duplicates just add to the ways.
        for (int val : mat[0]) {
            dp[val]++;
        }
        
        // Process remaining rows
        for (int i = 1; i < m; ++i) {
            vector<long long> next_dp(MAX_VAL + 1, 0);
            
            // Count frequencies of numbers in the current row to optimize
            // Instead of iterating n times, we iterate distinct values (at most 150).
            vector<int> row_counts(MAX_VAL + 1, 0);
            bool has_val = false;
            for (int val : mat[i]) {
                row_counts[val]++;
                has_val = true;
            }
            
            if (!has_val) continue; // Should not happen based on constraints

            // Iterate over all possible GCD values from the previous state
            for (int g = 1; g <= MAX_VAL; ++g) {
                if (dp[g] == 0) continue;
                
                // Try combining with every number present in the current row
                for (int val = 1; val <= MAX_VAL; ++val) {
                    if (row_counts[val] > 0) {
                        int new_gcd = std::gcd(g, val);
                        long long ways = (dp[g] * row_counts[val]) % MOD;
                        next_dp[new_gcd] = (next_dp[new_gcd] + ways) % MOD;
                    }
                }
            }
            dp = next_dp;
        }
        
        return dp[1];
    }
};
# @lc code=end