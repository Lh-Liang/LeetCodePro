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
        int target_count = 0;
        vector<int> prefix(n + 1, 0);
        unordered_map<int, int> count_map;
        count_map[0] = 1; // To handle cases where prefix itself is valid
        long long result = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == target) {
                ++target_count;
            }
            // Calculate current prefix sum difference
            int current_diff = 2 * target_count - (i + 1); // More than half condition converted to linear form
            // Check if there's a previous prefix with same difference that can create a valid subarray here
            if (count_map.find(current_diff) != count_map.end()) {
                result += count_map[current_diff]; 
            }
            // Store/update current prefix difference in map for future subarrays ending at later points
            ++count_map[current_diff]; 
        } 
        return result; 
    } 
}; 
# @lc code=end