#
# @lc app=leetcode id=3786 lang=cpp
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#
# @lc code=start
class Solution {
public:
    long long interactionCosts(int n, vector<vector<int>>& edges, vector<int>& group) {
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        
        vector<int> totalCount(21, 0);
        for (int i = 0; i < n; i++) {
            totalCount[group[i]]++;
        }
        
        vector<vector<int>> subtreeCount(n, vector<int>(21, 0));
        long long result = 0;
        
        function<void(int, int)> dfs = [&](int node, int parent) {
            subtreeCount[node][group[node]] = 1;
            
            for (int child : adj[node]) {
                if (child == parent) continue;
                dfs(child, node);
                
                for (int g = 1; g <= 20; g++) {
                    long long inSubtree = subtreeCount[child][g];
                    long long outside = totalCount[g] - inSubtree;
                    result += inSubtree * outside;
                }
                
                for (int g = 1; g <= 20; g++) {
                    subtreeCount[node][g] += subtreeCount[child][g];
                }
            }
        };
        
        dfs(0, -1);
        
        return result;
    }
};
# @lc code=end