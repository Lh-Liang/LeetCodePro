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
        if (n < 4) return LLONG_MIN;
        vector<long long> leftInc(n, 0), rightDec(n, 0);
        vector<long long> rightInc(n, 0), leftDec(n, 0);
        
        // Calculate strictly increasing sequences sums from left to right
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[i - 1]) {
                leftInc[i] = leftInc[i - 1] + nums[i];
            } else {
                leftInc[i] = nums[i];
            }
            
            if (nums[n - i - 1] < nums[n - i]) {
                rightDec[n - i - 1] = rightDec[n - i] + nums[n - i - 1];
            } else {
                rightDec[n - i - 1] = nums[n - i - 1];
            }
        }

        // Calculate strictly decreasing sequence sums from right to left
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] > nums[i + 1]) {
                rightInc[i] = rightInc[i + 1] + nums[i];
            } else {
                rightInc[i] = nums[i];
            }

            if (nums[n - i - 2] < nums[n - i - 3]) {
                leftDec[n - i - 2] = leftDec[n - i - 3] + nums[n - i - 2];
            } else {
                leftDec[n - i - 2] = nums[n - i - 2];
            }
        }

        long long max_sum = LLONG_MIN;
        // Find maximum sum of trionic subarray using precomputed arrays
        for (int p = 2; p < n-2; ++p) { // Middle point p must allow space for l and r
            if (leftInc[p-1] > nums[p-1] && rightDec[p+1] > nums[p+1]) { // Ensure valid configuration
                long long current_sum = leftInc[p-1] + nums[p-1]+rightDec[p+1];
                max_sum = max(max_sum, current_sum);
            }
        }

        return max_sum;
    }
};
# @lc code=end