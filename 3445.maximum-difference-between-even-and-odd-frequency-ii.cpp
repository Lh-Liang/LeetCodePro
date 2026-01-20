#
# @lc app=leetcode id=3445 lang=cpp
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.length();
        int max_diff = -1e9;

        // Precompute prefix sums for all digits '0'-'4'
        vector<vector<int>> pref(5, vector<int>(n, 0));
        for (int d = 0; d < 5; ++d) {
            int count = 0;
            for (int i = 0; i < n; ++i) {
                if (s[i] == (char)(d + '0')) count++;
                pref[d][i] = count;
            }
        }

        // Iterate over all pairs of distinct digits (a, b)
        // a: odd frequency, b: even frequency
        for (int a = 0; a < 5; ++a) {
            for (int b = 0; b < 5; ++b) {
                if (a == b) continue;

                // min_f[parity_a][parity_b] stores the minimum (pref_a - pref_b)
                // encountered so far for a given parity of prefix counts.
                vector<vector<int>> min_f(2, vector<int>(2, 1e9));
                int last_b = -1;
                int ptr = -1;

                for (int j = 0; j < n; ++j) {
                    if (s[j] == (char)(b + '0')) {
                        last_b = j;
                    }

                    // We need x <= j - k AND P_b(j) - P_b(x) > 0.
                    // P_b(j) - P_b(x) > 0 is satisfied if x < last_b.
                    // So we update min_f for all ptr <= min(j - k, last_b - 1).
                    while (ptr <= j - k && ptr < last_b) {
                        int cur_pa, cur_pb, cur_diff;
                        if (ptr == -1) {
                            cur_pa = 0; cur_pb = 0; cur_diff = 0;
                        } else {
                            cur_pa = pref[a][ptr] % 2;
                            cur_pb = pref[b][ptr] % 2;
                            cur_diff = pref[a][ptr] - pref[b][ptr];
                        }
                        min_f[cur_pa][cur_pb] = min(min_f[cur_pa][cur_pb], cur_diff);
                        ptr++;
                    }

                    // Current parities at index j
                    int pa = pref[a][j] % 2;
                    int pb = pref[b][j] % 2;
                    int diff = pref[a][j] - pref[b][j];

                    // We need: (pa - target_pa) % 2 == 1  => target_pa = 1 - pa
                    //          (pb - target_pb) % 2 == 0  => target_pb = pb
                    int target_pa = 1 - pa;
                    int target_pb = pb;

                    if (min_f[target_pa][target_pb] != 1e9) {
                        max_diff = max(max_diff, diff - min_f[target_pa][target_pb]);
                    }
                }
            }
        }

        return max_diff;
    }
};
# @lc code=end