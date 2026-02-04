#
# @lc app=leetcode id=3367 lang=cpp
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
class Solution {
public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        // Sort edges by weight in descending order
        sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[2] > b[2];
        });
        
        // Initialize connection count for each node
        unordered_map<int, int> connectionCount;
        long long maxWeightSum = 0;
        
        // Iterate through sorted edges and add them if possible
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1], weight = edge[2];
            if (connectionCount[u] < k && connectionCount[v] < k) {
                maxWeightSum += weight;
                connectionCount[u]++;
                connectionCount[v]++;
            }
        }
        
        return maxWeightSum;
    }
};
# @lc code=end