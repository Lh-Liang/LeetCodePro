#
# @lc app=leetcode id=3670 lang=cpp
#
# [3670] Maximum Product of Two Integers With No Common Bits
#
# @lc code=start
class Solution {
public:
    long long maxProduct(vector<int>& nums) {
        long long maxProduct = 0;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if ((nums[i] & nums[j]) == 0) { // Check for no common bits
                    maxProduct = max(maxProduct, static_cast<long long>(nums[i]) * nums[j]);
                }
            }
        }
        return maxProduct;
    }
};
# @lc code=end