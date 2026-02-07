#
# @lc app=leetcode id=3739 lang=cpp
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();
        long long count = 0;
        unordered_map<int, int> prefix_count;
        prefix_count[0] = 1; // Base case for zero difference.
        int diff = 0; // To track number of targets over non-targets.
        for (int i = 0; i < n; ++i) {
            if (nums[i] == target) diff++; 
            else diff--; 
            // Check if there is a previous point where the same diff occurred.
            if (diff > 0) { 
                count += prefix_count[diff]; 
            } else { 
                count += prefix_count[diff - 1]; 
            }
            // Update map with current diff.
prefix_count[diff]++; " }