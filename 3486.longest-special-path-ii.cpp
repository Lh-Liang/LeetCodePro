class Solution {
public:
    vector<vector<pair<int, int>>> adj;
    vector<int> nums;
    vector<vector<int>> pos;
    vector<long long> path_dists;
    int max_len = -1;
    int min_nodes = 1;

    void dfs(int u, int p, int depth, long long current_dist, int start, int repeat_start) {
        int val = nums[u];
        
        // Step A: Handle 3rd occurrence constraint
        if (pos[val].size() >= 2) {
            int second_last = pos[val][pos[val].size() - 2];
            start = max(start, second_last + 1);
            // If the window moved past the existing duplicate pair start, reset it
            if (repeat_start != -1 && repeat_start < start) {
                repeat_start = -1;
            }
        }

        // Step B: Handle 2nd occurrence constraint (duplicate pairs)
        if (!pos[val].empty()) {
            int last = pos[val].back();
            if (last >= start) {
                // We have a duplicate pair for 'val' in the current window
                if (repeat_start != -1) {
                    // There was already a duplicate pair. We now have two.
                    // We must remove the one that starts earliest to maximize window size.
                    start = max(start, min(last, repeat_start) + 1);
                    repeat_start = max(last, repeat_start);
                } else {
                    // This is the first duplicate pair
                    repeat_start = last;
                }
            }
        }

        // Update result
        long long len = current_dist - path_dists[start];
        int nodes = depth - start + 1;
        if (len > max_len) {
            max_len = len;
            min_nodes = nodes;
        } else if (len == max_len) {
            min_nodes = min(min_nodes, nodes);
        }

        // Prepare for recursion
        pos[val].push_back(depth);
        path_dists.push_back(current_dist);

        for (auto& edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (v != p) {
                dfs(v, u, depth + 1, current_dist + w, start, repeat_start);
            }
        }

        // Backtrack
        path_dists.pop_back();
        pos[val].pop_back();
    }

    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        this->nums = nums;
        adj.resize(n);
        pos.resize(50005); // Values are up to 50000
        
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }

        // Initial call: depth 0, dist 0, start 0, no repeat (-1)
        // path_dists needs to have dist for index 0 initially? 
        // No, we push current_dist *after* calculation but we need dist[start].
        // Actually, path_dists should store dists for indices 0, 1, ... depth.
        // Before processing u, path_dists has size `depth`. 
        // Wait, if start=0, we need path_dists[0] which is 0. 
        // Let's push 0 initially for the conceptual "root's parent" or handle index carefully.
        // Easier: path_dists[i] is distance from root to node at depth i.
        // When at node u (depth d), path_dists has 0..d-1. We compute len using path_dists[start].
        // So we must push current_dist to path_dists *before* recursing, but *after* using it?
        // No, for the current node `u`, `dist[u]` is `current_dist`. `dist[start]` is in `path_dists[start]`.
        // If `start == depth`, dist is `current_dist`. 
        // So `path_dists` should contain distances for 0 to depth-1. For `depth`, use `current_dist`.
        // BUT, `start` can be `depth`. Then `path_dists[depth]` is not in vector yet. 
        // Let's just push `current_dist` into `path_dists` *before* calculation? 
        // If we do that, `path_dists[start]` is valid for `start <= depth`.
        
        // Correct flow:
        // 1. Enter node u.
        // 2. Push current_dist to path_dists.
        // 3. Do calculations. path_dists[start] is valid.
        // 4. Recurse.
        // 5. Pop.
        
        path_dists.reserve(n);
        
        // Wrapper for DFS to handle the push/pop logic cleanly
        // Actually, I can just do it inside DFS.
        
        // Re-adjust DFS logic slightly for path_dists:
        // path_dists.push_back(current_dist); // Now size is depth + 1
        // ... logic ... len = current_dist - path_dists[start]
        // ... recurse ...
        // path_dists.pop_back()

        // But wait, the update logic depends on history. History is updated *after* logic in the previous thought.
        // "Prepare for recursion: pos[val].push_back(depth)". This must be *after* logic checks.
        // "path_dists.push_back" can be done before logic to simplify indexing.
        
        dfs_wrapper(0, -1, 0, 0, 0, -1);

        return {max_len, min_nodes};
    }

    void dfs_wrapper(int u, int p, int depth, long long current_dist, int start, int repeat_start) {
        path_dists.push_back(current_dist);
        
        int val = nums[u];
        
        // Step A
        if (pos[val].size() >= 2) {
            int second_last = pos[val][pos[val].size() - 2];
            start = max(start, second_last + 1);
            if (repeat_start != -1 && repeat_start < start) {
                repeat_start = -1;
            }
        }

        // Step B
        if (!pos[val].empty()) {
            int last = pos[val].back();
            if (last >= start) {
                if (repeat_start != -1) {
                    start = max(start, min(last, repeat_start) + 1);
                    repeat_start = max(last, repeat_start);
                } else {
                    repeat_start = last;
                }
            }
        }

        long long len = current_dist - path_dists[start];
        int nodes = depth - start + 1;
        if (len > max_len) {
            max_len = len;
            min_nodes = nodes;
        } else if (len == max_len) {
            min_nodes = min(min_nodes, nodes);
        }

        pos[val].push_back(depth);
        
        for (auto& edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (v != p) {
                dfs_wrapper(v, u, depth + 1, current_dist + w, start, repeat_start);
            }
        }

        pos[val].pop_back();
        path_dists.pop_back();
    }
};