#
# @lc app=leetcode id=3509 lang=cpp
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        // Implement backtracking to generate subsequences
        function<void(int, vector<int>&)> backtrack = [&](int start, vector<int>& path) {
            int altSum = 0, prod = 1;
            for (int i = 0; i < path.size(); ++i) {
                if (i % 2 == 0) altSum += path[i];
                else altSum -= path[i];
                prod *= path[i];
                if (prod > limit) return; // Early stop if product exceeds limit
            }
            if (altSum == k) maxProd = max(maxProd, prod);
            for (int i = start; i < nums.size(); ++i) {
                path.push_back(nums[i]);
                backtrack(i + 1, path);
                path.pop_back();
            }
        };
        int maxProd = -1; // Initialize with -1 as per problem statement when no valid subsequence exists.
        vector<int> path; // Current sequence being explored.
        backtrack(0, path); // Start backtracking from index 0.
        return maxProd; // Return maximum found or -1 if none found. 
    } 
}; 
# @lc code=end