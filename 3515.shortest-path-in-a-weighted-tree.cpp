#
# @lc app=leetcode id=3515 lang=cpp
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
class Solution {
public:
    vector<int> treeQueries(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        vector<vector<pair<int, int>>> g(n+1);
        map<pair<int,int>, int> edge_wt;
        for (auto& e : edges) {
            int u=e[0], v=e[1], w=e[2];
            g[u].push_back({v,w});
            g[v].push_back({u,w});
            edge_wt[{min(u,v), max(u,v)}] = w;
        }
        vector<int> in(n+1), out(n+1), parent(n+1), depth(n+1);
        int timer=0;
        function<void(int,int,int)> dfs = [&](int u, int p, int d) {
            parent[u]=p; depth[u]=d; in[u]=++timer;
            for (auto& [v, w] : g[u]) {
                if (v!=p) dfs(v, u, d+w);
            }
            out[u]=timer;
        };
        dfs(1,0,0);
        // Fenwick tree for range add, point query
        struct BIT {
            vector<long long> t; int n;
            BIT(int sz):t(sz+2),n(sz+2){}
            void add(int i, long long x){for(;i<n;i+=i&-i)t[i]+=x;}
            void range_add(int l,int r,long long x){add(l,x);add(r+1,-x);}
            long long query(int i){long long s=0;for(;i;i-=i&-i)s+=t[i];return s;}
        } bit(n+2);
        // initial fill
        for(int u=1;u<=n;u++) bit.range_add(in[u], in[u], depth[u]);
        // edge to child mapping
        map<pair<int,int>, int> edge2child;
        for (auto& e: edges) {
            int u=e[0], v=e[1];
            if (parent[v]==u) edge2child[{min(u,v),max(u,v)}]=v;
            else edge2child[{min(u,v),max(u,v)}]=u;
        }
        vector<int> ans;
        for (auto& q: queries) {
            if (q[0]==2) {
                int x=q[1];
                ans.push_back((int)bit.query(in[x]));
            } else {
                int u=q[1], v=q[2], nw=q[3];
                int keyu=min(u,v), keyv=max(u,v);
                int oldw=edge_wt[{keyu,keyv}];
                int diff=nw-oldw;
                edge_wt[{keyu,keyv}]=nw;
                int child = edge2child[{keyu, keyv}];
                bit.range_add(in[child], out[child], diff);
            }
        }
        return ans;
    }
};
# @lc code=end