#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

#
# @lc app=leetcode id=3435 lang=cpp
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
class Solution {
public:
    vector<vector<int>> supersequences(vector<string>& words) {
        std::unordered_map<char, int> char_to_id;
        std::vector<char> id_to_char;
        
        // Identify unique characters
        for (const std::string& w : words) {
            for (char c : w) {
                if (char_to_id.find(c) == char_to_id.end()) {
                    char_to_id[c] = id_to_char.size();
                    id_to_char.push_back(c);
                }
            }
        }

        int n = id_to_char.size();
        std::vector<int> adj(n, 0);
        for (const std::string& w : words) {
            int u = char_to_id[w[0]];
            int v = char_to_id[w[1]];
            adj[u] |= (1 << v);
        }

        // DP to find all masks that form a DAG
        std::vector<bool> is_dag(1 << n, false);
        is_dag[0] = true;
        int max_dag_size = 0;

        for (int mask = 1; mask < (1 << n); ++mask) {
            for (int i = 0; i < n; ++i) {
                if ((mask >> i) & 1) {
                    // A vertex i can be the last in the topological sort if it has no outgoing edges to the mask
                    if ((adj[i] & mask) == 0 && is_dag[mask ^ (1 << i)]) {
                        is_dag[mask] = true;
                        break;
                    }
                }
            }
            if (is_dag[mask]) {
                max_dag_size = std::max(max_dag_size, (int)__builtin_popcount(mask));
            }
        }

        // Collect all frequency distributions for the minimum SCS length
        std::vector<std::vector<int>> result;
        for (int mask = 0; mask < (1 << n); ++mask) {
            if (is_dag[mask] && __builtin_popcount(mask) == max_dag_size) {
                std::vector<int> freq(26, 0);
                for (int i = 0; i < n; ++i) {
                    if ((mask >> i) & 1) {
                        freq[id_to_char[i] - 'a'] = 1;
                    } else {
                        freq[id_to_char[i] - 'a'] = 2;
                    }
                }
                result.push_back(freq);
            }
        }

        return result;
    }
};
# @lc code=end