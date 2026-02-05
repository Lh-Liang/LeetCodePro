#
# @lc app=leetcode id=3670 lang=cpp
#
# [3670] Maximum Product of Two Integers With No Common Bits
#
# @lc code=start
class Solution {
public:
    long long maxProduct(vector<int>& nums) {
        unordered_map<int, int> bitmask_max;
        for (int num : nums) {
            int bm = num;
            if (bitmask_max.count(bm))
                bitmask_max[bm] = max(bitmask_max[bm], num);
            else
                bitmask_max[bm] = num;
        }
        vector<pair<int, int>> masks;
        for (auto& p : bitmask_max) {
            masks.push_back({p.first, p.second});
        }
        long long res = 0;
        int n = masks.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if ((masks[i].first & masks[j].first) == 0) {
                    res = max(res, 1LL * masks[i].second * masks[j].second);
                }
            }
        }
        return res;
    }
};
# @lc code=end