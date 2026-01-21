#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3331 lang=cpp
 *
 * [3331] Find Subtree Sizes After Changes
 */

// @lc code=start
class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = (int)parent.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; i++) children[parent[i]].push_back(i);

        // Step 1: compute new parent for each node based on closest same-char ancestor.
        vector<int> newParent(n, -1);
        vector<int> last(26, -1);
        vector<int> oldLast(n, -1);

        // iterative DFS with enter/exit states
        vector<pair<int,int>> st;
        st.reserve(2 * n);
        st.push_back({0, 0}); // (node, state) state:0 enter, 1 exit

        while (!st.empty()) {
            auto [u, state] = st.back();
            st.pop_back();
            int c = s[u] - 'a';

            if (state == 0) {
                // entering
                oldLast[u] = last[c];
                if (u == 0) newParent[u] = -1;
                else newParent[u] = (oldLast[u] != -1) ? oldLast[u] : parent[u];

                last[c] = u;
                st.push_back({u, 1});
                // push children in reverse to keep original order (not required)
                for (int i = (int)children[u].size() - 1; i >= 0; --i) {
                    st.push_back({children[u][i], 0});
                }
            } else {
                // exiting: restore
                last[c] = oldLast[u];
            }
        }

        // Step 2: build final tree using newParent
        vector<vector<int>> children2(n);
        for (int i = 1; i < n; i++) {
            children2[newParent[i]].push_back(i);
        }

        // Step 3: postorder traversal to compute subtree sizes
        vector<int> ans(n, 1);
        st.clear();
        st.push_back({0, 0});
        while (!st.empty()) {
            auto [u, state] = st.back();
            st.pop_back();
            if (state == 0) {
                st.push_back({u, 1});
                for (int i = (int)children2[u].size() - 1; i >= 0; --i) {
                    st.push_back({children2[u][i], 0});
                }
            } else {
                int sz = 1;
                for (int v : children2[u]) sz += ans[v];
                ans[u] = sz;
            }
        }

        return ans;
    }
};
// @lc code=end
