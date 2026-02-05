#
# @lc app=leetcode id=3513 lang=cpp
#
# [3513] Number of Unique XOR Triplets I
#

# @lc code=start
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        int n = nums.size();
        set<int> unique;
        for (int i = 0; i < n; ++i) {
            int x = 0;
            for (int j = i; j < n; ++j) {
                for (int k = j; k < n; ++k) {
                    int val = nums[i] ^ nums[j] ^ nums[k];
                    unique.insert(val);
                }
            }
        }
        return unique.size();
    }
};
# @lc code=end