#
# @lc app=leetcode id=3445 lang=cpp
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.length();
        vector<vector<int>> prefix(5, vector<int>(n + 1, 0));
        for (int i = 0; i < n; ++i) {
            for (int d = 0; d < 5; ++d) {
                prefix[d][i + 1] = prefix[d][i] + (s[i] - '0' == d);
            }
        }

        int max_diff = INT_MIN;

        for (int a = 0; a < 5; ++a) {
            for (int b = 0; b < 5; ++b) {
                if (a == b) continue;

                // min_satisfied[parity_a][parity_b] stores min(prefix[a][j] - prefix[b][j])
                // for j that satisfy: j <= i-k AND s[j...i-1] contains at least one 'b'
                vector<vector<int>> min_satisfied(2, vector<int>(2, 1e9));
                int p = 0; 
                int last_b_idx = -1;

                for (int i = 1; i <= n; ++i) {
                    if (s[i - 1] - '0' == b) last_b_idx = i - 1;

                    // Condition: j <= i - k AND j <= last_b_idx
                    int limit = min(i - k, last_b_idx);
                    while (p <= limit) {
                        int pa = prefix[a][p] % 2;
                        int pb = prefix[b][p] % 2;
                        int diff = prefix[a][p] - prefix[b][p];
                        if (diff < min_satisfied[pa][pb]) {
                            min_satisfied[pa][pb] = diff;
                        }
                        p++;
                    }

                    // Current parities at i
                    int cur_pa = prefix[a][i] % 2;
                    int cur_pb = prefix[b][i] % 2;

                    // We need freq_a = odd -> prefix[a][i] - prefix[a][j] % 2 == 1
                    // So target_pa = 1 - cur_pa (if cur_pa is 0, we need 1; if 1, we need 0)
                    // We need freq_b = even -> prefix[b][i] - prefix[b][j] % 2 == 0
                    // So target_pb = cur_pb
                    int target_pa = 1 - cur_pa;
                    int target_pb = cur_pb;

                    if (min_satisfied[target_pa][target_pb] != 1e9) {
                        int current_total_diff = (prefix[a][i] - prefix[b][i]) - min_satisfied[target_pa][target_pb];
                        if (current_total_diff > max_diff) {
                            max_diff = current_total_diff;
                        }
                    }
                }
            }
        }

        return max_diff;
    }
};
# @lc code=end