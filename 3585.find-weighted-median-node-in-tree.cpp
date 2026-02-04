#
# @lc app=leetcode id=3585 lang=cpp
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
class Solution {
public:
    vector<int> findMedian(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        vector<vector<pair<int, int>>> tree(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            tree[u].push_back({v, w});
            tree[v].push_back({u, w});
        }
        int LOG = 20;
        vector<vector<int>> up(n, vector<int>(LOG));
        vector<vector<long long>> upw(n, vector<long long>(LOG));
        vector<int> depth(n);
        vector<long long> pre_sum(n);
        function<void(int,int,int,long long)> dfs = [&](int u, int p, int d, long long s) {
            up[u][0] = p;
            upw[u][0] = (p==-1) ? 0 : s-pre_sum[p];
            depth[u] = d;
            pre_sum[u] = s;
            for (int k=1;k<LOG;++k) {
                if (up[u][k-1]==-1) { up[u][k]=-1; upw[u][k]=0; continue; }
                up[u][k] = up[up[u][k-1]][k-1];
                upw[u][k] = upw[u][k-1] + upw[up[u][k-1]][k-1];
            }
            for (auto& [v, w] : tree[u]) {
                if (v == p) continue;
                dfs(v, u, d+1, s+w);
            }
        };
        dfs(0, -1, 0, 0);
        auto lca = [&](int u, int v) {
            if (depth[u] < depth[v]) swap(u,v);
            for (int k=LOG-1;k>=0;--k) {
                if (up[u][k]!=-1 && depth[up[u][k]]>=depth[v]) u = up[u][k];
            }
            if (u==v) return u;
            for (int k=LOG-1;k>=0;--k) {
                if (up[u][k]!=-1 && up[u][k]!=up[v][k]) { u=up[u][k]; v=up[v][k]; }
            }
            return up[u][0];
        };
        vector<int> ans;
        for (auto& q : queries) {
            int u = q[0], v = q[1];
            if (u == v) { ans.push_back(u); continue; }
            int anc = lca(u, v);
            long long pathw = pre_sum[u] + pre_sum[v] - 2*pre_sum[anc];
            double half = pathw / 2.0;
            // Try path from u to anc
            int cur = u; long long acc = 0;
            for (int k=LOG-1;k>=0;--k) {
                if (up[cur][k]!=-1 && depth[up[cur][k]]>=depth[anc] && acc+upw[cur][k]<half) {
                    acc += upw[cur][k];
                    cur = up[cur][k];
                }
            }
            // Check if next step reaches/exceeds half
            if (cur != anc && up[cur][0]!=-1) {
                acc += upw[cur][0];
                cur = up[cur][0];
            }
            long long uj_to_cur = pre_sum[u] - pre_sum[cur];
            if (uj_to_cur >= half) {
                ans.push_back(cur); continue;
            }
            // Now move from anc towards v
            int cur2 = v; long long acc2 = pre_sum[v] - pre_sum[anc];
            vector<int> down_path;
            while (cur2 != anc) {
                down_path.push_back(cur2);
                cur2 = up[cur2][0];
            }
            reverse(down_path.begin(), down_path.end());
            long long uj_to_x = uj_to_cur;
            bool found = false;
            for (int node : down_path) {
                uj_to_x += pre_sum[node] - pre_sum[up[node][0]];
                if (uj_to_x >= half) {
                    ans.push_back(node); found = true; break;
                }
            }
            if (!found) ans.push_back(v); // fallback in case of rounding
        }
        return ans;
    }
};
# @lc code=end