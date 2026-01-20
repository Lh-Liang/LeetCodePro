#
# @lc app=leetcode id=3515 lang=cpp
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
class Solution {
    vector<int> tin, tout;
    vector<long long> initial_dist;
    vector<int> parent;
    int timer;
    vector<long long> bit;
    int n_nodes;
    
    // Standard Fenwick Tree for Range Update, Point Query
    // To add val to [l, r]: update(l, val), update(r + 1, -val)
    // To get value at index i: query(i)
    void update(int idx, long long val) {
        for (; idx <= n_nodes; idx += idx & -idx)
            bit[idx] += val;
    }

    long long query(int idx) {
        long long sum = 0;
        for (; idx > 0; idx -= idx & -idx)
            sum += bit[idx];
        return sum;
    }

    void range_update(int l, int r, long long val) {
        update(l, val);
        update(r + 1, -val);
    }

    void dfs(int u, int p, long long d, const vector<vector<pair<int, int>>>& adj) {
        tin[u] = ++timer;
        initial_dist[u] = d;
        parent[u] = p;
        for (auto& edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (v != p) {
                dfs(v, u, d + w, adj);
            }
        }
        tout[u] = timer;
    }

public:
    vector<long long> treeQueries(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        n_nodes = n;
        tin.assign(n + 1, 0);
        tout.assign(n + 1, 0);
        initial_dist.assign(n + 1, 0);
        parent.assign(n + 1, 0);
        bit.assign(n + 2, 0);
        timer = 0;

        vector<vector<pair<int, int>>> adj(n + 1);
        // Map to store current weight of edge between u and v. 
        // Since u, v are <= 10^5, we can use a map of pairs or just look it up.
        // A map<pair<int,int>, int> is simplest.
        // Actually, we just need to update the logic. We don't need to look up weight from map if we store it elsewhere.
        // Let's store edge weights in a way we can access by edge index or node pair.
        // The update query gives u, v. We need to find the child.
        
        // To handle updates efficiently, we need to know the current weight to calculate delta.
        // We can use a map for (min(u,v), max(u,v)) -> weight.
        map<pair<int, int>, int> edge_weights;

        for (auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
            int u = e[0], v = e[1];
            if (u > v) swap(u, v);
            edge_weights[{u, v}] = e[2];
        }

        dfs(1, 0, 0, adj);

        vector<long long> answer;
        answer.reserve(queries.size()); // Heuristic reservation

        for (auto& q : queries) {
            if (q[0] == 1) {
                int u = q[1];
                int v = q[2];
                int new_w = q[3];
                
                // Determine child node
                // In the DFS tree, the child is the one with deeper depth or simply the one that is not the parent of the other.
                // Since it's a tree edge, one is parent of other.
                int child = (parent[u] == v) ? u : v;
                
                int u_key = u, v_key = v;
                if (u_key > v_key) swap(u_key, v_key);
                
                int old_w = edge_weights[{u_key, v_key}];
                int delta = new_w - old_w;
                
                if (delta != 0) {
                    range_update(tin[child], tout[child], delta);
                    edge_weights[{u_key, v_key}] = new_w;
                }
            } else {
                int x = q[1];
                long long current_dist = initial_dist[x] + query(tin[x]);
                answer.push_back(current_dist);
            }
        }

        return answer;
    }
};
# @lc code=end