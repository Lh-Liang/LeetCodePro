#
# @lc app=leetcode id=3729 lang=cpp
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#
# @lc code=start
class Solution {
public:
    long long numGoodSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        set<vector<int>> distinctSubarrays;
        
        for (int i = 0; i < n; i++) {
            long long sum = 0;
            for (int j = i; j < n; j++) {
                sum += nums[j];
                if (sum % k == 0) {
                    vector<int> subarray(nums.begin() + i, nums.begin() + j + 1);
                    distinctSubarrays.insert(subarray);
                }
            }
        }
        
        return distinctSubarrays.size();
    }
};
# @lc code=end