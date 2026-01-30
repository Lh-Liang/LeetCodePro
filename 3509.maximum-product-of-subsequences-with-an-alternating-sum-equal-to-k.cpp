#
# @lc app=leetcode id=3509 lang=cpp
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
#include <vector>
#include <bitset>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        const int offset = 1800;
        const int max_sum_idx = 3600;
        
        if (k < -offset || k > offset) return -1;

        // dp[sum_idx][parity]: parity 0 = even length, parity 1 = odd length
        // bitset stores possible products
        vector<array<bitset<5001>, 2>> dp(max_sum_idx + 1);

        for (int x : nums) {
            // Use a temporary update structure to avoid using the same element multiple times in one subsequence
            vector<pair<int, pair<int, bitset<5001>>>> updates;

            // Case 1: x starts a new subsequence (Index 0, Even index, result length 1/Odd)
            if (x <= limit) {
                bitset<5001> start_bs;
                start_bs.set(x);
                updates.push_back({x + offset, {1, start_bs}});
            }

            for (int s = 0; s <= max_sum_idx; ++s) {
                // Case 2: x is added at an even index (current length is even, parity 0)
                // New sum: s + x, new parity: 1 (odd length)
                if (dp[s][0].any()) {
                    int ns = s + x;
                    if (ns >= 0 && ns <= max_sum_idx) {
                        updates.push_back({ns, {1, transform(dp[s][0], x, limit)}});
                    }
                }

                // Case 3: x is added at an odd index (current length is odd, parity 1)
                // New sum: s - x, new parity: 0 (even length)
                if (dp[s][1].any()) {
                    int ns = s - x;
                    if (ns >= 0 && ns <= max_sum_idx) {
                        updates.push_back({ns, {0, transform(dp[s][1], x, limit)}});
                    }
                }
            }

            for (auto& upd : updates) {
                dp[upd.first][upd.second.first] |= upd.second.second;
            }
        }

        int target_idx = k + offset;
        for (int p = limit; p >= 0; --p) {
            if (dp[target_idx][0].test(p) || dp[target_idx][1].test(p)) {
                return p;
            }
        }

        return -1;
    }

private:
    bitset<5001> transform(const bitset<5001>& bs, int x, int limit) {
        bitset<5001> res;
        if (x == 0) {
            res.set(0);
        } else if (x == 1) {
            res = bs;
        } else {
            for (int p = 0; p <= limit / x; ++p) {
                if (bs.test(p)) res.set(p * x);
            }
        }
        return res;
    }
};
# @lc code=end