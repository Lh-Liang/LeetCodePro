#
# @lc app=leetcode id=3594 lang=cpp
#
# [3594] Minimum Time to Transport All Individuals
#
# @lc code=start
class Solution {
public:
    double minTime(int n, int k, int m, vector<int>& time, vector<double>& mul) {
        if (n > k && k == 1) {
            return -1.0;
        }
        
        map<tuple<int, int, int>, double> memo;
        set<tuple<int, int, int>> visiting;
        
        function<double(int, int, int)> dfs = [&](int at_dest, int stage, int boat_at_dest) -> double {
            if (at_dest == (1 << n) - 1) {
                return 0.0;
            }
            
            auto key = make_tuple(at_dest, stage, boat_at_dest);
            if (memo.count(key)) {
                return memo[key];
            }
            if (visiting.count(key)) {
                return 1e9;
            }
            
            visiting.insert(key);
            double result = 1e9;
            
            if (boat_at_dest == 0) {
                vector<int> available;
                for (int i = 0; i < n; i++) {
                    if ((at_dest & (1 << i)) == 0) {
                        available.push_back(i);
                    }
                }
                
                int sz = available.size();
                for (int mask = 1; mask < (1 << sz); mask++) {
                    if (__builtin_popcount(mask) > k) continue;
                    
                    int new_at_dest = at_dest;
                    int max_time = 0;
                    for (int i = 0; i < sz; i++) {
                        if (mask & (1 << i)) {
                            new_at_dest |= (1 << available[i]);
                            max_time = max(max_time, time[available[i]]);
                        }
                    }
                    
                    double crossing_time = max_time * mul[stage];
                    int new_stage = (stage + ((int)floor(crossing_time) % m)) % m;
                    
                    result = min(result, crossing_time + dfs(new_at_dest, new_stage, 1));
                }
            } else {
                for (int i = 0; i < n; i++) {
                    if (at_dest & (1 << i)) {
                        int new_at_dest = at_dest ^ (1 << i);
                        double return_time = time[i] * mul[stage];
                        int new_stage = (stage + ((int)floor(return_time) % m)) % m;
                        
                        result = min(result, return_time + dfs(new_at_dest, new_stage, 0));
                    }
                }
            }
            
            visiting.erase(key);
            memo[key] = result;
            return result;
        };
        
        double ans = dfs(0, 0, 0);
        return ans >= 1e9 ? -1.0 : ans;
    }
};
# @lc code=end