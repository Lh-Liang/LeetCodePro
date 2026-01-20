#
# @lc app=leetcode id=3509 lang=cpp
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
#include <vector>
#include <bitset>
#include <cmath>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        long long sum_vals = 0;
        for(int x : nums) sum_vals += x;
        // The alternating sum cannot exceed the sum of absolute values of elements.
        if (abs(k) > sum_vals) return -1;

        const int OFFSET = 2000;
        // dp[product][parity]
        // parity 0: next element will be added (even index in subsequence)
        // parity 1: next element will be subtracted (odd index in subsequence)
        // We use bitsets to track reachable alternating sums.
        // Size 4002 is sufficient since max sum is ~1800 and min is ~-1800.
        vector<vector<bitset<4002>>> dp(limit + 1, vector<bitset<4002>>(2));

        // Base case: empty subsequence has product 1, sum 0, and next sign is +
        dp[1][0][OFFSET] = 1;

        int count_ones = 0;
        bool has_zero = false;
        vector<int> non_zero_nums;
        for(int x : nums) {
            if(x == 0) has_zero = true;
            else {
                non_zero_nums.push_back(x);
                if(x == 1) count_ones++;
            }
        }

        for(int x : non_zero_nums) {
            if (x == 1) {
                // For x=1, product p stays p. We update states based on previous states at same p.
                for(int p = 1; p <= limit; ++p) {
                    bitset<4002> old_0 = dp[p][0];
                    bitset<4002> old_1 = dp[p][1];
                    // Transition from state 0 (next +) -> state 1 (next -), sum increases by 1
                    dp[p][1] |= (old_0 << 1);
                    // Transition from state 1 (next -) -> state 0 (next +), sum decreases by 1
                    dp[p][0] |= (old_1 >> 1);
                }
            } else {
                // For x > 1, product increases. Iterate downwards to avoid using same element multiple times.
                for(int p = limit / x; p >= 1; --p) {
                    int np = p * x;
                    // Transition from state 0 (next +) -> state 1 (next -), sum increases by x
                    dp[np][1] |= (dp[p][0] << x);
                    // Transition from state 1 (next -) -> state 0 (next +), sum decreases by x
                    dp[np][0] |= (dp[p][1] >> x);
                }
            }
        }

        int target_idx = k + OFFSET;
        // Check products from limit down to 2
        for(int p = limit; p >= 2; --p) {
            if (dp[p][0].test(target_idx) || dp[p][1].test(target_idx)) {
                return p;
            }
        }

        // Check product 1
        // Product 1 is only possible with a sequence of 1s.
        // Alternating sum of 1s is 1 (odd length) or 0 (even length).
        if (k == 0) {
            // Need at least two 1s for sum 0 (e.g. 1-1=0)
            if (count_ones >= 2) return 1;
        } else if (k == 1) {
            // Need at least one 1 for sum 1
            if (count_ones >= 1) return 1;
        }

        // Check product 0
        // If we have a zero, we can achieve product 0.
        // We need to check if sum k is achievable with ANY subsequence of nums (including 0s).
        if (has_zero) {
            bitset<4002> r[2];
            r[0][OFFSET] = 1;
            
            for(int x : nums) {
                bitset<4002> next_r0 = r[0];
                bitset<4002> next_r1 = r[1];
                
                if (x == 0) {
                    // 0 allows switching parity without changing sum
                    next_r0 |= r[1];
                    next_r1 |= r[0];
                } else {
                    next_r1 |= (r[0] << x);
                    next_r0 |= (r[1] >> x);
                }
                r[0] = next_r0;
                r[1] = next_r1;
            }
            
            if (r[0].test(target_idx) || r[1].test(target_idx)) {
                return 0;
            }
        }

        return -1;
    }
};
# @lc code=end