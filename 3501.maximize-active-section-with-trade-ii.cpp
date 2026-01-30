#
# @lc app=leetcode id=3501 lang=cpp
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.length();
        int total_ones = 0;
        for (char c : s) if (c == '1') total_ones++;

        struct Block {
            int l, r, gain_left, gain_right, total_gain;
        };
        vector<Block> tradeable;
        
        vector<pair<int, int>> segs;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && s[j] == s[i]) j++;
            segs.push_back({i, j - 1});
            i = j;
        }

        for (int k = 1; k < (int)segs.size() - 1; ++k) {
            int l = segs[k].first, r = segs[k].second;
            if (s[l] == '1' && s[l-1] == '0' && s[r+1] == '0') {
                int gl = segs[k-1].second - segs[k-1].first + 1;
                int gr = segs[k+1].second - segs[k+1].first + 1;
                tradeable.push_back({l, r, gl, gr, gl + gr});
            }
        }

        int m = tradeable.size();
        if (m == 0) return vector<int>(queries.size(), total_ones);

        int max_log = 32 - __builtin_clz(m);
        vector<vector<int>> st(max_log, vector<int>(m));
        for (int i = 0; i < m; i++) st[0][i] = tradeable[i].total_gain;
        for (int j = 1; j < max_log; j++) {
            for (int i = 0; i + (1 << j) <= m; i++) {
                st[j][i] = max(st[j-1][i], st[j-1][i + (1 << (j-1))]);
            }
        }

        auto query_st = [&](int L, int R) {
            if (L > R) return 0;
            int j = 31 - __builtin_clz(R - L + 1);
            return max(st[j][L], st[j][R - (1 << j) + 1]);
        };

        vector<int> results;
        for (const auto& q : queries) {
            int li = q[0], ri = q[1];
            int start = -1, end = -1;
            
            int low = 0, high = m - 1;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (tradeable[mid].l >= li) { start = mid; high = mid - 1; } else low = mid + 1;
            }
            low = 0, high = m - 1;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (tradeable[mid].r <= ri) { end = mid; low = mid + 1; } else high = mid - 1;
            }

            if (start != -1 && end != -1 && start <= end) {
                int current_max = 0;
                // Boundary: start block
                current_max = max(current_max, min(tradeable[start].gain_left, tradeable[start].l - li) + 
                                             (start == end ? min(tradeable[start].gain_right, ri - tradeable[start].r) : tradeable[start].gain_right));
                
                // Boundary: end block
                if (start < end) {
                    current_max = max(current_max, tradeable[end].gain_left + min(tradeable[end].gain_right, ri - tradeable[end].r));
                }

                // Internal blocks
                if (start + 1 <= end - 1) {
                    current_max = max(current_max, query_st(start + 1, end - 1));
                }
                results.push_back(total_ones + current_max);
            } else {
                results.push_back(total_ones);
            }
        }
        return results;
    }
};
# @lc code=end