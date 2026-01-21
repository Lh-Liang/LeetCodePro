#
# @lc app=leetcode id=3425 lang=cpp
#
# [3425] Longest Special Path
#

# @lc code=start
class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        vector<vector<pair<int, int>>> adj(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].emplace_back(v, w);
            adj[v].emplace_back(u, w);
        }
        const int MAXV = 50010;
        vector<int> last_pos(MAXV, -1);
        vector<long long> prefix_sum;
        prefix_sum.reserve(n + 1);
        int lft = 0;
        long long mxlen = 0;
        int mnk = 1;
        auto dfs = [&](auto&& self, int u, int p, int dep, long long cursum) -> void {
            int val = nums[u];
            int oldlp = last_pos[val];
            int cur_l = lft;
            int nl = cur_l;
            if (oldlp >= cur_l) {
                nl = oldlp + 1;
            }
            int saved_l = lft;
            lft = nl;
            last_pos[val] = dep;
            prefix_sum.push_back(cursum);
            long long plen = prefix_sum[dep] - prefix_sum[nl];
            int pk = dep - nl + 1;
            if (plen > mxlen) {
                mxlen = plen;
                mnk = pk;
            } else if (plen == mxlen) {
                mnk = min(mnk, pk);
            }
            for (auto [v, w] : adj[u]) {
                if (v != p) {
                    self(self, v, u, dep + 1, cursum + w);
                }
            }
            prefix_sum.pop_back();
            last_pos[val] = oldlp;
            lft = saved_l;
        };
        dfs(dfs, 0, -1, 0, 0LL);
        return {(int)mxlen, mnk};
    }
};
# @lc code=end