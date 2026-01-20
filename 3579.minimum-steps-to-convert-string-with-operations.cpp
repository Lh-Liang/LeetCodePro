#
# @lc app=leetcode id=3579 lang=cpp
#
# [3579] Minimum Steps to Convert String with Operations
#

# @lc code=start
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int minOperations(string word1, string word2) {
        int n = word1.length();
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;

        auto hamming = [](const string& s1, const string& s2) {
            int count = 0;
            for (size_t i = 0; i < s1.length(); ++i) {
                if (s1[i] != s2[i]) count++;
            }
            return count;
        };

        auto min_swap_hamming = [&](string s1, const string& s2) {
            int len = s1.length();
            if (len < 2) return 1000000; // Impossible to swap
            
            int base_dist = 0;
            vector<int> mismatch(len, 0);
            for(int i=0; i<len; ++i) {
                if(s1[i] != s2[i]) {
                    base_dist++;
                    mismatch[i] = 1;
                }
            }

            int max_reduction = 0;
            // Try swapping every pair (i, j)
            for (int i = 0; i < len; ++i) {
                for (int j = i + 1; j < len; ++j) {
                    int current_mismatch_i = mismatch[i];
                    int current_mismatch_j = mismatch[j];
                    
                    int new_mismatch_i = (s1[j] != s2[i]);
                    int new_mismatch_j = (s1[i] != s2[j]);
                    
                    int reduction = (current_mismatch_i + current_mismatch_j) - 
                                    (new_mismatch_i + new_mismatch_j);
                    
                    if (reduction > max_reduction) {
                        max_reduction = reduction;
                    }
                }
            }
            return base_dist - max_reduction;
        };

        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < i; ++j) {
                string sub1 = word1.substr(j, i - j);
                string sub2 = word2.substr(j, i - j);
                
                // Option 1: Just Replace
                int cost1 = hamming(sub1, sub2);
                
                // Option 2: Reverse + Replace
                string rev_sub1 = sub1;
                reverse(rev_sub1.begin(), rev_sub1.end());
                int cost2 = 1 + hamming(rev_sub1, sub2);
                
                // Option 3: Swap + Replace
                int cost3 = 1 + min_swap_hamming(sub1, sub2);
                
                // Option 4: Reverse + Swap + Replace
                int cost4 = 2 + min_swap_hamming(rev_sub1, sub2);
                
                int min_cost = min({cost1, cost2, cost3, cost4});
                
                if (dp[j] != INT_MAX) {
                    dp[i] = min(dp[i], dp[j] + min_cost);
                }
            }
        }

        return dp[n];
    }
};
# @lc code=end