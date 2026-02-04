#
# @lc app=leetcode id=3670 lang=cpp
#
# [3670] Maximum Product of Two Integers With No Common Bits
#
# @lc code=start
class Solution {
public:
    long long maxProduct(vector<int>& nums) {
        vector<pair<int, int>> num_bitmask_pairs;
        
        // Step 1: Compute bitmask for each number
        for (int num : nums) {
            int bitmask = 0;
            int temp = num;
            int pos = 0; // Correct position tracking
            // Traverse through bits of the number
            while (temp > 0) {
                if (temp & 1) {
                    bitmask |= (1 << pos);
                }
                temp >>= 1;
                ++pos;
            }
            num_bitmask_pairs.push_back({num, bitmask});
        }
        
        long long max_product = 0;
        // Step 3: Check all pairs of numbers
        for (size_t i = 0; i < num_bitmask_pairs.size(); ++i) {
            for (size_t j = i + 1; j < num_bitmask_pairs.size(); ++j) {
                // Step 3: Ensure no common set bits
                if ((num_bitmask_pairs[i].second & num_bitmask_pairs[j].second) == 0) {
                    // Step 4: Calculate product and update maximum product
                    max_product = max(max_product, static_cast<long long>(num_bitmask_pairs[i].first) * num_bitmask_pairs[j].first);
                }
            }
        }
        return max_product;
    }
};
# @lc code=end