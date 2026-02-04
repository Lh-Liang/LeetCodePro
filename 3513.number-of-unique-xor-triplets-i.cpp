#
# @lc app=leetcode id=3513 lang=cpp
#
# [3513] Number of Unique XOR Triplets I
#

# @lc code=start
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        unordered_set<int> unique_xors;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                for (int k = j; k < n; ++k) {
                    int xor_value = nums[i] ^ nums[j] ^ nums[k];
                    unique_xors.insert(xor_value);
                }
            }
        }
        return unique_xors.size();
    }
};
# @lc code=end