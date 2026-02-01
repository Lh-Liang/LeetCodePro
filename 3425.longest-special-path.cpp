#
# @lc app=leetcode id=3425 lang=cpp
#
# [3425] Longest Special Path
#

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }

        int maxLen = -1;
        int minNodes = 1e9;
        // last_occurrence[v] stores the depth of value v in the current path
        vector<int> last_occurrence(50001, -1);
        // pathDist[d] stores the distance from root to the node at depth d in the current path
        vector<int> pathDist(n, 0);

        struct Frame {
            int u, p, currentDist, currentDepth, topDepth, edgeIdx, prevOcc;
        };

        vector<Frame> st;
        st.reserve(n);
        // Start DFS from root (node 0)
        st.push_back({0, -1, 0, 0, 0, 0, -1});

        while (!st.empty()) {
            int currIdx = st.size() - 1;
            int u = st[currIdx].u;
            int p = st[currIdx].p;
            int currentDist = st[currIdx].currentDist;
            int currentDepth = st[currIdx].currentDepth;
            
            if (st[currIdx].edgeIdx == 0) {
                // First time visit: calculate path properties
                st[currIdx].prevOcc = last_occurrence[nums[u]];
                // The special path ending at u must start after any previous occurrence of nums[u]
                // and must also satisfy the uniqueness constraints of its ancestors.
                int newTopDepth = max(st[currIdx].topDepth, st[currIdx].prevOcc + 1);
                st[currIdx].topDepth = newTopDepth; 
                
                pathDist[currentDepth] = currentDist;
                int length = currentDist - pathDist[newTopDepth];
                int nodes = currentDepth - newTopDepth + 1;

                if (length > maxLen) {
                    maxLen = length;
                    minNodes = nodes;
                } else if (length == maxLen) {
                    minNodes = min(minNodes, nodes);
                }

                last_occurrence[nums[u]] = currentDepth;
            }

            int topDepthForChildren = st[currIdx].topDepth;
            bool pushed = false;
            while (st[currIdx].edgeIdx < (int)adj[u].size()) {
                auto& edge = adj[u][st[currIdx].edgeIdx++];
                if (edge.first != p) {
                    st.push_back({edge.first, u, currentDist + edge.second, currentDepth + 1, topDepthForChildren, 0, -1});
                    pushed = true;
                    break;
                }
            }

            if (!pushed) {
                // Backtrack: restore the state of last_occurrence
                last_occurrence[nums[u]] = st[currIdx].prevOcc;
                st.pop_back();
            }
        }

        return {maxLen, minNodes};
    }
};
# @lc code=end