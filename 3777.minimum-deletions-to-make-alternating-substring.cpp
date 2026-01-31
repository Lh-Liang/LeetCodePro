#
# @lc app=leetcode id=3777 lang=cpp
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> minDeletions(string s, vector<vector<int>>& queries) {
        int n = s.length();
        vector<int> bit(n + 1, 0);

        auto update = [&](int idx, int val) {
            if (idx <= 0 || idx >= n) return;
            for (; idx < n; idx += idx & -idx)
                bit[idx] += val;
        };

        auto get_sum = [&](int idx) {
            int sum = 0;
            for (; idx > 0; idx -= idx & -idx)
                sum += bit[idx];
            return sum;
        };

        auto get_pair_val = [&](int i) {
            if (i < 0 || i >= n - 1) return 0;
            return (s[i] == s[i + 1]) ? 1 : 0;
        };

        // Initial BIT construction
        for (int i = 0; i < n - 1; ++i) {
            if (s[i] == s[i + 1]) {
                update(i + 1, 1);
            }
        }

        vector<int> results;
        for (const auto& q : queries) {
            if (q[0] == 1) {
                int j = q[1];
                // Indices affected are j-1 (pair j-1, j) and j (pair j, j+1)
                // We need to subtract old values and add new values
                
                // Handle pair (j-1, j)
                if (j > 0) {
                    update(j, -get_pair_val(j - 1));
                }
                // Handle pair (j, j+1)
                if (j < n - 1) {
                    update(j + 1, -get_pair_val(j));
                }

                s[j] = (s[j] == 'A' ? 'B' : 'A');

                if (j > 0) {
                    update(j, get_pair_val(j - 1));
                }
                if (j < n - 1) {
                    update(j + 1, get_pair_val(j));
                }
            } else {
                int l = q[1];
                int r = q[2];
                // Range sum of D[i] for i in [l, r-1]
                // BIT indices are [l+1, r]
                if (l >= r) {
                    results.push_back(0);
                } else {
                    results.push_back(get_sum(r) - get_sum(l));
                }
            }
        }

        return results;
    }
};
# @lc code=end