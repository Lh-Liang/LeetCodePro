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
        vector<vector<int>> children(n);
        vector<int> answer(n, 1);
        unordered_map<char, int> charAncestor; // Map to store last seen ancestor for each character.
        
        // Build initial tree structure
        for (int i = 1; i < n; ++i) {
            children[parent[i]].push_back(i);
        }
        
        function<void(int)> dfs = [&](int node) {
            char currentChar = s[node];
            int previousAncestor = -1;
            if (charAncestor.find(currentChar) != charAncestor.end()) {
                previousAncestor = charAncestor[currentChar];
                // Reparent if valid ancestor found
                if (previousAncestor != -1 && previousAncestor != parent[node]) {
                    // Update tree structure by changing parent relationships
                    auto& siblings = children[parent[node]];
                    siblings.erase(remove(siblings.begin(), siblings.end(), node), siblings.end());
                    children[previousAncestor].push_back(node);
                    parent[node] = previousAncestor;
                }
            }
            
            // Update last seen ancestor for this character
            charAncestor[currentChar] = node;
            
            // Visit all children and calculate subtree sizes
            for (int child : children[node]) {
                dfs(child);
                answer[node] += answer[child];
            }
            
            // Restore previous state after returning from recursion
            charAncestor[currentChar] = previousAncestor;
        };
        
dfs(0); // Start DFS from root node
        return answer;
    }
};
# @lc code=end