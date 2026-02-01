#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:
    vector<vector<int>> supersequences(vector<string>& words) {
        unordered_map<char, int> char_to_idx;
        vector<char> idx_to_char;
        for (const string& w : words) {
            for (char c : w) {
                if (char_to_idx.find(c) == char_to_idx.end()) {
                    char_to_idx[c] = idx_to_char.size();
                    idx_to_char.push_back(c);
                }
            }
        }

        int n = idx_to_char.size();
        vector<pair<int, int>> edges;
        for (const string& w : words) {
            if (w[0] != w[1]) {
                edges.push_back({char_to_idx[w[0]], char_to_idx[w[1]]});
            }
        }

        auto is_dag = [&](int mask) {
            vector<int> in_degree(n, 0);
            vector<vector<int>> adj(n);
            int count = 0;
            for (auto& edge : edges) {
                if (((mask >> edge.first) & 1) && ((mask >> edge.second) & 1)) {
                    adj[edge.first].push_back(edge.second);
                    in_degree[edge.second]++;
                }
            }

            queue<int> q;
            for (int i = 0; i < n; ++i) {
                if (((mask >> i) & 1)) {
                    count++;
                    if (in_degree[i] == 0) q.push(i);
                }
            }

            int visited = 0;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                visited++;
                for (int v : adj[u]) {
                    if (--in_degree[v] == 0) q.push(v);
                }
            }
            return visited == count;
        };

        int max_nodes = 0;
        vector<int> best_masks;

        for (int mask = 0; mask < (1 << n); ++mask) {
            int bits = __builtin_popcount(mask);
            if (bits < max_nodes) continue;

            if (is_dag(mask)) {
                if (bits > max_nodes) {
                    max_nodes = bits;
                    best_masks.clear();
                }
                best_masks.push_back(mask);
            }
        }

        vector<vector<int>> results;
        for (int mask : best_masks) {
            vector<int> freq(26, 0);
            for (int i = 0; i < n; ++i) {
                int char_idx = idx_to_char[i] - 'a';
                if ((mask >> i) & 1) freq[char_idx] = 1;
                else freq[char_idx] = 2;
            }
            results.push_back(freq);
        }

        return results;
    }
};