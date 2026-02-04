#
# @lc app=leetcode id=3695 lang=cpp
#
# [3695] Maximize Alternating Sum Using Swaps
#
# @lc code=start
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution {
public:
    // Union-Find structure with path compression and union by rank
    class UnionFind {
    private:
        vector<int> parent, rank;
    public:
        UnionFind(int size) : parent(size), rank(size, 0) {
            for (int i = 0; i < size; ++i) {
                parent[i] = i;
            }
        }
        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]); // Path compression
            }
            return parent[x];
        }
        void unionSets(int x, int y) {
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
        }
    };

    long long maxAlternatingSum(vector<int>& nums, vector<vector<int>>& swaps) {
        int n = nums.size();
        UnionFind uf(n);
        for (const auto& swap : swaps) {
            uf.unionSets(swap[0], swap[1]);
        }

        unordered_map<int, vector<int>> components;
        for (int i = 0; i < n; ++i) {
            components[uf.find(i)].push_back(nums[i]);
        }

        long long maxSum = 0;
nint index = 0;
nfor (auto& [root, componentNums] : components) {\nnsort(componentNums.begin(), componentNums.end(), greater<int>());\nnfor (int num : componentNums) {\nnmaxSum += (index % 2 == 0 ? num : -num);\nnindex++;\nn}\nn}\nnreturn maxSum;n}
n};
n# @lc code=end