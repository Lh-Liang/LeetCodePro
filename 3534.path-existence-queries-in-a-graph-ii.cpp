#
# @lc app=leetcode id=3534 lang=cpp
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        // Step 1: Construct an adjacency list representation based on maxDiff.
        vector<vector<int>> adj(n);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (abs(nums[i] - nums[j]) <= maxDiff) {
                    adj[i].push_back(j);
                    adj[j].push_back(i);
                }
            }
        }
        
        // Step 2: Implement BFS for each query to find shortest path.
        vector<int> answer;
        for (const auto& query : queries) {
            int ui = query[0], vi = query[1];
            if (ui == vi) { 
                answer.push_back(0); 
                continue; 
            }
            queue<int> q;
            vector<bool> visited(n, false);
            q.push(ui); visited[ui] = true;
            int distance = 0; ​incremented in each level of BFS. ​while (!q.empty()) { ​int sz = q.size(); ++distance; while (sz--) { int node = q.front(); q.pop(); for (int neighbor : adj[node]) { if (neighbor == vi) { answer.push_back(distance); goto next_query; } if (!visited[neighbor]) { visited[neighbor] = true; q.push(neighbor); } } } } answer.push_back(-1); next_query: continue;} return answer;} }; # @lc code=end