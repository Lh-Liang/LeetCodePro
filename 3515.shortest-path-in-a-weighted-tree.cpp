#
# @lc app=leetcode id=3515 lang=cpp
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
class Solution {
public:
    vector<int> treeQueries(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        // adjacency list and edge mapping
        vector<vector<pair<int,int>>> adj(n+1);
        map<pair<int,int>, int> edge_idx;
        vector<int> edge_weight(edges.size());
        for (int i=0; i<edges.size(); ++i) {
            int u=edges[i][0], v=edges[i][1], w=edges[i][2];
            adj[u].push_back({v, i});
            adj[v].push_back({u, i});
            edge_idx[{min(u,v), max(u,v)}] = i;
            edge_weight[i] = w;
        }
        // parent, depth, distance from root
        vector<int> parent(n+1, -1), depth(n+1, 0);
        vector<long long> dist(n+1, 0);
        // DFS to fill parent, depth, dist
        function<void(int,int)> dfs = [&](int u, int p) {
            parent[u] = p;
            for (auto& [v, idx] : adj[u]) {
                if (v == p) continue;
                depth[v] = depth[u] + 1;
                dist[v] = dist[u] + edge_weight[idx];
                dfs(v, u);
            }
        };
        dfs(1, -1);
        // Euler tour for subtree range
        vector<int> tin(n+1), tout(n+1), order;
        int timer = 0;
        function<void(int,int)> tour = [&](int u, int p) {
            tin[u] = timer++;
            order.push_back(u);
            for (auto& [v, idx]: adj[u])
                if (v != p) tour(v,u);
            tout[u] = timer-1;
        };
        tour(1, -1);
        // Segment tree for range add and point query
        struct SegTree {
            int n; vector<long long> tree, lazy;
            SegTree(int sz) { n=1; while(n<sz) n<<=1; tree.assign(2*n,0); lazy.assign(2*n,0); }
            void push(int x, int l, int r) {
                if (lazy[x]) {
                    tree[x] += lazy[x];
                    if (l!=r) { lazy[2*x]+=lazy[x]; lazy[2*x+1]+=lazy[x]; }
                    lazy[x]=0;
                }
            }
            void add(int l, int r, long long val, int x, int lx, int rx) {
                push(x, lx, rx);
                if (r<lx||rx<l) return;
                if (l<=lx&&rx<=r) { lazy[x]+=val; push(x,lx,rx); return; }
                int m=(lx+rx)/2;
                add(l,r,val,2*x,lx,m); add(l,r,val,2*x+1,m+1,rx);
            }
            void add(int l, int r, long long val) { add(l,r,val,1,0,n-1); }
            long long get(int idx, int x, int lx, int rx) {
                push(x,lx,rx);
                if (lx==rx) return tree[x];
                int m=(lx+rx)/2;
                if (idx<=m) return get(idx,2*x,lx,m);
                else return get(idx,2*x+1,m+1,rx);
            }
            long long get(int idx) { return get(idx,1,0,n-1); }
        };
        SegTree seg(n+2);
        for (int i=1;i<=n;++i) seg.add(tin[i], tin[i], dist[i]);
        vector<int> answer;
        for (auto& q: queries) {
            if (q[0]==2) {
                int x=q[1];
                answer.push_back(seg.get(tin[x]));
            } else {
                int u=q[1], v=q[2], w=q[3];
                int a=u, b=v;
                if (parent[a]==b) swap(a,b); // b is parent of a
                int idx = edge_idx[{min(u,v),max(u,v)}];
                long long delta = w - edge_weight[idx];
                edge_weight[idx] = w;
                seg.add(tin[a], tout[a], delta);
            }
        }
        return answer;
    }
};
# @lc code=end