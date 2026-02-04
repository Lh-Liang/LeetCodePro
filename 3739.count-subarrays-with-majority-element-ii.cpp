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
        unordered_map<int, int> balance_count; // Track occurrences of each balance
        int balance = 0; // Balance of target occurrences minus non-target occurrences
        balance_count[0] = 1; // Initial state: zero balance has one occurrence
        long long result = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == target) {
                balance += 1;
            } else {
                balance -= 1;
            }
            // Check if there exists a previous state where the adjusted balance indicates majority
            result += balance_count[balance - 1];
            // Update current balance occurrence in map
            balance_count[balance] += 1;
        }
        return result;
    }
};
# @lc code=end