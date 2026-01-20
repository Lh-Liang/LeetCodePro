#
# @lc app=leetcode id=3695 lang=cpp
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums, vector<vector<int>>& swaps) {
        int n = nums.size();
        vector<vector<int>> adj(n);
        for (const auto& swap : swaps) {
            adj[swap[0]].push_back(swap[1]);
            adj[swap[1]].push_back(swap[0]);
        }

        vector<bool> visited(n, false);
        long long totalSum = 0;

        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                vector<int> componentValues;
                int evenIndicesCount = 0;
                
                // BFS to find component
                vector<int> q;
                q.push_back(i);
                visited[i] = true;
                
                int head = 0;
                while(head < q.size()){
                    int u = q[head++];
                    componentValues.push_back(nums[u]);
                    if (u % 2 == 0) {
                        evenIndicesCount++;
                    }
                    
                    for (int v : adj[u]) {
                        if (!visited[v]) {
                            visited[v] = true;
                            q.push_back(v);
                        }
                    }
                }

                // Sort values descending
                sort(componentValues.begin(), componentValues.end(), greater<int>());

                // Assign largest values to even indices (add)
                // Assign smallest values to odd indices (subtract)
                for (int k = 0; k < componentValues.size(); ++k) {
                    if (k < evenIndicesCount) {
                        totalSum += componentValues[k];
                    } else {
                        totalSum -= componentValues[k];
                    }
                }
            }
        }

        return totalSum;
    }
};
# @lc code=end