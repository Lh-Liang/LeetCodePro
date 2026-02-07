#
# @lc app=leetcode id=3509 lang=cpp
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        int max_product = -1;
        // Iterate through all possible subsets
        int n = nums.size();
        for (int mask = 1; mask < (1 << n); ++mask) {
            int alt_sum = 0;
            int product = 1;
            bool valid = true;
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) {
                    if ((product *= nums[i]) > limit) {
                        valid = false; // Product exceeds limit, break early.
                        break;
                    }
                    alt_sum += (i % 2 == 0 ? nums[i] : -nums[i]);
                }
            }
            if (valid && alt_sum == k) {
                max_product = max(max_product, product);
            }
        }
        return max_product; // Return maximum product found or -1 if none.
    }
};
# @lc code=end