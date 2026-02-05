#
# @lc app=leetcode id=3510 lang=cpp
#
# [3510] Minimum Pair Removal to Sort Array II
#
# @lc code=start
class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int ops = 0;
        auto is_sorted = [](const vector<int>& arr) {
            for (int i = 1; i < arr.size(); ++i)
                if (arr[i] < arr[i-1]) return false;
            return true;
        };
        while (!is_sorted(nums)) {
            int min_sum = nums[0] + nums[1];
            int idx = 0;
            for (int i = 1; i < nums.size() - 1; ++i) {
                int s = nums[i] + nums[i+1];
                if (s < min_sum) {
                    min_sum = s;
                    idx = i;
                }
            }
            nums[idx] = nums[idx] + nums[idx+1];
            nums.erase(nums.begin() + idx + 1);
            ++ops;
        }
        return ops;
    }
};
# @lc code=end