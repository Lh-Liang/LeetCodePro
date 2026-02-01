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
        vector<vector<int>> P(n + 1, vector<int>(5, 0));
        for (int i = 0; i < n; ++i) {
            for (int c = 0; c < 5; ++c) {
                P[i + 1][c] = P[i][c];
            }
            P[i + 1][s[i] - '0']++;
        }

        int max_diff = -1e9;

        for (int a = 0; a < 5; ++a) {
            for (int b = 0; b < 5; ++b) {
                if (a == b) continue;

                vector<vector<int>> min_val(2, vector<int>(2, 1e9));
                int processed_until = -1;
                int last_b_idx = -1;

                for (int j = 0; j <= n; ++j) {
                    int limit = min(j - k, last_b_idx);
                    
                    while (processed_until < limit) {
                        processed_until++;
                        int i = processed_until;
                        int pa = P[i][a] & 1;
                        int pb = P[i][b] & 1;
                        min_val[pa][pb] = min(min_val[pa][pb], P[i][a] - P[i][b]);
                    }

                    int target_pa = 1 - (P[j][a] & 1);
                    int target_pb = P[j][b] & 1;
                    
                    if (min_val[target_pa][target_pb] != 1e9) {
                        max_diff = max(max_diff, (P[j][a] - P[j][b]) - min_val[target_pa][target_pb]);
                    }

                    if (j < n && (s[j] - '0') == b) {
                        last_b_idx = j;
                    }
                }
            }
        }

        return max_diff;
    }
};
# @lc code=end