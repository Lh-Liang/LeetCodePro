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
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }
        
        vector<long long> dist = {0};
        unordered_map<int, int> last;
        unordered_map<int, int> secondLast;
        
        long long maxLen = 0;
        int minNodes = 1;
        
        function<void(int, int, long long, int, int)> dfs = [&](int u, int parent, long long d, int left, int boundary) {
            int idx = dist.size() - 1;
            int v = nums[u];
            
            int oldLast = last.count(v) ? last[v] : -1;
            int oldSecondLast = secondLast.count(v) ? secondLast[v] : -1;
            
            int prevOcc = oldLast;
            int secondPrevOcc = oldSecondLast;
            
            // Handle "3 occurrences" constraint
            if (secondPrevOcc >= left) {
                left = secondPrevOcc + 1;
            }
            
            // Recheck boundary validity
            if (boundary < left) {
                boundary = -1;
            }
            
            // Handle "at most one duplicate" constraint
            if (prevOcc >= left) {
                if (boundary >= left) {
                    // Two duplicates, remove the older one
                    if (boundary < prevOcc) {
                        left = max(left, boundary + 1);
                        boundary = (prevOcc >= left) ? prevOcc : -1;
                    } else {
                        left = max(left, prevOcc + 1);
                        boundary = (boundary >= left) ? boundary : -1;
                    }
                } else {
                    boundary = prevOcc;
                }
            }
            
            // Update tracking
            if (oldLast >= 0) {
                secondLast[v] = oldLast;
            }
            last[v] = idx;
            
            // Update answer
            long long pathLen = d - dist[left];
            int nodeCount = idx - left + 1;
            if (pathLen > maxLen || (pathLen == maxLen && nodeCount < minNodes)) {
                maxLen = pathLen;
                minNodes = nodeCount;
            }
            
            // Recurse
            for (auto& [next, w] : adj[u]) {
                if (next != parent) {
                    dist.push_back(d + w);
                    dfs(next, u, d + w, left, boundary);
                    dist.pop_back();
                }
            }
            
            // Backtrack
            if (oldLast >= 0) {
                last[v] = oldLast;
            } else {
                last.erase(v);
            }
            
            if (oldSecondLast >= 0) {
                secondLast[v] = oldSecondLast;
            } else {
                secondLast.erase(v);
            }
        };
        
        dfs(0, -1, 0, 0, -1);
        
        return {(int)maxLen, minNodes};
    }
};
# @lc code=end