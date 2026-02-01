#
# @lc app=leetcode id=3331 lang=cpp
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
#include <vector>
#include <string>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> adj(n);
        for (int i = 1; i < n; ++i) {
            adj[parent[i]].push_back(i);
        }

        vector<int> newParent = parent;
        vector<int> lastNode(26, -1);
        
        // Step 1: Find new parents via DFS
        // Using a manual stack to avoid recursion depth issues with n=10^5
        struct State {
            int u;
            int childIdx;
            int prevLast;
        };
        
        stack<State> st;
        st.push({0, 0, -1});
        
        // Helper to update newParent and lastNode
        auto processPre = [&](int u) {
            int charIdx = s[u] - 'a';
            int old = lastNode[charIdx];
            if (old != -1) {
                newParent[u] = old;
            }
            lastNode[charIdx] = u;
            return old;
        };

        while (!st.empty()) {
            State& curr = st.top();
            if (curr.childIdx == 0) {
                curr.prevLast = processPre(curr.u);
            }
            
            if (curr.childIdx < adj[curr.u].size()) {
                int v = adj[curr.u][curr.childIdx];
                curr.childIdx++;
                st.push({v, 0, -1});
            } else {
                lastNode[s[curr.u] - 'a'] = curr.prevLast;
                st.pop();
            }
        }

        // Step 2: Build new adjacency list
        vector<vector<int>> newAdj(n);
        for (int i = 1; i < n; ++i) {
            newAdj[newParent[i]].push_back(i);
        }

        // Step 3: Calculate subtree sizes
        vector<int> subtreeSize(n, 1);
        vector<int> order;
        stack<int> topo;
        topo.push(0);
        
        // Iterative post-order traversal to calculate sizes
        vector<int> visitIdx(n, 0);
        stack<int> post;
        post.push(0);
        while(!post.empty()) {
            int u = post.top();
            if (visitIdx[u] < newAdj[u].size()) {
                post.push(newAdj[u][visitIdx[u]]);
                visitIdx[u]++;
            } else {
                order.push_back(u);
                post.pop();
            }
        }

        // Process in reverse topological order (leaves to root)
        vector<int> ans(n, 0);
        for (int u : order) {
            int currentSize = 1;
            for (int v : newAdj[u]) {
                currentSize += ans[v];
            }
            ans[u] = currentSize;
        }

        return ans;
    }
};
# @lc code=end