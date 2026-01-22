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
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        // For n >= 3, find the smallest power of 2 greater than n
        int k = 1;
        while (k <= n) {
            k <<= 1;
        }
        return k;
    }
};
# @lc code=end