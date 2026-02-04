#
# @lc app=leetcode id=3538 lang=cpp
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
#include <vector>
#include <tuple>
#include <algorithm>
#include <unordered_map>
using namespace std;

struct VectorHash {
    size_t operator()(const vector<int>& v) const {
        size_t h = 0;
        for (int x : v) h = h * 31 + x;
        return h;
    }
};

class Solution {
public:
    int minTravelTime(int l, int n, int k, vector<int>& position, vector<int>& time) {
        using State = tuple<vector<int>, vector<int>, int>;
        struct StateHash {
            size_t operator()(const State& s) const {
                VectorHash vh;
                const auto& t = get<0>(s);
                const auto& seg = get<1>(s);
                int m = get<2>(s);
                return vh(t) ^ (vh(seg) << 1) ^ (m << 16);
            }
        };
        unordered_map<State, int, StateHash> memo;
        vector<int> seg_len(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            seg_len[i] = position[i + 1] - position[i];
        }
        function<int(vector<int>&, vector<int>&, int)> dp = [&](vector<int>& t, vector<int>& seg, int merges) -> int {
            if (merges == k) {
                int ans = 0;
                for (int i = 0; i < seg.size(); ++i) {
                    ans += seg[i] * t[i];
                }
                return ans;
            }
            State key = make_tuple(t, seg, merges);
            if (memo.count(key)) return memo[key];
            int res = INT_MAX;
            // Try all valid merges: merge i-1 and i (for i >= 1)
            for (int i = 1; i < (int)t.size(); ++i) {
                vector<int> t2 = t, seg2 = seg;
                t2[i] += t2[i - 1];
                t2.erase(t2.begin() + (i - 1));
                seg2[i - 1] += seg2[i];
                seg2.erase(seg2.begin() + i);
                res = min(res, dp(t2, seg2, merges + 1));
            }
            memo[key] = res;
            return res;
        };
        // Initial verification: the number of times matches number of segments
        if ((int)time.size() != n || (int)seg_len.size() != n - 1) return -1;
        // Defensive: k within valid range
        if (k < 0 || k > n - 2) return -1;
        return dp(time, seg_len, 0);
    }
};
# @lc code=end