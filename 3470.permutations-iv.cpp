#
# @lc app=leetcode id=3470 lang=cpp
#
# [3470] Permutations IV
#
# @lc code=start
class Solution {
public:
    vector<int> permute(int n, long long k) {
        vector<int> odds, evens;
        for (int i = 1; i <= n; ++i) {
            if (i % 2) odds.push_back(i);
            else evens.push_back(i);
        }
        int odd_cnt = odds.size(), even_cnt = evens.size();
        // dp[odd_left][even_left][last_parity]: number of valid arrangements
        map<tuple<int,int,int>, long long> dp;
        function<long long(int,int,int)> count = [&](int o, int e, int last) -> long long {
            if (o+e == 0) return 1;
            auto key = make_tuple(o,e,last);
            if (dp.count(key)) return dp[key];
            long long res = 0;
            if (last == -1) {
                if (o) res += o * count(o-1,e,1);
                if (e) res += e * count(o,e-1,0);
            } else {
                if (last == 1 && e) res += e * count(o,e-1,0);
                if (last == 0 && o) res += o * count(o-1,e,1);
            }
            return dp[key]=res;
        };
        long long total = count(odd_cnt,even_cnt,-1);
        if (k > total) return {};
        vector<int> result;
        vector<bool> used(n+1,false);
        int o = odd_cnt, e = even_cnt, last = -1;
        for (int pos = 0; pos < n; ++pos) {
            for (int num = 1; num <= n; ++num) {
                if (used[num]) continue;
                int np = num%2;
                if (last==-1 || np!=last) {
                    int no = o, ne = e;
                    if (np) --no;
                    else --ne;
                    if (no < 0 || ne < 0) continue;
                    long long cnt = count(no, ne, np);
                    if (k > cnt) {
                        k -= cnt;
                    } else {
                        result.push_back(num);
                        used[num]=true;
                        o = no, e = ne, last=np;
                        break;
                    }
                }
            }
        }
        // Verification step: ensure no two adjacent elements have the same parity
        for (int i = 1; i < result.size(); ++i) {
            if ((result[i]%2) == (result[i-1]%2)) return {};
        }
        return result;
    }
};
# @lc code=end