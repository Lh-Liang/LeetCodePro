#
# @lc app=leetcode id=3419 lang=cpp
#
# [3419] Minimize the Maximum Edge Weight of Graph
#
# @lc code=start
class Solution {
public:
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        // Collect unique weights for binary search
        set<int> unique_weights;
        for (auto& e : edges) unique_weights.insert(e[2]);
        vector<int> weights(unique_weights.begin(), unique_weights.end());
        sort(weights.begin(), weights.end());
        // Build original adjacency list
        vector<vector<pair<int,int>>> adj(n);
        for (auto& e : edges)
            adj[e[0]].emplace_back(e[1], e[2]);
        // Feasibility function
        auto feasible = [&](int maxw) -> bool {
            // For each node, keep only outgoing edges with weight <= maxw and pick the lowest threshold
            vector<vector<int>> out(n);
            for (int u=0; u<n; ++u) {
                vector<pair<int,int>> filtered;
                for (auto& p : adj[u]) if (p.second <= maxw) filtered.push_back(p);
                sort(filtered.begin(), filtered.end(), [](auto& a, auto& b){ return a.second < b.second; });
                for (int i=0; i<filtered.size() && i<threshold; ++i) out[u].push_back(filtered[i].first);
            }
            // Build reverse graph
            vector<vector<int>> rev(n);
            for (int u=0; u<n; ++u) for (int v : out[u]) rev[v].push_back(u);
            // BFS from node 0 in the reverse graph
            vector<bool> seen(n, false);
            queue<int> q; q.push(0); seen[0]=true;
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int v : rev[u]) if (!seen[v]) { seen[v]=true; q.push(v); }
            }
            // All nodes except 0 must be able to reach 0
            for (int u=0; u<n; ++u) if (!seen[u]) return false;
            return true;
        };
        int l=0, r=weights.size()-1, ans=-1;
        while (l<=r) {
            int m = (l+r)/2;
            if (feasible(weights[m])) { ans=weights[m]; r=m-1; }
            else l=m+1;
        }
        return ans;
    }
};
# @lc code=end