#
# @lc app=leetcode id=3513 lang=cpp
#
# [3513] Number of Unique XOR Triplets I
#
# @lc code=start
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        unordered_set<int> uniqueXorValues;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            int xorValue = 0;
            for (int j = i; j < n; ++j) {
                xorValue ^= nums[j];
                uniqueXorValues.insert(xorValue);
            }
        }
        return uniqueXorValues.size();
    }
};
# @lc code=end