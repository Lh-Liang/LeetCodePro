# @lc app=leetcode id=3513 lang=cpp
#
# [3513] Number of Unique XOR Triplets I
#
# @lc code=start
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        // Since nums is a permutation of [1, n], all numbers from 0 to n-1 can be formed by XOR.
        return nums.size();
    }
};
# @lc code=end