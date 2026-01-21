#include <bits/stdc++.h>
using namespace std;

// @lc app=leetcode id=3771 lang=cpp
//
// [3771] Total Score of Dungeon Runs
//
// @lc code=start
class Solution {
public:
    long long totalScore(int hp, vector<int>& damage, vector<int>& requirement) {
        int n = (int)damage.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            pref[i] = pref[i - 1] + damage[i - 1];
        }

        long long ans = 0;
        for (int i = 1; i <= n; i++) {
            long long A = pref[i] + (long long)requirement[i - 1] - (long long)hp;
            // count t in [0, i-1] with pref[t] >= A
            int idx = (int)(lower_bound(pref.begin(), pref.begin() + i, A) - pref.begin());
            ans += (long long)(i - idx);
        }
        return ans;
    }
};
// @lc code=end
