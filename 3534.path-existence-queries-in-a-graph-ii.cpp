# @lc code=start
class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<vector<int>> adj(n);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (abs(nums[i] - nums[j]) <= maxDiff) {
                    adj[i].push_back(j);
                    adj[j].push_back(i);
                }
            }
        }
        vector<int> answer;
        for (const auto& query : queries) {
            int ui = query[0], vi = query[1];
            if (ui == vi) {
                answer.push_back(0);
                continue;
            }
            vector<int> dist(n, -1);
            queue<int> q;
            q.push(ui);
            dist[ui] = 0;
            bool found = false;
            while (!q.empty() && !found) {
                int node = q.front();
                q.pop();
                for (int neighbor : adj[node]) {
                    if (dist[neighbor] == -1) { // not visited
                        dist[neighbor] = dist[node] + 1;
                        if (neighbor == vi) {
                            answer.push_back(dist[neighbor]);
                            found = true;
                            break;
                        }
                        q.push(neighbor);
                    }
                }
            }
            if (!found) answer.push_back(-1);
        }
        return answer;
    }
};
# @lc code=end