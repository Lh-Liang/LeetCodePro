#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> supersequences(vector<string>& words) {
        vector<int> present_chars;
        int char_to_idx[26];
        fill(char_to_idx, char_to_idx + 26, -1);
        
        for (const string& w : words) {
            for (char c : w) {
                int code = c - 'a';
                if (char_to_idx[code] == -1) {
                    char_to_idx[code] = (int)present_chars.size();
                    present_chars.push_back(code);
                }
            }
        }
        
        int n = (int)present_chars.size();
        if (n == 0) return {};

        int must_two = 0;
        int adj[16] = {0};
        
        for (const string& w : words) {
            int u = char_to_idx[w[0] - 'a'];
            int v = char_to_idx[w[1] - 'a'];
            if (u == v) {
                must_two |= (1 << u);
            } else {
                adj[u] |= (1 << v);
            }
        }
        
        // dp[mask] = true if the subgraph induced by nodes in mask is a DAG
        vector<bool> dp(1 << n, false);
        dp[0] = true;
        for (int mask = 1; mask < (1 << n); ++mask) {
            for (int i = 0; i < n; ++i) {
                if ((mask >> i) & 1) {
                    // If node i can be a sink (no edges to other nodes in the mask)
                    // and the rest of the mask is a DAG, then this mask is a DAG.
                    if (!(adj[i] & mask) && dp[mask ^ (1 << i)]) {
                        dp[mask] = true;
                        break;
                    }
                }
            }
        }
        
        int max_s1_size = -1;
        vector<int> best_masks;
        
        for (int mask = 0; mask < (1 << n); ++mask) {
            if (dp[mask] && !(mask & must_two)) {
                int current_size = __builtin_popcount(mask);
                if (current_size > max_s1_size) {
                    max_s1_size = current_size;
                    best_masks = {mask};
                } else if (current_size == max_s1_size) {
                    best_masks.push_back(mask);
                }
            }
        }
        
        vector<vector<int>> result;
        for (int mask : best_masks) {
            vector<int> freq(26, 0);
            for (int i = 0; i < n; ++i) {
                freq[present_chars[i]] = ((mask >> i) & 1) ? 1 : 2;
            }
            result.push_back(freq);
        }
        
        return result;
    }
};