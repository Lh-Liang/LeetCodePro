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
        // Memoization: key=(i, alt_sum, parity), value=max product
        int n = nums.size();
        // The key is (i, current alternating sum, parity)
        // To reduce state size, product only tracked if <=limit
        unordered_map<long long, int> dp[151];
        int ans = -1;
        function<void(int,int,long long,int)> dfs = [&](int idx, int alt_sum, long long prod, int parity) {
            if (prod > limit) return;
            if (idx == n) {
                // Only non-empty subsequences
                if (alt_sum == k && prod > ans && prod > 0) ans = prod;
                return;
            }
            // State key
            long long key = ((long long)(alt_sum + 105) << 1) | parity;
            if (dp[idx].count(key) && dp[idx][key] >= prod) return;
            dp[idx][key] = prod;
            // Exclude current
            dfs(idx+1, alt_sum, prod, parity);
            // Include current
            int nalt = parity ? alt_sum - nums[idx] : alt_sum + nums[idx];
            long long nprod = prod * nums[idx];
            dfs(idx+1, nalt, nprod, 1-parity);
        };
        // Try all possible starting points (subsequences can be any length)
        for (int i=0;i<n;++i) {
            if (nums[i] > 0)
                dfs(i+1, nums[i], nums[i], 1); // Start with nums[i] at even pos
        }
        // Handle zeros as well (if nums[i]==0 and k==0)
        for (int i=0;i<n;++i) {
            if (nums[i]==0 && k==0 && 0<=limit) ans = max(ans, 0);
        }
        return ans;
    }
};
# @lc code=end