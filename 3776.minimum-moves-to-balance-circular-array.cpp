#include <bits/stdc++.h>
using namespace std;

#// @lc app=leetcode id=3776 lang=cpp
#//
#// [3776] Minimum Moves to Balance Circular Array
#//

#// @lc code=start
class Solution {
public:
    long long minMoves(vector<int>& balance) {
        int n = (int)balance.size();
        if (n == 1) return balance[0] >= 0 ? 0LL : -1LL;

        int negIdx = -1;
        for (int i = 0; i < n; i++) {
            if (balance[i] < 0) {
                if (negIdx != -1) return -1; // safety (though problem says at most one)
                negIdx = i;
            }
        }
        if (negIdx == -1) return 0LL;

        long long total = 0;
        for (int x : balance) total += (long long)x;
        if (total < 0) return -1LL;

        long long deficit = -(long long)balance[negIdx];
        vector<pair<int,long long>> sources; // (distance to negIdx, supply)
        sources.reserve(n - 1);

        for (int i = 0; i < n; i++) {
            if (i == negIdx) continue;
            long long supply = (long long)balance[i];
            if (supply <= 0) continue;
            int cw = (i - negIdx + n) % n;
            int ccw = (negIdx - i + n) % n;
            int d = min(cw, ccw);
            sources.push_back({d, supply});
        }

        sort(sources.begin(), sources.end(), [](const auto& a, const auto& b){
            return a.first < b.first;
        });

        long long moves = 0;
        long long need = deficit;
        for (auto &p : sources) {
            if (need == 0) break;
            int d = p.first;
            long long can = p.second;
            long long take = min(need, can);
            moves += take * (long long)d;
            need -= take;
        }

        // If total >= 0 and only one negative exists, need must be 0.
        return need == 0 ? moves : -1LL;
    }
};
#// @lc code=end
