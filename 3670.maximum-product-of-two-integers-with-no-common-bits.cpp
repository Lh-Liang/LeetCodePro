#
# @lc app=leetcode id=3670 lang=cpp
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    long long maxProduct(std::vector<int>& nums) {
        // nums[i] <= 10^6, so we need bits up to 2^19. 20 bits (0 to 2^20 - 1) cover up to 1,048,575.
        const int BITS = 20;
        const int LIMIT = 1 << BITS;
        
        // g[mask] will store the maximum value in nums that is a submask of 'mask'.
        // Using a vector of size 2^20 (approx 4MB).
        std::vector<int> g(LIMIT, 0);
        for (int x : nums) {
            if (x > g[x]) {
                g[x] = x;
            }
        }
        
        // SOS DP (Sum Over Subsets) variation: Max Over Subsets.
        // After this, g[mask] = max(nums[j]) for all nums[j] such that (nums[j] & mask) == nums[j].
        for (int i = 0; i < BITS; ++i) {
            int bit = 1 << i;
            for (int mask = 0; mask < LIMIT; ++mask) {
                if (mask & bit) {
                    g[mask] = std::max(g[mask], g[mask ^ bit]);
                }
            }
        }
        
        long long max_p = 0;
        const int full_mask = LIMIT - 1;
        
        // For each number x, the condition (x & y) == 0 means y must be a submask of ~x.
        for (int x : nums) {
            int complement = full_mask ^ x;
            // g[complement] gives the largest value in nums that shares no bits with x.
            if (g[complement] > 0) {
                long long current_prod = (long long)x * g[complement];
                if (current_prod > max_p) {
                    max_p = current_prod;
                }
            }
        }
        
        return max_p;
    }
};
# @lc code=end