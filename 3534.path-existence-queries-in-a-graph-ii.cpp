# @lc app=leetcode id=3534 lang=cpp
#
# [3534] Path Existence Queries in a Graph II
#
# @lc code=start
#include <vector>
#include <algorithm>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class DSU {
public:
    vector<int> parent, rank;
    DSU(int n) : parent(n), rank(n, 1) {
        for (int i = 0; i < n; ++i) parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int x, int y) {
        int xr = find(x), yr = find(y);
        if (xr == yr) return;
        if (rank[xr] < rank[yr]) swap(xr, yr);
        parent[yr] = xr;
        if (rank[xr] == rank[yr]) rank[xr]++;
    }
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
};

class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<pair<int,int>> numidx(n);
        for (int i = 0; i < n; ++i) numidx[i] = {nums[i], i};
        sort(numidx.begin(), numidx.end());
        DSU dsu(n);
        int left = 0;
        for (int right = 0; right < n; ++right) {
            while (numidx[right].first - numidx[left].first > maxDiff) ++left;
            for (int i = left; i < right; ++i) {
                dsu.unite(numidx[right].second, numidx[i].second);
            }
        }
        vector<vector<int>> adj(n);
        left = 0;
        for (int right = 0; right < n; ++right) {
            while (numidx[right].first - numidx[left].first > maxDiff) ++left;
            for (int i = left; i < right; ++i) {
                int u = numidx[right].second, v = numidx[i].second;
                adj[u].push_back(v);
                adj[v].push_back(u);
            }
        }
        vector<int> answer(queries.size(), -1);
        for (int i = 0; i < queries.size(); ++i) {
            int u = queries[i][0], v = queries[i][1];
            if (u == v) {
                answer[i] = 0;
            } else if (!dsu.connected(u, v)) {
                answer[i] = -1;
            }
        }
        unordered_map<int, unordered_map<int, int>> cache;
        for (int i = 0; i < queries.size(); ++i) {
            int u = queries[i][0], v = queries[i][1];
            if (u == v || !dsu.connected(u, v)) continue;
            if (cache.count(u) && cache[u].count(v)) {
                answer[i] = cache[u][v];
                continue;
            }
            vector<int> dist(n, -1);
            queue<int> q;
            dist[u] = 0;
            q.push(u);
            bool found = false;
            while (!q.empty()) {
                int x = q.front(); q.pop();
                for (int y : adj[x]) {
                    if (dist[y] == -1) {
                        dist[y] = dist[x] + 1;
                        if (y == v) {
                            answer[i] = dist[y];
                            cache[u][v] = dist[y];
                            found = true;
                            break;
                        }
                        q.push(y);
                    }
                }
                if (found) break;
            }
        }
        return answer;
    }
};
# @lc code=end