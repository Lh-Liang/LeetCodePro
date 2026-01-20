#
# @lc app=leetcode id=3425 lang=cpp
#
# [3425] Longest Special Path
#

# @lc code=start
class Solution {
public:
    vector<pair<int, int>> adj[50005];
    int last_pos[50005];
    vector<int> path_dist;
    // result: {max_len, min_nodes}
    long long max_len = -1;
    int min_nodes = 1;

    void dfs(int u, int p, int current_dist, int start_index, const vector<int>& nums) {
        int val = nums[u];
        int prev_pos = last_pos[val];
        
        // The new start index must be after the previous occurrence of this value
        // and also at least the start index dictated by ancestors.
        int new_start_index = max(start_index, prev_pos + 1);
        
        // Calculate length of the special path ending at u starting at new_start_index
        // path_dist[i] stores the cumulative distance from root to the node at depth i.
        // path_dist size is equal to the current depth. path_dist[new_start_index] is the dist to the start node's parent?
        // No, let's define path_dist[i] as distance to node at depth i.
        // The path is from node at new_start_index to node at current depth.
        // Length = dist[current] - dist[node_at_new_start_index].
        
        int current_len = current_dist - path_dist[new_start_index];
        int current_nodes = (int)path_dist.size() - new_start_index + 1;
        
        if (current_len > max_len) {
            max_len = current_len;
            min_nodes = current_nodes;
        } else if (current_len == max_len) {
            min_nodes = min(min_nodes, current_nodes);
        }
        
        // Update state for recursion
        path_dist.push_back(current_dist);
        last_pos[val] = path_dist.size() - 1;
        
        for (auto& edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (v != p) {
                dfs(v, u, current_dist + w, new_start_index, nums);
            }
        }
        
        // Backtrack
        last_pos[val] = prev_pos;
        path_dist.pop_back();
    }

    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            adj[i].clear();
            last_pos[i] = -1;
        }
        // Since values can be up to 50000, we need to handle max value potentially being larger than n.
        // Constraints say nums[i] <= 5*10^4. We can use a map or a fixed size array if max value is known.
        // The constraints say nums[i] <= 5 * 10^4, so array size 50005 is fine.
        // Wait, nums[i] is value, not index. We need to reset last_pos for all possible values.
        // Or use a vector and fill with -1. But iterating 50000 times for each testcase is fine.
        // Actually, we should just fill `last_pos` with -1. The max value is 50000.
        fill(last_pos, last_pos + 50005, -1);

        for (auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }

        // path_dist stores the distance from root to the node at that depth.
        // Initially, we are at root (depth 0), dist is 0.
        // However, in the logic `current_len = current_dist - path_dist[new_start_index]`, 
        // if new_start_index is 0 (root), we want `current_dist - 0`. 
        // So path_dist should store distances. Before pushing current node, 
        // path_dist has distances of ancestors.
        // Let's adjust logic: 
        // path_dist[k] is distance from root to node at depth k.
        // We push the current node's distance *after* calculation or handle it carefully.
        
        // Let's restart the exact state logic:
        // path_dist will store distances of nodes currently in the recursion stack.
        // path_dist[0] = 0 (root).
        // When at u (depth k), path_dist has k elements (indices 0 to k-1).
        // We calculate special path ending at u.
        // Then we push dist[u] to path_dist (now size k+1) and recurse.
        
        path_dist.clear();
        path_dist.push_back(0); // Distance to root is 0
        
        // Special handling for root outside or inside?
        // Inside is cleaner if we adjust indices.
        // Let's pass `path_dist` differently. Let's make `path_dist` store distances of the stack.
        // Before processing root, stack is empty? No, root is part of the path.
        
        // Let's use a slightly different approach for the vector.
        // `path_dist` stores distances of nodes on the stack.
        // When at node u, `path_dist` contains distances for `root` ... `parent of u`.
        // We need `dist[u]` as well.
        // Let's pass `current_dist`.
        
        // Re-check `current_len` calculation:
        // Path from `start_index` node to `u`.
        // Length = `dist[u] - dist[node_at_start_index]`.
        // `path_dist` should store `dist` of nodes at indices 0, 1, ...
        // `path_dist[i]` = distance from root to node at depth `i`.
        
        // Reset globals
        max_len = 0;
        min_nodes = 1;
        
        // Root logic:
        // depth 0. Val = nums[0].
        // prev_pos = last_pos[val] = -1.
        // new_start = max(0, 0) = 0.
        // len = 0 - path_dist[0] = 0.
        // nodes = 0 - 0 + 1 = 1.
        // update result.
        // last_pos[val] = 0.
        // path_dist.push_back(0) is already there? No.
        
        // Let's refine the helper.
        
        vector<int> path_stack_dist;
        // We need to push 0 for root's distance initially? No, let's do it inside.
        
        dfs_final(0, -1, 0, 0, nums, path_stack_dist);
        
        return {(int)max_len, min_nodes};
    }
    
    void dfs_final(int u, int p, int current_dist, int start_index, const vector<int>& nums, vector<int>& path_stack_dist) {
        int val = nums[u];
        int prev_pos = last_pos[val];
        
        // The valid path ending at u must start after the previous occurrence of val.
        // The stack currently has `path_stack_dist` for ancestors.
        // Current depth is path_stack_dist.size().
        
        int new_start_index = max(start_index, prev_pos + 1);
        
        int dist_at_start = (new_start_index == path_stack_dist.size()) ? current_dist : path_stack_dist[new_start_index];
        // Actually, path_stack_dist contains distances of ancestors.
        // If new_start_index == current_depth, it means the path is just the node u itself.
        // distance is 0.
        
        long long current_len = current_dist - dist_at_start;
        int current_nodes = (int)path_stack_dist.size() - new_start_index + 1;
        
        if (current_len > max_len) {
            max_len = current_len;
            min_nodes = current_nodes;
        } else if (current_len == max_len) {
            min_nodes = min(min_nodes, current_nodes);
        }
        
        path_stack_dist.push_back(current_dist);
        last_pos[val] = path_stack_dist.size() - 1;
        
        for (auto& edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (v != p) {
                dfs_final(v, u, current_dist + w, new_start_index, nums, path_stack_dist);
            }
        }
        
        last_pos[val] = prev_pos;
        path_stack_dist.pop_back();
    }
};
# @lc code=end