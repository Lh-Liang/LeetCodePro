#
# @lc app=leetcode id=3640 lang=cpp
#
# [3640] Trionic Array II
#

# @lc code=start
class Solution {
public:
    long long maxSumTrionic(vector<int>& nums) {
        int n = nums.size();
        vector<long long> left(n), right(n);
        
        // Calculate increasing segments sum from left to right.
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[i - 1]) {
                left[i] = left[i - 1] + nums[i];
            } else {
                left[i] = nums[i];
            }
        }
        
        // Calculate increasing segments sum from right to left.
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] < nums[i + 1]) {
                right[i] = right[i + 1] + nums[i];
            } else {
                right[i] = nums[i];
            }
        }
        
        long long max_sum = LLONG_MIN;
        
        // Find maximum trionic subarray sum.
        for (int p = 1; p < n - 2; ++p) { // Ensure space for q and r after p.
            for (int q = p + 1; q < n - 1; ++q) { // Ensure space for r after q.
                if (nums[p] > nums[q]) { // Valid decreasing segment check.
                    for (int r = q + 1; r < n; ++r) { // Ensure valid r index.
                        if (right[q] > right[r]) continue; // Valid increasing segment check after q. 
                        long long current_sum = left[p-1] + nums[p] + nums[q] + nums[r-1]; 
                        max_sum = max(max_sum, current_sum); 
                    } 
                } 
            } 
        } 
    return max_sum; 
}
}; # @lc code=end