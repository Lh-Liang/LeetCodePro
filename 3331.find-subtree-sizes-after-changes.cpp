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
        
        // Build adjacency list for the original tree
        vector<vector<int>> children(n);
        for (int i = 1; i < n; i++) {
            children[parent[i]].push_back(i);
        }
        
        // New parent array
        vector<int> newParent = parent;
        
        // Stack for each character to track ancestors (closest ancestor at back)
        vector<vector<int>> charStack(26);
        
        // DFS to find new parents based on closest ancestor with same character
        function<void(int)> dfs1 = [&](int node) {
            int charIdx = s[node] - 'a';
            
            // If there's an ancestor with the same character, update parent
            if (!charStack[charIdx].empty()) {
                newParent[node] = charStack[charIdx].back();
            }
            
            // Push current node to its character stack
            charStack[charIdx].push_back(node);
            
            // Visit children in original tree
            for (int child : children[node]) {
                dfs1(child);
            }
            
            // Pop current node from its character stack when leaving
            charStack[charIdx].pop_back();
        };
        
        dfs1(0);
        
        // Build new tree based on new parent relationships
        vector<vector<int>> newChildren(n);
        for (int i = 1; i < n; i++) {
            newChildren[newParent[i]].push_back(i);
        }
        
        // Calculate subtree sizes in the new tree
        vector<int> answer(n, 0);
        
        function<int(int)> dfs2 = [&](int node) -> int {
            int size = 1;
            for (int child : newChildren[node]) {
                size += dfs2(child);
            }
            answer[node] = size;
            return size;
        };
        
        dfs2(0);
        
        return answer;
    }
};
# @lc code=end