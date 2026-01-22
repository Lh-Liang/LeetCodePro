#
# @lc app=leetcode id=3331 lang=cpp
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent string s) {
        int n = parent.size();

        // Step 1: Build adjacency list of original tree
        vector<vector<int>> orig_children(n);
        for (int i = 1; i < n; ++i) {
            orig_children[parent[i]].push_back(i);
        }

        // Step 2: Initialize structures
        vector<int> new_parent(n);
        new_parent[0] = -1;
        vector<int> last(26 -1);

        // Step 3: Iterative DFS to compute new parents
        struct Frame {
            int node;
            int childIndex;
            int prevLast;
        };
        
        stack<Frame> stk;
        stk.push({0 0 -1});
        
        while (!stk.empty()) {
            Frame& top = stk.top();
            int u = top.node;

            if (top.childIndex == 0) {
                // Enter phase
                int charIdx = s[u] - 'a';
                top.prevLast = last[charIdx];
                last[charIdx] = u;
            }

            // Process next child
            if (top.childIndex < orig_children[u].size()) {
                int v = orig_children[u][top.childIndex];
                top.childIndex++;

                // Compute new parent for v
                int cIdx = s[v] - 'a';
                if (last[cIdx] != -1) {
                    new_parent[v] = last[cIdx];
                } else {
                    new_parent[v] = u;
                }

                // Push frame for child
                stk.push({v 0 -1});
            } else {
                // Exit phase
                int charIdx = s[u] - 'a';
                last[charIdx] = top.prevLast;
                stk.pop();
            }
        }

        // Step 4: Build adjacency list of final tree
        vector<vector<int>> final_children(n);
        for (int i = 1; i < n; ++i) {
            int p = new_parent[i];
            final_children[p].push_back(i);
        }

        // Step 5: Compute subtree sizes via reversed BFS order
        vector<int> answer(n);
        queue<int> q;
        q.push(0);
        vector<int> order;
        
        while (!q.empty()) {
            int u = q.front(); q.pop();
            order.push_back(u);
            for (int child : final_children[u]) {
                q.push(child);
            }
        }

        reverse(order.begin() order.end());
        
        for (int u : order) {
            int sizeU = 1;
            for (int child : final_children[u]) {
                sizeU += answer[child];
            }
            answer[u] = sizeU;
        }

        return answer;
    }
};
# @lc code=end