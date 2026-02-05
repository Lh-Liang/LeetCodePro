#
# @lc app=leetcode id=3594 lang=cpp
#
# [3594] Minimum Time to Transport All Individuals
#

# @lc code=start
class Solution {
public:
    double minTime(int n, int k, int m, vector<int>& time, vector<double>& mul) {
        using State = tuple<int,int,bool>;
        unordered_map<long long, double> memo;
        function<double(int,int,bool)> dp = [&](int mask, int stage, bool at_base) -> double {
            if(mask == 0) return 0.0; // all at destination
            long long key = ((long long)mask << 3) | (stage << 1) | at_base;
            if(memo.count(key)) return memo[key];
            double res = 1e18;
            if(at_base) {
                // choose group: all non-empty subsets of size <= k
                vector<int> people;
                for(int i=0;i<n;++i) if(mask & (1<<i)) people.push_back(i);
                int sz = people.size();
                for(int group=1; group<(1<<sz); ++group) {
                    int cnt = __builtin_popcount(group);
                    if(cnt > k) continue;
                    int next_mask = mask;
                    double mx_time = 0;
                    vector<int> crossers;
                    for(int j=0;j<sz;++j) {
                        if(group & (1<<j)) {
                            crossers.push_back(people[j]);
                            mx_time = max(mx_time, (double)time[people[j]]);
                            next_mask ^= (1<<people[j]);
                        }
                    }
                    double cross_time = mx_time * mul[stage];
                    int new_stage = (stage + ((int)floor(cross_time)) % m) % m;
                    if(next_mask == 0) {
                        res = min(res, cross_time);
                        continue;
                    }
                    // If k==n and not all cross, must return
                    for(int ret: crossers) {
                        double ret_time = time[ret] * mul[new_stage];
                        int ret_stage = (new_stage + ((int)floor(ret_time)) % m) % m;
                        int ret_mask = next_mask | (1<<ret);
                        double sub = dp(ret_mask, ret_stage, true);
                        if(sub < 1e18)
                            res = min(res, cross_time + ret_time + sub);
                    }
                }
            }
            memo[key] = res;
            return res;
        };
        double ans = dp((1<<n)-1, 0, true);
        if(ans > 1e17) return -1.0;
        return ans;
    }
};
# @lc code=end