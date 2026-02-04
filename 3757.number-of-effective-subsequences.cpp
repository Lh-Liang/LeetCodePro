#
# @lc app=leetcode id=3757 lang=cpp
#
# [3757] Number of Effective Subsequences
#
# @lc code=start
class Solution {
public:
    int countEffective(vector<int>& nums) {
        const int MOD = 1e9 + 7;
        int total_or = 0;
        for (int num : nums) {
            total_or |= num;
        }
        std::unordered_map<int, int> element_count;
        for (int num : nums) {
            element_count[num]++;
        }
        int result = 0;
        for (const auto& [element, count] : element_count) {
            if ((total_or & ~element) < total_or) {
                result = (result + (1 << count) - 1) % MOD;
            }
        }
        return result;
    }
};
# @lc code=end