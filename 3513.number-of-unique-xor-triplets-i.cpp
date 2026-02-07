#
# @lc app=leetcode id=3513 lang=cpp
#
# [3513] Number of Unique XOR Triplets I
#

# @lc code=start
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        unordered_set<int> xor_values;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                int xor_val = nums[i];
                for (int k = j; k < n; ++k) {
                    xor_val ^= nums[k];
                    xor_values.insert(xor_val);
                }
            }
        }
        return xor_values.size();
    }
};
# @lc code=end