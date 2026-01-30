#
# @lc app=leetcode id=3435 lang=cpp
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> supersequences(vector<string>& words) {
        int charMap[26];
        fill(charMap, charMap + 26, -1);
        vector<int> indexToChar;
        int n = 0;

        for (const string& s : words) {
            for (char c : s) {
                if (charMap[c - 'a'] == -1) {
                    charMap[c - 'a'] = n++;
                    indexToChar.push_back(c - 'a');
                }
            }
        }

        int adj[16][16] = {0};
        int mandatory = 0;
        for (const string& s : words) {
            int u = charMap[s[0] - 'a'];
            int v = charMap[s[1] - 'a'];
            if (u == v) {
                mandatory |= (1 << u);
            } else {
                adj[u][v] = 1;
            }
        }

        int minDoubles = n + 1;
        vector<int> validMasks;

        for (int mask = 0; mask < (1 << n); ++mask) {
            if ((mask & mandatory) != mandatory) continue;
            
            int doubles = __builtin_popcount(mask);
            if (doubles > minDoubles) continue;

            // Check if nodes NOT in mask form a DAG
            int inDegree[16] = {0};
            int activeNodes = 0;
            int activeMask = ((1 << n) - 1) ^ mask;
            
            for (int i = 0; i < n; ++i) {
                if (activeMask & (1 << i)) {
                    activeNodes++;
                    for (int j = 0; j < n; ++j) {
                        if ((activeMask & (1 << j)) && adj[i][j]) {
                            inDegree[j]++;
                        }
                    }
                }
            }

            int q[16], head = 0, tail = 0;
            for (int i = 0; i < n; ++i) {
                if ((activeMask & (1 << i)) && inDegree[i] == 0) q[tail++] = i;
            }

            int visited = 0;
            while (head < tail) {
                int u = q[head++];
                visited++;
                for (int v = 0; v < n; ++v) {
                    if ((activeMask & (1 << v)) && adj[u][v]) {
                        if (--inDegree[v] == 0) q[tail++] = v;
                    }
                }
            }

            if (visited == activeNodes) {
                if (doubles < minDoubles) {
                    minDoubles = doubles;
                    validMasks.clear();
                }
                validMasks.push_back(mask);
            }
        }

        vector<vector<int>> result;
        for (int mask : validMasks) {
            vector<int> freq(26, 0);
            for (int i = 0; i < n; ++i) {
                freq[indexToChar[i]] = (mask & (1 << i)) ? 2 : 1;
            }
            result.push_back(freq);
        }
        return result;
    }
};
# @lc code=end