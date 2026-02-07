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
        int operations = 0;
        while (!nums.empty()) {
            // Check if all elements are distinct
            unordered_set<int> numSet(nums.begin(), nums.end());
            if (numSet.size() == nums.size()) break; // All elements are distinct
            // Remove first three elements or fewer if remaining size is less than three
            nums.erase(nums.begin(), nums.begin() + min(3, (int)nums.size()));
            operations++;
        }
        return operations;
    }
};
# @lc code=end