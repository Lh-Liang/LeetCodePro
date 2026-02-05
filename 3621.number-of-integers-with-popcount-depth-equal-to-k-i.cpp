#
# @lc app=leetcode id=3621 lang=cpp
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#
# @lc code=start
#include <vector>
using namespace std;
class Solution {
public:
    int pop_depth(int x) {
        int d = 0;
        while (x > 1) {
            int cnt = 0, t = x;
            while (t) { cnt += t & 1; t >>= 1; }
            x = cnt;
            d++;
        }
        return d;
    }
    // count numbers <= n with exactly k ones
    long long count_ones(long long n, int ones) {
        vector<int> bits;
        while (n) { bits.push_back(n & 1); n >>= 1; }
        int L = bits.size();
        vector<vector<long long>> dp(L+1, vector<long long>(ones+2, 0));
        dp[L][0] = 1;
        for (int i = L-1; i >= 0; --i) {
            for (int cnt = 0; cnt <= ones; ++cnt) {
                // Place 0 at this bit
                dp[i][cnt] += dp[i+1][cnt];
                // Place 1 if bits[i] == 1 or less
                if (cnt < ones) {
                    if (bits[i])
                        dp[i][cnt+1] += dp[i+1][cnt];
                    else
                        dp[i][cnt+1] += 0;
                }
            }
            // Fix overflow
            for (int cnt = 0; cnt <= ones+1; ++cnt)
                if (dp[i][cnt] < 0) dp[i][cnt] = 0;
        }
        long long res = 0;
        for (int i = 0; i < L; ++i) {
            if (ones < 0) break;
            if (bits[i]) {
                res += comb(L-1-i, ones);
                ones--;}
        }
        if (ones == 0) res++;
        return res;
    }
    long long comb(int n, int k) {
        if (k < 0 || k > n) return 0;
        long long res = 1;
        for (int i = 1; i <= k; ++i)
            res = res * (n-i+1) / i;
        return res;
    }
    long long popcountDepth(long long n, int k) {
        if (n == 0) return 0;
        if (k == 0) return 1; // Only x=1
        vector<int> depths(70, -1);
        for (int i = 1; i < 70; ++i) {
            int x = i, d = 0;
            while (x > 1) {
                int c = 0, t = x; while (t) { c += t&1; t >>= 1; }
                x = c; d++;
            }
            depths[i] = d;
        }
        long long ans = 0;
        for (int ones = 1; ones < 70; ++ones) {
            if (depths[ones] == k-1) {
                ans += count_ones(n, ones);
            }
        }
        if (k == 1) ans--; // Exclude 0
        return ans;
    }
};
# @lc code=end