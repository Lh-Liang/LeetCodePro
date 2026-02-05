#
# @lc app=leetcode id=3630 lang=cpp
#
# [3630] Partition Array for Maximum XOR and AND
#
# @lc code=start
class Solution {
public:
    long long maximizeXorAndXor(vector<int>& nums) {
        int n = nums.size();
        long long ans = 0;
        function<void(int, long long, long long, bool, long long)> dfs = [&](int idx, long long xora, long long andb, bool hasB, long long xorc) {
            if (idx == n) {
                long long sum = xora + (hasB ? andb : 0) + xorc;
                ans = max(ans, sum);
                return;
            }
            // Assign nums[idx] to A
            dfs(idx+1, xora ^ nums[idx], andb, hasB, xorc);
            // Assign nums[idx] to B
            if (hasB)
                dfs(idx+1, xora, andb & nums[idx], true, xorc);
            else
                dfs(idx+1, xora, nums[idx], true, xorc);
            // Assign nums[idx] to C
            dfs(idx+1, xora, andb, hasB, xorc ^ nums[idx]);
        };
        dfs(0, 0, 0, false, 0);
        return ans;
    }
};
# @lc code=end