//
// @lc app=leetcode id=3721 lang=cpp
//
// [3721] Longest Balanced Subarray II
//
// @lc code=start
class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        
        int block_size = max(1, (int)sqrt(n));
        int num_blocks = (n + block_size - 1) / block_size;
        
        vector<long long> base(n, 0);
        vector<long long> lazy(num_blocks, 0);
        vector<unordered_map<long long, int>> block_map(num_blocks);
        
        auto get_block = [&](int i) { return i / block_size; };
        auto block_start = [&](int b) { return b * block_size; };
        auto block_end = [&](int b) { return min((b + 1) * block_size, n); };
        
        auto rebuild = [&](int b) {
            block_map[b].clear();
            for (int i = block_start(b); i < block_end(b); i++) {
                if (block_map[b].find(base[i]) == block_map[b].end()) {
                    block_map[b][base[i]] = i;
                }
            }
        };
        
        for (int b = 0; b < num_blocks; b++) {
            rebuild(b);
        }
        
        auto pushdown = [&](int b) {
            if (lazy[b] != 0) {
                for (int i = block_start(b); i < block_end(b); i++) {
                    base[i] += lazy[b];
                }
                lazy[b] = 0;
                rebuild(b);
            }
        };
        
        auto update = [&](int l, int r, long long delta) {
            if (l > r) return;
            int bl = get_block(l), br = get_block(r);
            if (bl == br) {
                pushdown(bl);
                for (int i = l; i <= r; i++) {
                    base[i] += delta;
                }
                rebuild(bl);
            } else {
                pushdown(bl);
                for (int i = l; i < block_end(bl); i++) {
                    base[i] += delta;
                }
                rebuild(bl);
                
                for (int b = bl + 1; b < br; b++) {
                    lazy[b] += delta;
                }
                
                pushdown(br);
                for (int i = block_start(br); i <= r; i++) {
                    base[i] += delta;
                }
                rebuild(br);
            }
        };
        
        auto query = [&](int query_r) -> int {
            int br = get_block(query_r);
            for (int b = 0; b <= br; b++) {
                long long query_key = -lazy[b];
                if (b < br) {
                    auto it = block_map[b].find(query_key);
                    if (it != block_map[b].end()) {
                        return it->second;
                    }
                } else {
                    for (int i = block_start(b); i <= query_r; i++) {
                        if (base[i] + lazy[b] == 0) {
                            return i;
                        }
                    }
                }
            }
            return -1;
        };
        
        unordered_map<int, int> last_occurrence;
        int max_len = 0;
        
        for (int r = 0; r < n; r++) {
            int v = nums[r];
            long long delta = (v % 2 == 0) ? 1 : -1;
            
            int prev = (last_occurrence.count(v) ? last_occurrence[v] : -1);
            
            update(prev + 1, r, delta);
            
            int l = query(r);
            if (l != -1) {
                max_len = max(max_len, r - l + 1);
            }
            
            last_occurrence[v] = r;
        }
        
        return max_len;
    }
};
// @lc code=end