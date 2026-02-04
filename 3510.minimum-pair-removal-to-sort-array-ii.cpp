# @lc app=leetcode id=3510 lang=cpp
#
# [3510] Minimum Pair Removal to Sort Array II
#
# @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int operations = 0;
        int i = 0;
        while (i < nums.size() - 1) {
            if (nums[i] > nums[i + 1]) {
                // Replace current and next element with their sum
                nums[i] += nums[i + 1];
                nums.erase(nums.begin() + i + 1);
                ++operations;
                // After modification, check if we need to step back
                if (i > 0) --i;
            } else {
                ++i;
            }
        }
        return operations;
    }
};
# @lc code=end