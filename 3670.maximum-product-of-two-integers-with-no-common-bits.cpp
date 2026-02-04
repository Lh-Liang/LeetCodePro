#
# @lc app=leetcode id=3670 lang=cpp
#
# [3670] Maximum Product of Two Integers With No Common Bits
#
# @lc code=start
class Solution {
public:
    long long maxProduct(vector<int>& nums) {
        // Step 1: Map bitmask to the largest number with that mask
        unordered_map<int, int> mask_max;
        for (int num : nums) {
            int mask = num;
            if (mask_max.count(mask)) {
                mask_max[mask] = max(mask_max[mask], num);
            } else {
                mask_max[mask] = num;
            }
        }
        // Step 2: Collect unique (mask, max_value) pairs
        vector<pair<int, int>> v;
        for (auto& [mask, val] : mask_max) {
            v.emplace_back(mask, val);
        }
        // Step 3: Compare all pairs for disjoint masks
        long long res = 0;
        int n = v.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if ((v[i].first & v[j].first) == 0) {
                    res = max(res, 1LL * v[i].second * v[j].second);
                }
            }
        }
        // Step 4: Return the result
        return res;
    }
};
# @lc code=end