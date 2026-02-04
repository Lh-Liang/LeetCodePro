#
# @lc app=leetcode id=3331 lang=cpp
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        // Step 1: Build original tree (children list)
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) {
            children[parent[i]].push_back(i);
        }

        // Step 2: Find new parent for each node (excluding root)
        vector<int> new_parent(n, -1);
        new_parent[0] = -1;
        vector<vector<int>> char_stack(26); // stack for each character
        function<void(int)> dfs = [&](int node) {
            int c = s[node] - 'a';
            // If there is an ancestor with same char, set as new parent
            if (!char_stack[c].empty()) {
                new_parent[node] = char_stack[c].back();
            } else {
                new_parent[node] = parent[node];
            }
            char_stack[c].push_back(node);
            for (int child : children[node]) {
                dfs(child);
            }
            char_stack[c].pop_back();
        };
        dfs(0);

        // Step 3: Build new tree with new_parent array
        vector<vector<int>> new_children(n);
        for (int i = 1; i < n; ++i) {
            if (new_parent[i] != -1) {
                new_children[new_parent[i]].push_back(i);
            }
        }

        // Step 4: Verify the new tree is valid (one root, no cycles, all nodes reachable)
        vector<bool> visited(n, false);
        function<void(int)> verify = [&](int node) {
            visited[node] = true;
            for (int child : new_children[node]) {
                if (visited[child]) throw runtime_error("Cycle detected");
                verify(child);
            }
        };
        verify(0);
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) throw runtime_error("Disconnected node detected");
        }

        // Step 5: Calculate subtree sizes in new tree
        vector<int> answer(n, 0);
        function<int(int)> dfs_size = [&](int node) {
            int size = 1;
            for (int child : new_children[node]) {
                size += dfs_size(child);
            }
            answer[node] = size;
            return size;
        };
        dfs_size(0);
        return answer;
    }
};
# @lc code=end