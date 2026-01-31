#
# @lc app=leetcode id=3771 lang=cpp
#
# [3771] Total Score of Dungeon Runs
#
# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long totalScore(int hp, vector<int>& damage, vector<int>& requirement) {
        int n = damage.size();
        // S[i] stores the prefix sum of damage from room 1 to i.
        // S[0] = 0, S[1] = damage[0], ..., S[n] = sum(damage[0...n-1])
        vector<long long> S(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            S[i + 1] = S[i] + (long long)damage[i];
        }
        
        long long total = 0;
        for (int i = 1; i <= n; ++i) {
            // Condition for starting room j to earn a point at room i:
            // hp - (S[i] - S[j-1]) >= requirement[i-1]
            // S[j-1] >= S[i] + requirement[i-1] - hp
            long long Ri = (long long)S[i] + requirement[i - 1] - hp;
            
            // Since S is strictly increasing, find the number of k in [0, i-1] s.t. S[k] >= Ri
            // lower_bound gives the first index k where S[k] >= Ri
            auto it = lower_bound(S.begin(), S.begin() + i, Ri);
            int k = (int)(it - S.begin());
            
            // The indices k, k+1, ..., i-1 all satisfy S[index] >= Ri.
            // Total valid indices = (i-1) - k + 1 = i - k.
            total += (long long)(i - k);
        }
        
        return total;
    }
};
# @lc code=end