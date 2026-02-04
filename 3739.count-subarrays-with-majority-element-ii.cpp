#
# @lc app=leetcode id=3739 lang=cpp
#
# [3739] Count Subarrays With Majority Element II
#
# @lc code=start
class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();
        long long result = 0;
        unordered_map<int, int> prefixCount;
        prefixCount[0] = 1;
        int currentCount = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == target) {
                currentCount++;
            } else {
                currentCount--;
            }
            if (prefixCount.find(currentCount - 1) != prefixCount.end()) {
                result += prefixCount[currentCount - 1];
            }
            prefixCount[currentCount]++;
        }
        return result;
    }
};
# @lc code=end