#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

class Solution {
    struct Block {
        int val; // 0 or 1
        int len;
        int start_idx;
        int end_idx;
    };
    
    vector<Block> blocks;
    vector<int> block_starts;
    
    // Sparse Tables
    vector<vector<int>> st_max_0;
    vector<vector<int>> st_min_1;
    vector<vector<int>> st_max_merge;
    vector<int> lg;
    
    void buildST(int n_blocks) {
        lg.resize(n_blocks + 1);
        lg[1] = 0;
        for (int i = 2; i <= n_blocks; i++)
            lg[i] = lg[i/2] + 1;
            
        int K = lg[n_blocks] + 1;
        
        st_max_0.assign(n_blocks, vector<int>(K, -1e9));
        st_min_1.assign(n_blocks, vector<int>(K, 1e9));
        st_max_merge.assign(n_blocks, vector<int>(K, -1e9));
        
        for (int i = 0; i < n_blocks; i++) {
            if (blocks[i].val == 0) {
                st_max_0[i][0] = blocks[i].len;
            } else {
                st_min_1[i][0] = blocks[i].len;
                // Merge val valid only for internal 1-blocks with neighbors
                if (i > 0 && i < n_blocks - 1) {
                    st_max_merge[i][0] = blocks[i-1].len + blocks[i+1].len;
                }
            }
        }
        
        for (int j = 1; j < K; j++) {
            for (int i = 0; i + (1 << j) <= n_blocks; i++) {
                st_max_0[i][j] = max(st_max_0[i][j-1], st_max_0[i + (1 << (j-1))][j-1]);
                st_min_1[i][j] = min(st_min_1[i][j-1], st_min_1[i + (1 << (j-1))][j-1]);
                st_max_merge[i][j] = max(st_max_merge[i][j-1], st_max_merge[i + (1 << (j-1))][j-1]);
            }
        }
    }
    
    int queryMax0(int L, int R) {
        if (L > R) return -1e9;
        int j = lg[R - L + 1];
        return max(st_max_0[L][j], st_max_0[R - (1 << j) + 1][j]);
    }
    
    int queryMin1(int L, int R) {
        if (L > R) return 1e9;
        int j = lg[R - L + 1];
        return min(st_min_1[L][j], st_min_1[R - (1 << j) + 1][j]);
    }
    
    int queryMaxMerge(int L, int R) {
        if (L > R) return -1e9;
        int j = lg[R - L + 1];
        return max(st_max_merge[L][j], st_max_merge[R - (1 << j) + 1][j]);
    }
    
    vector<long long> pref_1;

public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.length();
        blocks.clear();
        
        if (n == 0) return {};
        
        int start = 0;
        for (int i = 0; i < n; i++) {
            if (i == n - 1 || s[i] != s[i+1]) {
                blocks.push_back({s[i] - '0', i - start + 1, start, i});
                start = i + 1;
            }
        }
        
        int m = blocks.size();
        block_starts.resize(m);
        pref_1.assign(m + 1, 0);
        
        for(int i=0; i<m; ++i) {
            block_starts[i] = blocks[i].start_idx;
            pref_1[i+1] = pref_1[i] + (blocks[i].val == 1 ? blocks[i].len : 0);
        }
        
        buildST(m);
        
        vector<int> ans;
        ans.reserve(queries.size());
        
        for (auto& q : queries) {
            int l = q[0];
            int r = q[1];
            
            auto it_u = upper_bound(block_starts.begin(), block_starts.end(), l);
            int u = prev(it_u) - block_starts.begin();
            
            auto it_v = upper_bound(block_starts.begin(), block_starts.end(), r);
            int v = prev(it_v) - block_starts.begin();
            
            int base_count = 0;
            
            if (u == v) {
                if (blocks[u].val == 1) base_count = r - l + 1;
                ans.push_back(base_count);
                continue;
            }
            
            int len_u = blocks[u].end_idx - l + 1;
            if (blocks[u].val == 1) base_count += len_u;
            
            int len_v = r - blocks[v].start_idx + 1;
            if (blocks[v].val == 1) base_count += len_v;
            
            if (u + 1 <= v - 1) {
                base_count += (pref_1[v] - pref_1[u+1]);
            }
            
            int start_search = u + 1;
            int end_search = v - 1;
            
            if (start_search > end_search) {
                ans.push_back(base_count);
                continue;
            }
            
            int max_z = -1e9;
            if (blocks[u].val == 0) max_z = max(max_z, len_u);
            if (blocks[v].val == 0) max_z = max(max_z, len_v);
            max_z = max(max_z, queryMax0(start_search, end_search));
            
            int max_gain = 0;
            
            // 1. Boundary victim at u+1
            if (blocks[u+1].val == 1) {
                int v_len = blocks[u+1].len;
                int left_len = len_u;
                int right_len = 0;
                if (u + 2 < v) right_len = blocks[u+2].len;
                else if (u + 2 == v) right_len = len_v;
                
                int merge_g = left_len + right_len;
                int sep_g = max_z - v_len;
                max_gain = max(max_gain, max(merge_g, sep_g));
            }
            
            // 2. Boundary victim at v-1
            if (v - 1 > u + 1 && blocks[v-1].val == 1) {
                int v_len = blocks[v-1].len;
                int right_len = len_v;
                int left_len = blocks[v-2].len;
                
                int merge_g = left_len + right_len;
                int sep_g = max_z - v_len;
                max_gain = max(max_gain, max(merge_g, sep_g));
            }
            
            // 3. Middle victims
            if (start_search + 1 <= end_search - 1) {
                int q_l = start_search + 1;
                int q_r = end_search - 1;
                
                int best_merge = queryMaxMerge(q_l, q_r);
                int min_v = queryMin1(q_l, q_r);
                
                if (best_merge > -1e9) max_gain = max(max_gain, best_merge);
                if (min_v < 1e9) max_gain = max(max_gain, max_z - min_v);
            }
            
            ans.push_back(base_count + max_gain);
        }
        
        return ans;
    }
};