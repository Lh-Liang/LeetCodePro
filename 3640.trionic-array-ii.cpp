//
// @lc app=leetcode id=3640 lang=cpp
//
// [3640] Trionic Array II
//
// @lc code=start
class Solution {
public:
    long long maxSumTrionic(vector<int>& nums) {
        int n = nums.size();
        
        // Phase 1: First increasing segment
        vector<long long> inc_sum(n);
        vector<int> inc_len(n);
        
        // Phase 2: Decreasing segment (after inc of len >= 2)
        vector<long long> dec_sum(n, LLONG_MIN);
        vector<int> dec_len(n, 0);
        
        // Phase 3: Second increasing segment (trionic completion)
        vector<long long> tri_sum(n, LLONG_MIN);
        vector<int> tri_len(n, 0);
        
        inc_sum[0] = nums[0];
        inc_len[0] = 1;
        
        long long ans = LLONG_MIN;
        
        for (int i = 1; i < n; i++) {
            // Update first increasing phase
            if (nums[i] > nums[i-1]) {
                inc_sum[i] = inc_sum[i-1] + nums[i];
                inc_len[i] = inc_len[i-1] + 1;
            } else {
                inc_sum[i] = nums[i];
                inc_len[i] = 1;
            }
            
            // Update decreasing phase
            if (nums[i] < nums[i-1]) {
                // Transition from inc to dec (need inc_len >= 2)
                if (inc_len[i-1] >= 2) {
                    long long cand = inc_sum[i-1] + nums[i];
                    if (cand > dec_sum[i]) {
                        dec_sum[i] = cand;
                        dec_len[i] = 2;
                    }
                }
                // Continue dec (need dec_len >= 2)
                if (dec_len[i-1] >= 2) {
                    long long cand = dec_sum[i-1] + nums[i];
                    if (cand > dec_sum[i]) {
                        dec_sum[i] = cand;
                        dec_len[i] = dec_len[i-1] + 1;
                    }
                }
            }
            
            // Update second increasing phase (trionic)
            if (nums[i] > nums[i-1]) {
                // Transition from dec to tri (need dec_len >= 2)
                if (dec_len[i-1] >= 2) {
                    long long cand = dec_sum[i-1] + nums[i];
                    if (cand > tri_sum[i]) {
                        tri_sum[i] = cand;
                        tri_len[i] = 2;
                    }
                }
                // Continue tri (need tri_len >= 2)
                if (tri_len[i-1] >= 2) {
                    long long cand = tri_sum[i-1] + nums[i];
                    if (cand > tri_sum[i]) {
                        tri_sum[i] = cand;
                        tri_len[i] = tri_len[i-1] + 1;
                    }
                }
            }
            
            // Update answer (need tri_len >= 2 for valid trionic)
            if (tri_len[i] >= 2) {
                ans = max(ans, tri_sum[i]);
            }
        }
        
        return ans;
    }
};
// @lc code=end