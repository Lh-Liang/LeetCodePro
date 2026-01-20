#
# @lc app=leetcode id=3585 lang=cpp
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
class Solution {
public:
    vector<int> findMedian(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }

        int LOG = 0;
        while ((1 << LOG) <= n) LOG++;
        
        vector<vector<int>> up(n, vector<int>(LOG, -1));
        vector<int> depth(n, 0);
        vector<long long> dist(n, 0);

        // BFS to build tree properties
        // Using BFS prevents stack overflow for deep trees compared to DFS
        vector<int> q;
        q.push_back(0);
        vector<bool> visited(n, false);
        visited[0] = true;
        
        while (!q.empty()) {
            int u = q.front(); // Standard BFS queue logic, but using vector as queue here is fine if we iterate index
            // Actually standard queue is better or just iterate vector
            break; // Switching to standard DFS recursion is risky for 10^5, let's use iterative DFS or BFS with parent tracking
        }
        
        // Let's restart the traversal logic cleanly using a stack for iterative DFS to compute depths and parents
        // Or BFS. BFS is good for depth and dist.
        // We need traversal order to fill `up` table. Standard BFS works.
        
        vector<int> bfs_order;
        bfs_order.reserve(n);
        vector<int> parent(n, -1);
        vector<int> queue_nodes;
        queue_nodes.push_back(0);
        visited.assign(n, false);
        visited[0] = true;
        
        int head = 0;
        while(head < queue_nodes.size()){
            int u = queue_nodes[head++];
            bfs_order.push_back(u);
            
            for(auto& edge : adj[u]){
                int v = edge.first;
                int w = edge.second;
                if(!visited[v]){
                    visited[v] = true;
                    depth[v] = depth[u] + 1;
                    dist[v] = dist[u] + w;
                    parent[v] = u;
                    up[v][0] = u;
                    queue_nodes.push_back(v);
                }
            }
        }

