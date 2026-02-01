#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        const int offset = 1800;
        const int range = 3601;
        // dp[parity][sum] where parity 0 = even length, 1 = odd length
        // We use bitset<5001> to store possible products.
        vector<vector<bitset<5001>>> dp(2, vector<bitset<5001>>(range));

        int min_s = offset, max_s = offset;

        for (int x : nums) {
            vector<vector<bitset<5001>>> next_dp = dp;
            
            // Start a new subsequence (length 1, so parity is odd/1)
            if (x <= limit) {
                next_dp[1][offset + x].set(x);
            }

            for (int s = min_s; s <= max_s; ++s) {
                // Extend even length to odd length (Add x)
                if (dp[0][s].any()) {
                    int ns = s + x;
                    if (ns >= 0 && ns < range) {
                        if (x == 0) next_dp[1][ns].set(0);
                        else if (x == 1) next_dp[1][ns] |= dp[0][s];
                        else {
                            for (int p = 0; p <= limit / x; ++p) {
                                if (dp[0][s].test(p)) next_dp[1][ns].set(p * x);
                            }
                        }
                    }
                }
                // Extend odd length to even length (Subtract x)
                if (dp[1][s].any()) {
                    int ns = s - x;
                    if (ns >= 0 && ns < range) {
                        if (x == 0) next_dp[0][ns].set(0);
                        else if (x == 1) next_dp[0][ns] |= dp[1][s];
                        else {
                            for (int p = 0; p <= limit / x; ++p) {
                                if (dp[1][s].test(p)) next_dp[0][ns].set(p * x);
                            }
                        }
                    }
                }
            }
            dp = move(next_dp);
            min_s = max(0, min_s - x);
            max_s = min(range - 1, max_s + x);
        }

        int target_s = k + offset;
        if (target_s < 0 || target_s >= range) return -1;

        int best = -1;
        for (int p = limit; p >= 0; --p) {
            if (dp[0][target_s].test(p) || dp[1][target_s].test(p)) {
                return p;
            }
        }
        return -1;
    }
};