#
# @lc app=leetcode id=3670 lang=cpp
#
# [3670] Maximum Product of Two Integers With No Common Bits
#
# @lc code=start
class Solution {
public:
    long long maxProduct(vector<int>& nums) {
        vector<pair<int, int>> bitmasks; // To store number and its bitmask
        long long maxProduct = 0;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            int num = nums[i];
            int bitmask = 0;
            for (int j = 0; j < 31; ++j) { // Assuming numbers up to 10^6 which fits in 31 bits
                if (num & (1 << j)) {
                    bitmask |= (1 << j);
                }
            }
            for (const auto& [storedNum, storedBitmask] : bitmasks) {
                if ((bitmask & storedBitmask) == 0) { // no common set bits
                    maxProduct = max(maxProduct, (long long)num * storedNum);
                }
            }
            // Store the current number and its calculated bitmask for future checks
            bitmasks.emplace_back(num, bitmask);
        }
        return maxProduct;
    }
};
# @lc code=end