#
# @lc app=leetcode id=3776 lang=cpp
#
# [3776] Minimum Moves to Balance Circular Array
#
# @lc code=start
class Solution {
public:
    long long minMoves(vector<int>& balance) {
        long long sum = 0;
        int n = balance.size();
        for (int b : balance) sum += b;
        if (sum < 0) return -1;
        int negIdx = -1;
        for (int i = 0; i < n; ++i) {
            if (balance[i] < 0) {
                negIdx = i;
                break;
            }
        }
        if (negIdx == -1) return 0; // All non-negative
        long long deficit = -balance[negIdx];
        long long moves = 0;
        int left = (negIdx - 1 + n) % n;
        int right = (negIdx + 1) % n;
        while (deficit > 0) {
            // Find closest nonzero surplus to negIdx
            int l = left, r = right, d = 1;
            bool found = false;
            while (d < n && !found) {
                if (balance[l] > 0) {
                    long long t = min((long long)balance[l], deficit);
                    balance[l] -= t;
                    deficit -= t;
                    moves += t * d;
                    found = true;
                } else if (balance[r] > 0) {
                    long long t = min((long long)balance[r], deficit);
                    balance[r] -= t;
                    deficit -= t;
                    moves += t * d;
                    found = true;
                }
                l = (l - 1 + n) % n;
                r = (r + 1) % n;
                ++d;
            }
            if (!found) return -1; // Shouldn't happen, but for safety
        }
        return moves;
    }
};
# @lc code=end