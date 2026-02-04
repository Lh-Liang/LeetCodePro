#
# @lc app=leetcode id=3762 lang=cpp
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

class Solution {
public:
    vector<long long> minOperations(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int n = nums.size();
        int q = queries.size();
        // Precompute prefix sums of remainders modulo k for quick congruence checks
        vector<vector<int>> rem_counts(k, vector<int>(n + 1, 0));
        for (int i = 0; i < n; ++i) {
            int rem = nums[i] % k;
            for (int j = 0; j < k; ++j) {
                rem_counts[j][i + 1] = rem_counts[j][i];
            }
            rem_counts[rem][i + 1]++;
        }

        // Precompute base values for each nums[i]
        vector<int> bases(n);
        for (int i = 0; i < n; ++i) {
            bases[i] = nums[i] / k;
        }

        vector<long long> ans(q);
        for (int idx = 0; idx < q; ++idx) {
            int l = queries[idx][0], r = queries[idx][1];
            int len = r - l + 1;
            // Step 2: Check if all elements in the subarray have the same remainder modulo k
            int rem = nums[l] % k;
            int cnt = rem_counts[rem][r + 1] - rem_counts[rem][l];
            // Step 3: Explicitly verify the assumption
            bool valid = (cnt == len);
            if (!valid) {
                ans[idx] = -1;
                continue;
            }
            // Step 4: Get base values
            vector<int> sub_bases(bases.begin() + l, bases.begin() + r + 1);
            // Step 5: Find median
            nth_element(sub_bases.begin(), sub_bases.begin() + len / 2, sub_bases.end());
            int median = sub_bases[len / 2];
            // Step 6: Calculate sum of absolute differences
            long long ops = 0;
            for (int b : sub_bases) ops += abs(b - median);
            // Step 7: Verification step (implicit in logic)
            ans[idx] = ops;
        }
        return ans;
    }
};
# @lc code=end