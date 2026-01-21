#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> supersequences(vector<string>& words) {
        // Collect distinct letters
        bool used[26] = {false};
        for (auto &w : words) {
            used[w[0] - 'a'] = true;
            used[w[1] - 'a'] = true;
        }
        vector<int> letters;
        letters.reserve(26);
        for (int c = 0; c < 26; c++) if (used[c]) letters.push_back(c);
        int m = (int)letters.size();

        // Map letter -> compact index [0..m)
        int id[26];
        memset(id, -1, sizeof(id));
        for (int i = 0; i < m; i++) id[letters[i]] = i;

        // Required duplicates from "xx"
        int reqMask = 0;
        // Directed edges between distinct letters
        vector<pair<int,int>> edges;
        edges.reserve(words.size());
        {
            vector<vector<char>> seen(m, vector<char>(m, 0));
            for (auto &w : words) {
                int a = id[w[0] - 'a'];
                int b = id[w[1] - 'a'];
                if (a == b) {
                    reqMask |= (1 << a);
                } else {
                    if (!seen[a][b]) {
                        seen[a][b] = 1;
                        edges.push_back({a, b});
                    }
                }
            }
        }

        auto isDup = [&](int mask, int i) -> bool {
            return (mask >> i) & 1;
        };

        auto acyclic = [&](int mask) -> bool {
            int N = 2 * m;
            uint32_t adj[32];
            int indeg[32];
            for (int i = 0; i < N; i++) {
                adj[i] = 0;
                indeg[i] = 0;
            }

            auto addEdge = [&](int u, int v) {
                if (((adj[u] >> v) & 1u) == 0u) {
                    adj[u] |= (1u << v);
                    indeg[v]++;
                }
            };

            // Duplicate constraint: first -> last
            for (int i = 0; i < m; i++) {
                if (isDup(mask, i)) {
                    addEdge(2*i, 2*i + 1);
                }
            }

            // word constraints: first(x) -> last(y)
            for (auto [x, y] : edges) {
                int from = 2 * x; // first(x) always even
                int to = isDup(mask, y) ? (2 * y + 1) : (2 * y);
                addEdge(from, to);
            }

            // Kahn's algorithm
            deque<int> dq;
            for (int i = 0; i < N; i++) if (indeg[i] == 0) dq.push_back(i);
            int popped = 0;
            while (!dq.empty()) {
                int u = dq.front(); dq.pop_front();
                popped++;
                uint32_t out = adj[u];
                while (out) {
                    int v = __builtin_ctz(out);
                    out &= (out - 1);
                    if (--indeg[v] == 0) dq.push_back(v);
                }
            }
            return popped == N;
        };

        int best = INT_MAX;
        vector<int> bestMasks;
        int totalMasks = 1 << m;
        for (int mask = 0; mask < totalMasks; mask++) {
            if ((mask & reqMask) != reqMask) continue; // must include required duplicates
            int dupCnt = __builtin_popcount((unsigned)mask);
            if (dupCnt > best) continue;
            if (!acyclic(mask)) continue;
            if (dupCnt < best) {
                best = dupCnt;
                bestMasks.clear();
            }
            bestMasks.push_back(mask);
        }

        vector<vector<int>> ans;
        ans.reserve(bestMasks.size());
        for (int mask : bestMasks) {
            vector<int> freq(26, 0);
            for (int i = 0; i < m; i++) {
                int ch = letters[i];
                freq[ch] = 1 + ((mask >> i) & 1);
            }
            ans.push_back(std::move(freq));
        }
        return ans;
    }
};
// @lc code=end
