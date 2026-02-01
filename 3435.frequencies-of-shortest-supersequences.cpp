#
# @lc app=leetcode id=3435 lang=cpp
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<vector<int>> supersequences(vector<string>& words) {
        // Step 1: Identify all unique characters present in the words.
        // There are at most 16 unique characters according to the constraints.
        vector<int> present_chars;
        vector<int> char_to_id(26, -1);
        for (const string& w : words) {
            for (char c : w) {
                if (char_to_id[c - 'a'] == -1) {
                    char_to_id[c - 'a'] = present_chars.size();
                    present_chars.push_back(c - 'a');
                }
            }
        }

        int n = present_chars.size();
        int must_twice = 0;
        vector<int> adj_in(n, 0);

        // Step 2: Build the dependency graph.
        // If words[i] = "uv", then u must appear before v if they both appear once.
        // If u == v, then u must appear at least twice.
        for (const string& w : words) {
            int u = char_to_id[w[0] - 'a'];
            int v = char_to_id[w[1] - 'a'];
            if (u == v) {
                must_twice |= (1 << u);
            } else {
                adj_in[v] |= (1 << u);
            }
        }

        // Step 3: Find all subsets of characters that can appear only once.
        // A subset of characters can appear only once if the dependency graph induced 
        // by them is a Directed Acyclic Graph (DAG). 
        // We use dynamic programming to find all masks that represent a DAG.
        vector<bool> is_dag(1 << n, false);
        is_dag[0] = true;
        for (int mask = 1; mask < (1 << n); ++mask) {
            for (int i = 0; i < n; ++i) {
                if ((mask >> i) & 1) {
                    // Check if node i has no incoming edges from other nodes in the mask.
                    if (!(adj_in[i] & mask)) {
                        if (is_dag[mask ^ (1 << i)]) {
                            is_dag[mask] = true;
                            break;
                        }
                    }
                }
            }
        }

        // Step 4: Find the maximum size of such a subset (to minimize total length).
        // The length of the supersequence is 2 * |UniqueChars| - |SubsetSize|.
        int max_o = -1;
        vector<int> best_masks;
        for (int mask = 0; mask < (1 << n); ++mask) {
            if (is_dag[mask] && !(mask & must_twice)) {
                int size = __builtin_popcount(mask);
                if (size > max_o) {
                    max_o = size;
                    best_masks = {mask};
                } else if (size == max_o) {
                    best_masks.push_back(mask);
                }
            }
        }

        // Step 5: Construct the frequency arrays for each optimal subset.
        vector<vector<int>> result;
        for (int mask : best_masks) {
            vector<int> freq(26, 0);
            for (int i = 0; i < n; ++i) {
                int char_idx = present_chars[i];
                if ((mask >> i) & 1) {
                    freq[char_idx] = 1; // Appears once
                } else {
                    freq[char_idx] = 2; // Appears twice
                }
            }
            result.push_back(freq);
        }

        return result;
    }
};
# @lc code=end