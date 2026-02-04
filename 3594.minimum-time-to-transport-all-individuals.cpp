#
# @lc app=leetcode id=3594 lang=cpp
#
# [3594] Minimum Time to Transport All Individuals
#
# @lc code=start
#include <vector>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;

class Solution {
public:
    double minTime(int n, int k, int m, vector<int>& time, vector<double>& mul) {
        // DP state: (people_at_base_mask, stage, boat_at_base)
        // boat_at_base: 1 = at base, 0 = at destination
        // Use memoization
        constexpr double INF = 1e18;
        double dp[1<<12][5][2];
        bool vis[1<<12][5][2];
        memset(vis, 0, sizeof(vis));
        
        function<double(int,int,int)> dfs = [&](int mask, int stage, int boat) -> double {
            // Sanity check: if all people have crossed and boat is at destination, done
            if(mask == 0 && boat == 0) return 0.0;
            // If boat is at base but no one left to cross, invalid
            if(mask == 0) return INF;
            if(vis[mask][stage][boat]) return dp[mask][stage][boat];
            vis[mask][stage][boat] = 1;
            double& res = dp[mask][stage][boat];
            res = INF;
            if(boat == 1) { // boat at base
                // Generate all valid non-empty groups of up to k people at base
                vector<int> idxs;
                for(int i=0;i<n;++i) if((mask>>i)&1) idxs.push_back(i);
                int bsize = idxs.size();
                for(int sel = 1; sel < (1<<bsize); ++sel) {
                    if(__builtin_popcount(sel) > k) continue;
                    int newmask = mask;
                    double mx = 0.0;
                    for(int j=0;j<bsize;++j) {
                        if((sel>>j)&1) {
                            mx = max(mx, (double)time[idxs[j]]);
                            newmask ^= (1<<idxs[j]);
                        }
                    }
                    double trip = mx * mul[stage];
                    int adv = (int)floor(trip)%m;
                    int newstage = (stage + adv)%m;
                    double subres = dfs(newmask,newstage,0);
                    if(subres < INF) res = min(res, trip+subres);
                }
            } else { // boat at destination, need to return someone if people still at base
                // If all at base, can't return
                if(mask == (1<<n)-1) return INF;
                vector<int> idxs;
                for(int i=0;i<n;++i) if(!((mask>>i)&1)) idxs.push_back(i); // at dest
                for(int i: idxs) {
                    double rtrip = time[i] * mul[stage];
                    int adv = (int)floor(rtrip)%m;
                    int newstage = (stage + adv)%m;
                    double subres = dfs(mask|(1<<i),newstage,1);
                    if(subres < INF) res = min(res, rtrip+subres);
                }
            }
            // Complete: return computed value for this state
            return res;
        };
        double ans = dfs((1<<n)-1, 0, 1);
        if(ans >= INF) return -1.0;
        return ans;
    }
};
# @lc code=end