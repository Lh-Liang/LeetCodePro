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
        vector<int> inc_left(n, 1), dec_left(n, 1), inc_right(n, 1), dec_right(n, 1);
        vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) prefix[i + 1] = prefix[i] + nums[i];
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[i - 1]) inc_left[i] = inc_left[i - 1] + 1;
            if (nums[i] < nums[i - 1]) dec_left[i] = dec_left[i - 1] + 1;
        }
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] < nums[i + 1]) inc_right[i] = inc_right[i + 1] + 1;
            if (nums[i] > nums[i + 1]) dec_right[i] = dec_right[i + 1] + 1;
        }
        long long ans = LLONG_MIN;
        // Try all possible q as the valley point
        for (int q = 1; q < n - 1; ++q) {
            int dec_len = dec_left[q] - 1;
            if (dec_len < 1) continue;
            int p = q - dec_len;
            if (p <= 0) continue;
            int inc_len = inc_left[p - 1];
            if (inc_len < 1) continue;
            int l = p - inc_len;
            if (l < 0) continue;
            int inc2_len = inc_right[q];
            if (inc2_len < 2) continue; // at least one element after q
            int r = q + inc2_len - 1;
            if (r >= n) continue;
            // Use precomputed arrays, avoid redundant checks
            long long sum = prefix[r + 1] - prefix[l];
            ans = max(ans, sum);
        }
        return ans;
    }
};
# @lc code=end