#
# @lc app=leetcode id=3509 lang=cpp
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#
# @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        // dp[sum][parity] = max product
        // use unordered_map for sum: (sum, parity) => max product
        using Key = pair<int, int>;
        struct KeyHash { size_t operator()(const Key& p) const { return hash<int>()(p.first) ^ hash<int>()(p.second << 1); } };
        unordered_map<Key, int, KeyHash> dp, ndp;
        int n = nums.size();
        int ans = -1;
        for (int i = 0; i < n; ++i) {
            ndp = dp;
            // Start new subsequence with nums[i]
            int sum0 = nums[i];
            int prod0 = nums[i];
            if (prod0 <= limit) {
                Key key0 = {sum0, 1}; // first element is at even index (0), next will be odd (1)
                ndp[key0] = max(ndp[key0], prod0);
                if (sum0 == k) ans = max(ans, prod0);
            }
            // Extend all existing subsequences
            for (const auto& it : dp) {
                int sum = it.first.first;
                int parity = it.first.second;
                int prod = it.second;
                int nsum, nprod;
                if (parity == 0) {
                    nsum = sum + nums[i];
                } else {
                    nsum = sum - nums[i];
                }
                nprod = prod * nums[i];
                if (nprod > limit) continue;
                Key nkey = {nsum, 1 - parity};
                ndp[nkey] = max(ndp[nkey], nprod);
                if (nsum == k) ans = max(ans, nprod);
            }
            swap(dp, ndp);
        }
        return ans;
    }
};
# @lc code=end