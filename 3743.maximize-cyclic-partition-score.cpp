#
# @lc app=leetcode id=3743 lang=cpp
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
class Solution {
public:
    long long maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> dp(k + 1);
        vector<int> extendedNums(nums.begin(), nums.end());
        extendedNums.insert(extendedNums.end(), nums.begin(), nums.end());
        long long maxScore = 0;
        for (int i = 0; i < n; ++i) {
            vector<long long> currentDp(k + 1);
            int minVal = extendedNums[i], maxVal = extendedNums[i];
            for (int j = i; j < i + n && j < extendedNums.size(); ++j) {
                minVal = min(minVal, extendedNums[j]);
                maxVal = max(maxVal, extendedNums[j]);
                int range = maxVal - minVal;
                for (int p = k; p >= 1; --p) {
                    currentDp[p] = max(currentDp[p], dp[p - 1] + range);
                }
            }
            dp.swap(currentDp);
        }
        return *max_element(dp.begin(), dp.end());
    }
};