        // Fill binary lifting table
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i < n; i++) {
                if (up[i][j-1] != -1) {
                    up[i][j] = up[up[i][j-1]][j-1];
                }
            }
        }

        auto get_lca = [&](int u, int v) -> int {
            if (depth[u] < depth[v]) swap(u, v);
            for (int j = LOG - 1; j >= 0; j--) {
                if (depth[u] - (1 << j) >= depth[v]) {
                    u = up[u][j];
                }
            }
            if (u == v) return u;
            for (int j = LOG - 1; j >= 0; j--) {
                if (up[u][j] != up[v][j]) {
                    u = up[u][j];
                    v = up[v][j];
                }
            }
            return up[u][0];
        };

        auto get_kth_ancestor = [&](int node, int k) -> int {
            for (int i = 0; i < LOG; i++) {
                if ((k >> i) & 1) {
                    node = up[node][i];
                }
            }
            return node;
        };

        vector<int> ans;
        ans.reserve(queries.size());

        for (const auto& query : queries) {
            int u = query[0];
            int v = query[1];
            
            int lca = get_lca(u, v);
            long long dist_u_lca = dist[u] - dist[lca];
            long long dist_v_lca = dist[v] - dist[lca];
            long long total_dist = dist_u_lca + dist_v_lca;
            
            // We need the first node x on path u->v such that dist(u, x) * 2 >= total_dist
            // This is equivalent to dist(u, x) >= total_dist / 2.0
            // To avoid float issues: 2 * dist(u, x) >= total_dist
            
            if (2 * dist_u_lca >= total_dist) {
                // The target is on the path from u to lca.
                // We need an ancestor x of u (up to lca) such that dist(u, x) is minimized but >= limit.
                // Wait, condition is dist(u, x) >= limit.
                // On the path u -> lca, dist(u, x) increases as we go up.
                // We want the *first* node satisfying the condition.
                // Since we start from u (dist=0) and go to lca, the distance increases.
                // We want to find the node closest to u (lowest depth) that satisfies the condition.
                // But wait, if dist(u, x) >= limit, and we are going u->lca, the first node we hit satisfying this
                // is the one with the smallest distance >= limit. 
                // Since distance is monotonic, this is just finding a point on the path.
                // Specifically, we want x such that dist(u) - dist(x) >= total_dist / 2.
                // dist(x) <= dist(u) - total_dist / 2.
                // We want the ancestor x with largest dist(x) (closest to u) that satisfies this? 
                // No. Path is u -> ... -> x -> ... -> lca.
                // Distances from u: 0, ..., d_x, ..., d_lca.
                // We want smallest d_x such that d_x >= limit.
                // Since d_x = dist[u] - dist[x], we want smallest (dist[u] - dist[x]) >= limit.
                // dist[u] - dist[x] >= limit  =>  dist[x] <= dist[u] - limit.
                // To minimize (dist[u] - dist[x]), we need to maximize dist[x].
                // So we want the ancestor x with the LARGEST dist[x] (deepest node) such that dist[x] <= dist[u] - limit.
                // Wait, floating point logic: target_w = ceil(total_dist / 2.0). We want dist(u, x) >= target_w.
                // value needed: rem = dist[u] - target_w. We need dist[x] <= rem.
                // To find the *first* node on path u->v, we want the one closest to u.
                // Closest to u means largest depth.
                // So we want the deepest ancestor x such that dist[u] - dist[x] >= target_w.
                // Which is dist[x] <= dist[u] - target_w.
                // So we look for the highest node (smallest dist) that fails, and go one down? 
                // Or simply binary lift to find the deepest node satisfying the condition dist[x] <= dist[u] - target_w.
                
                long long limit_doubled = total_dist;
                // We want smallest dist(u, x) such that 2 * dist(u, x) >= total_dist
                // 2 * (dist[u] - dist[x]) >= total_dist
                // 2 * dist[u] - 2 * dist[x] >= total_dist
                // 2 * dist[x] <= 2 * dist[u] - total_dist
                
                long long target_val = 2 * dist[u] - total_dist;
                
                // We want deepest x (closest to u) such that 2 * dist[x] <= target_val.
                // Wait, if 2*dist[x] is very small (root), it satisfies.
                // If x is u, 2*dist[u] <= 2*dist[u] - total_dist => 0 <= -total_dist (False).
                // So we start from u and go up. The condition 2*dist[x] <= target_val becomes true closer to root.
                // We want the *first* node on path u->lca satisfying the median condition.
                // First node means closest to u satisfying 2*(dist[u] - dist[x]) >= total_dist.
                // i.e., 2*dist[x] <= target_val.
                // Since dist[x] decreases as we go up, once it satisfies, all ancestors satisfy.
                // We want the one closest to u, so the largest dist[x] satisfying 2*dist[x] <= target_val.
                
                int curr = u;
                for (int i = LOG - 1; i >= 0; i--) {
                    // If we jump to up[curr][i], is the distance still too large?
                    // We want to verify if 2 * dist[up[curr][i]] > target_val.
                    // If it is, we MUST jump up because we haven't satisfied the condition yet.
                    // We want to stop just before we satisfy it (or find the point).
                    // Actually, we want the deepest node satisfying <= target_val.
                    // Let's try to find the highest node violating the condition (> target_val) and take its parent.
                    // No, parent has smaller distance. 
                    // We want the node with largest dist <= target_val.
                    // So if up[curr][i] has 2*dist > target_val, we are still too close to u (dist is too large), 
                    // but we need smaller dist. Wait.
                    // dist[x] decreases as we go up.
                    // u (large dist) -> ... -> root (small dist).
                    // We want largest dist <= K.
                    // If up[curr][i] exists and 2 * dist[up[curr][i]] > target_val:
                    // It means up[curr][i] does NOT satisfy the condition (dist is too big).
                    // So the answer must be above up[curr][i]. We jump there.
                    if (up[curr][i] != -1 && 2 * dist[up[curr][i]] > target_val) {
                        curr = up[curr][i];
                    }
                }
                // After loop, curr is the highest node where 2 * dist > target_val.
                // So curr does not satisfy. The parent of curr should satisfy it.
                // However, we must be careful if u itself satisfies it? (handled by logic, u > target_val usually).
                // If 2*dist[u] <= target_val, then u is the answer. (Handled separately or carefully).
                // Let's check u first.
                if (2 * dist[u] <= target_val) {
                    ans.push_back(u);
                } else {
                    // curr is the highest node violating. The answer is up[curr][0].
                    // We must check if up[curr][0] is valid (not -1), though logic suggests it should exist if solution exists.
                    // Also need to ensure we don't go above LCA. But condition 2*dist_u_lca >= total_dist ensures solution is in subtree.
                    ans.push_back(up[curr][0]);
                }
            } else {
                // The target is on the path from lca to v.
                // We want the first node x on lca->v such that dist(u, x) >= total_dist / 2.
                // dist(u, x) = dist(u, lca) + (dist[x] - dist[lca]).
                // 2 * (dist_u_lca + dist[x] - dist[lca]) >= total_dist
                // 2 * dist[x] >= total_dist - 2 * dist_u_lca + 2 * dist[lca]
                
                long long target_val = total_dist - 2 * dist_u_lca + 2 * dist[lca];
                
                // We need x on path lca->v (x is ancestor of v).
                // As we go down from lca to v, dist[x] increases.
                // We want the *first* node x, so closest to lca (smallest dist[x]).
                // Satisfying 2 * dist[x] >= target_val.
                
                // We start from v and jump up.
                // v has large dist. lca has small dist.
                // We want smallest dist >= K.
                // If up[v][i] satisfies 2 * dist[up[v][i]] >= target_val:
                // It means up[v][i] is a candidate, and there might be a better one (smaller dist) above it.
                // So we jump to it.
                // Wait, if we jump to it, we move closer to root (smaller dist).
                // Yes, we want smallest dist >= K.
                // So if up[v][i] >= K, we can go there and try to go even higher.
                
                int curr = v;
                for (int i = LOG - 1; i >= 0; i--) {
                    if (up[curr][i] != -1) {
                        // We need to ensure we don't jump above LCA? 
                        // The condition 2*dist >= target_val implicitly handles it?
                        // dist[lca] < target_val (since solution is on lca->v excluding lca).
                        // So if we jump to a node with dist >= target_val, it is definitely below or equal to the optimal node.
                        // Wait, if up[curr][i] satisfies the condition (>= target_val),
                        // it is a valid candidate (dist is large enough). We want to see if we can go higher (smaller dist) and still satisfy.
                        // So if satisfies, we jump? 
                        // If we jump, curr becomes up[curr][i]. We continue checking higher.
                        // This finds the highest node satisfying the condition.
                        // Highest node = smallest dist = first node on path from lca to v.
                        
                        if (2 * dist[up[curr][i]] >= target_val) {
                            curr = up[curr][i];
                        }
                    }
                }
                ans.push_back(curr);
            }
        }

        return ans;
    }
};
# @lc code=end