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
        vector<int> even(n + 1), odd(n + 1);
        even[0] = odd[0] = 1; // Base case: empty subsequence
        for (int i = 0; i < n; ++i) {
            if (nums[i] % 2 == 0) { // Current number is even
                even[i + 1] = (even[i] + odd[i]) % MOD;
                odd[i + 1] = odd[i]; // No change in odd count as no new odd is added
            } else { // Current number is odd
                odd[i + 1] = (even[i] + odd[i]) % MOD;
                even[i + 1] = even[i]; // No change in even count as no new even is added
            }
        }
        return (even[n] + odd[n] - 1) % MOD; // Subtracting 1 to exclude empty subsequence
    }
};
# @lc code=end