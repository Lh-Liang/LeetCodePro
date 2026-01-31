#
# @lc app=leetcode id=3779 lang=cpp
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> seen;
        int s = n; // s will store the starting index of the longest distinct suffix
        
        // Iterate backwards to find the longest suffix with unique elements
        for (int i = n - 1; i >= 0; --i) {
            if (seen.count(nums[i])) {
                // Duplicate found; the distinct suffix cannot extend further left
                break;
            }
            seen.insert(nums[i]);
            s = i;
        }
        
        // We need to remove elements such that the new start index (3 * k) is >= s.
        // The smallest k satisfying 3k >= s is ceil(s / 3).
        return (s + 2) / 3;
    }
};
# @lc code=end