# @lc app=leetcode id=3534 lang=cpp
#
# [3534] Path Existence Queries in a Graph II
#
# @lc code=start
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<int> parent(n);
        vector<int> rank(n, 0);
        vector<vector<int>> adjList(n); // Adjacency list for BFS
        vector<int> result(queries.size(), -1);

        // Helper functions for Union-Find with path compression and union by rank
        function<int(int)> find = [&](int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        };

        auto unionSet = [&](int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX != rootY) {
                if (rank[rootX] > rank[rootY]) {
                    parent[rootY] = rootX;
                } else if (rank[rootX] < rank[rootY]) {
                    parent[rootX] = rootY;
                } else {
                    parent[rootY] = rootX;
                    rank[rootX]++;
                }
            }
        };

        // Initialize Union-Find structure with each node as its own parent initially
        iota(parent.begin(), parent.end(), 0);

        // Create edges based on maxDiff condition using sorting to reduce complexity
        vector<pair<int, int>> indexedNums(n);
        for (int i = 0; i < n; ++i) {
            indexedNums[i] = {nums[i], i};
        }
        sort(indexedNums.begin(), indexedNums.end());

        // Build adjacency list only for valid connections within maxDiff range using sorted order
        for (int i = 0; i < n; ++i) {	for (int j = i + 1; j < n && (indexedNums[j].first - indexedNums[i].first <= maxDiff); ++j) { unionSet(indexedNums[i].second, indexedNums[j].second); adjList[indexedNums[i].second].push_back(indexedNums[j].second); adjList[indexedNums[j].second].push_back(indexedNums[i].second); } }	// Process each query and determine connectivity using Union-Find and BFS if necessary	for (int qIdx = 0; qIdx < queries.size(); ++qIdx) { auto [u, v] = queries[qIdx]; if (find(u) == find(v)) { // If connected in same component // Use BFS to find shortest path length queue<pair<int,int>> qBFS; vector<bool> visited(n, false); qBFS.push({u, 0}); visited[u] = true; bool found = false; while (!qBFS.empty()) { auto [node, dist] = qBFS.front(); qBFS.pop(); if (node == v) { result[qIdx] = dist; found = true; break; } for (auto neighbor : adjList[node]) { if (!visited[neighbor]) { visited[neighbor] = true; qBFS.push({neighbor, dist + 1}); } } } if (!found) { result[qIdx] = -1; } // If not found after BFS } else { result[qIdx] = -1; // Nodes not connected } } return result;} }; # @lc code=end