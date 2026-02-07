#
# @lc app=leetcode id=3686 lang=cpp
#
# [3686] Number of Stable Subsequences
#
# @lc code=start
class Solution {
public:
    int countStableSubsequences(vector<int>& nums) {
        const int MOD = 1e9 + 7;
        int n = nums.size();
        vector<int> dp_odd(n + 1, 0), dp_even(n + 1, 0);
        // Base case initialization for first element
        if (nums[0] % 2 == 0) {
            dp_even[0] = 1;
        } else {
            dp_odd[0] = 1;
        }
        for (int i = 1; i < n; ++i) {
            if (nums[i] % 2 == 0) { // Even number
                dp_even[i] = (dp_even[i - 1] + dp_odd[i - 1]) % MOD;
                // Check for three consecutive evens
                if (i >= 2 && nums[i-1] % 2 == 0 && nums[i-2] % 2 == 0) {
                    dp_even[i] = (dp_even[i] - dp_even[i-2] + MOD) % MOD;
                }
            } else { // Odd number
                dp_odd[i] = (dp_odd[i - 1] + dp_even[i - 1]) % MOD;
                // Check for three consecutive odds
                if (i >= 2 && nums[i-1] % 2 != 0 && nums[i-2] % 2 != 0) {
                    dp_odd[i] = (dp_odd[i] - dp_odd[i-2] + MOD) % MOD;
                }
            }
        }
        long long total_stable_subsequences = accumulate(dp_odd.begin(), dp_odd.end(), static_cast<long long>(0)) \
                                           + accumulate(dp_even.begin(), dp_even.end(), static_cast<long long>(0));
        total_stable_subsequences %= MOD;
        return total_stable_subsequences; // Return total valid subsequences.
    }
};
# @lc code=end