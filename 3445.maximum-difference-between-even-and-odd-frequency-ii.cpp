#
# @lc app=leetcode id=3445 lang=cpp
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#
# @lc code=start
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.length();
        // Precompute prefix counts for digits '0' through '4'
        vector<vector<int>> P(5, vector<int>(n + 1, 0));
        for (int i = 0; i < n; ++i) {
            int digit = s[i] - '0';
            for (int d = 0; d < 5; ++d) {
                P[d][i + 1] = P[d][i] + (d == digit);
            }
        }
        
        int max_diff = -1e9;
        
        // Iterate through every ordered pair of distinct digits (a, b)
        for (int a = 0; a < 5; ++a) {
            for (int b = 0; b < 5; ++b) {
                if (a == b) continue;
                
                // min_val[parity_a][parity_b] stores min (P[a][i] - P[b][i])
                int min_val[2][2];
                for (int i = 0; i < 2; ++i)
                    for (int j = 0; j < 2; ++j)
                        min_val[i][j] = 1e9;
                
                int last_b_idx = -1;
                int processed_i = 0;
                
                for (int j = 1; j <= n; ++j) {
                    // Update the last seen position of character b to satisfy non-zero frequency
                    if (s[j - 1] - '0' == b) {
                        last_b_idx = j - 1;
                    }
                    
                    // Valid i must satisfy: i <= j - k AND i <= last_b_idx
                    int limit = min(j - k, last_b_idx);
                    
                    while (processed_i <= limit) {
                        int pa = P[a][processed_i] % 2;
                        int pb = P[b][processed_i] % 2;
                        int val = P[a][processed_i] - P[b][processed_i];
                        if (val < min_val[pa][pb]) {
                            min_val[pa][pb] = val;
                        }
                        processed_i++;
                    }
                    
                    // Target parities for P[a][i] and P[b][i] to ensure:
                    // (P[a][j] - P[a][i]) is odd  => P[a][i] parity != P[a][j] parity
                    // (P[b][j] - P[b][i]) is even => P[b][i] parity == P[b][j] parity
                    int target_pa = (P[a][j] % 2) ^ 1;
                    int target_pb = P[b][j] % 2;
                    
                    if (min_val[target_pa][target_pb] != 1e9) {
                        max_diff = max(max_diff, (P[a][j] - P[b][j]) - min_val[target_pa][target_pb]);
                    }
                }
            }
        }
        
        return max_diff;
    }
};
# @lc code=end