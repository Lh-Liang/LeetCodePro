#
# @lc app=leetcode id=3486 lang=cpp
#
# [3486] Longest Special Path II
#
# @lc code=start
class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        vector<vector<pair<int, int>>> adj(n);
        
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        
        vector<long long> prefix;
        unordered_map<int, vector<int>> positions;
        
        multiset<int, greater<int>> hardBounds;
        multiset<int, greater<int>> softBounds;
        
        long long maxLen = 0;
        int minNodes = INT_MAX;
        
        function<void(int, int, long long)> dfs = [&](int u, int par, long long dist) {
            int idx = prefix.size();
            prefix.push_back(dist);
            
            int v = nums[u];
            auto& pos = positions[v];
            int m = pos.size();
            
            if (m == 1) {
                softBounds.insert(pos[0]);
            } else if (m == 2) {
                softBounds.erase(softBounds.find(pos[0]));
                softBounds.insert(pos[1]);
                hardBounds.insert(pos[0]);
            } else if (m >= 3) {
                hardBounds.erase(hardBounds.find(pos[m-3]));
                hardBounds.insert(pos[m-2]);
                softBounds.erase(softBounds.find(pos[m-2]));
                softBounds.insert(pos[m-1]);
            }
            
            pos.push_back(idx);
            
            int hardMax = hardBounds.empty() ? -1 : *hardBounds.begin();
            int soft2 = -1;
            if (softBounds.size() >= 2) {
                auto it = softBounds.begin();
                ++it;
                soft2 = *it;
            }
            
            int minStart = max(hardMax, soft2) + 1;
            
            long long len = dist - prefix[minStart];
            int numNodes = idx - minStart + 1;
            
            if (len > maxLen || (len == maxLen && numNodes < minNodes)) {
                maxLen = len;
                minNodes = numNodes;
            }
            
            for (auto& [child, w] : adj[u]) {
                if (child != par) {
                    dfs(child, u, dist + w);
                }
            }
            
            pos.pop_back();
            
            if (m == 1) {
                softBounds.erase(softBounds.find(pos[0]));
            } else if (m == 2) {
                softBounds.erase(softBounds.find(pos[1]));
                softBounds.insert(pos[0]);
                hardBounds.erase(hardBounds.find(pos[0]));
            } else if (m >= 3) {
                hardBounds.erase(hardBounds.find(pos[m-2]));
                hardBounds.insert(pos[m-3]);
                softBounds.erase(softBounds.find(pos[m-1]));
                softBounds.insert(pos[m-2]);
            }
            
            prefix.pop_back();
        };
        
        dfs(0, -1, 0);
        
        return {(int)maxLen, minNodes};
    }
};
# @lc code=end