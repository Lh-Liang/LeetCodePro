#
# @lc app=leetcode id=3776 lang=cpp
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
class Solution {
public:
    long long minMoves(vector<int>& balance) {
        int n = balance.size();
        int k = -1;
        long long total = 0;
        long long deficit = 0;
        for (int i = 0; i < n; ++i) {
            total += balance[i];
            if (balance[i] < 0) {
                k = i;
                deficit = - (long long)balance[i];
            }
        }
        if (k == -1) return 0;
        if (total < 0) return -1;
        vector<long long> cap(n + 1, 0LL);
        for (int i = 0; i < n; ++i) {
            if (i == k) continue;
            int diff = abs(i - k);
            int d = min(diff, n - diff);
            cap[d] += (long long)balance[i];
        }
        long long ans = 0;
        long long rem = deficit;
        for (int d = 1; d < n; ++d) {
            if (cap[d] == 0 || rem == 0) continue;
            long long take = min(rem, cap[d]);
            ans += take * d;
            rem -= take;
        }
        return ans;
    }
};
# @lc code=end