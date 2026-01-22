#
# @lc app=leetcode id=3515 lang=cpp
#
# [3515] Shortest Path in a Weighted Tree
#
# @lc code=start
class Solution {
public:
    vector<int> treeQueries(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        vector<vector<pair<int, int>>> adj(n + 1);
        for (auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }
        
        vector<long long> dist(n + 1, 0);
        vector<int> parent(n + 1, 0), inTime(n + 1), outTime(n + 1), edgeWeight(n + 1, 0);
        int timer = 0;
        
        // Iterative DFS to compute distances, parent, and Euler tour
        stack<pair<int, bool>> stk;
        stk.push({1, true});
        while (!stk.empty()) {
            auto [u, first] = stk.top();
            stk.pop();
            if (first) {
                inTime[u] = ++timer;
                stk.push({u, false});
                for (auto [v, w] : adj[u]) {
                    if (v != parent[u]) {
                        parent[v] = u;
                        dist[v] = dist[u] + w;
                        edgeWeight[v] = w;
                        stk.push({v, true});
                    }
                }
            } else {
                outTime[u] = timer;
            }
        }
        
        // Fenwick tree for range update, point query
        vector<long long> bit(n + 2, 0);
        
        auto update = [&](int i, long long delta) {
            for (; i <= n; i += i & -i) bit[i] += delta;
        };
        
        auto query = [&](int i) -> long long {
            long long sum = 0;
            for (; i > 0; i -= i & -i) sum += bit[i];
            return sum;
        };
        
        vector<int> answer;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int u = q[1], v = q[2], newW = q[3];
                // Find which one is the child (the one whose parent is the other)
                int child = (parent[v] == u) ? v : u;
                long long delta = newW - edgeWeight[child];
                edgeWeight[child] = newW;
                // Range update for subtree of child
                update(inTime[child], delta);
                update(outTime[child] + 1, -delta);
            } else {
                int x = q[1];
                answer.push_back(dist[x] + query(inTime[x]));
            }
        }
        return answer;
    }
};
# @lc code=end