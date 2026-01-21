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
        vector<int> newParent(n);
        newParent[0] = -1;
        
        // For each node from 1 to n-1, find its new parent
        for (int x = 1; x < n; x++) {
            char ch = s[x];
            int curr = parent[x];
            int closestAncestor = -1;
            
            // Traverse up to find closest ancestor with same character
            while (curr != -1) {
                if (s[curr] == ch) {
                    closestAncestor = curr;
                    break;
                }
                curr = parent[curr];
            }
            
            if (closestAncestor != -1) {
                newParent[x] = closestAncestor;
            } else {
                newParent[x] = parent[x];
            }
        }
        
        // Build new tree adjacency list
        vector<vector<int>> children(n);
        for (int i = 1; i < n; i++) {
            children[newParent[i]].push_back(i);
        }
        
        // Calculate subtree sizes using DFS
        vector<int> answer(n);
        function<int(int)> dfs = [&](int node) -> int {
            int size = 1;
            for (int child : children[node]) {
                size += dfs(child);
            }
            answer[node] = size;
            return size;
        };
        
        dfs(0);
        return answer;
    }
};
# @lc code=end