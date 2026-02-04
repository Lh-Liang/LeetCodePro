#
# @lc app=leetcode id=3776 lang=cpp
#
# [3776] Minimum Moves to Balance Circular Array
#
# @lc code=start
class Solution {
public:
    long long minMoves(vector<int>& balance) {
        long long total = 0;
        int n = balance.size();
        for (int b : balance) total += b;
        if (total < 0) return -1;
        int neg = -1;
        for (int i = 0; i < n; ++i) {
            if (balance[i] < 0) { neg = i; break; }
        }
        if (neg == -1) return 0;
        long long need = -balance[neg];
        vector<pair<long long, int>> sources; // pair: (distance, units)
        for (int d = 1; d < n; ++d) {
            int l = (neg - d + n) % n;
            int r = (neg + d) % n;
            if (balance[l] > 0) sources.push_back({d, balance[l]});
            if (l != r && balance[r] > 0) sources.push_back({d, balance[r]});
        }
        sort(sources.begin(), sources.end());
        long long moves = 0;
        for (auto [dist, units] : sources) {
            long long take = min(need, (long long)units);
            moves += take * dist;
            need -= take;
            if (need == 0) break;
        }
        if (need > 0) return -1;
        return moves;
    }
};
# @lc code=end