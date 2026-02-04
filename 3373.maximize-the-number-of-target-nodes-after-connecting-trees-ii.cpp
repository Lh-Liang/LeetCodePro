#\n# @lc app=leetcode id=3373 lang=cpp\n#\n# [3373] Maximize the Number of Target Nodes After Connecting Trees II\n#\n\n# @lc code=start\n#include <vector>\n#include <queue>\nusing namespace std;\nclass Solution {\npublic:\n    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {\n        int n = edges1.size() + 1; \n        int m = edges2.size() + 1; \n        vector<vector<int>> adjList1(n), adjList2(m);\n        \n        // Create adjacency list for both trees\n        for (auto &edge : edges1) {\n            adjList1[edge[0]].push_back(edge[1]);\n            adjList1[edge[1]].push_back(edge[0]);\n        }\n        for (auto &edge : edges2) {\n            adjList2[edge[0]].push_back(edge[1]);\n            adjList2[edge[1]].push_back(edge[0]);\n        }\n
        // Function to calculate distances using BFS
        auto bfsDistances = [](int start, const vector<vector<int>>& adjList) {
            int size = adjList.size();
            vector<int> distance(size, -1);
            queue<int> q;
            q.push(start);
            distance[start] = 0;
            while (!q.empty()) {
                int node = q.front(); q.pop();
                for (int neighbor : adjList[node]) {
                    if (distance[neighbor] == -1) { // Not visited
                        distance[neighbor] = distance[node] + 1;
                        q.push(neighbor);
                    }
                }
            }
            return distance;
        };
bfsDistances(0,adjList2);return {};} };