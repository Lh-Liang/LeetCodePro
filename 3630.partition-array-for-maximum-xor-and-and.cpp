#
# @lc app=leetcode id=3630 lang=cpp
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
class Solution {
public:
    long long maximizeXorAndXor(vector<int>& nums) {
        int n = nums.size();
        long long max_val = 0;
        int total_subsets = 1 << n;

        // Precompute powers of 2 for bit checking might be slightly faster, 
        // but standard shifts are fine.

        for (int i = 0; i < total_subsets; ++i) {
            long long current_and_b = 0;
            int xor_r = 0;
            
            // We need a linear basis for elements NOT in B (i.e., in R)
            // A basis of size 30 is sufficient for integers up to 10^9
            vector<int> basis;
            
            bool first_b = true;

            for (int j = 0; j < n; ++j) {
                if ((i >> j) & 1) {
                    // Element nums[j] is in B
                    if (first_b) {
                        current_and_b = nums[j];
                        first_b = false;
                    } else {
                        current_and_b &= nums[j];
                    }
                } else {
                    // Element nums[j] is in R (A or C)
                    int val = nums[j];
                    xor_r ^= val;
                    
                    // Insert into basis
                    for (int b : basis) {
                        val = min(val, val ^ b);
                    }
                    if (val > 0) {
                        basis.push_back(val);
                        // Keep basis sorted to process MSB first or just sort later.
                        // Standard insert usually maintains structure or requires sort.
                        // Let's just insert and sort at the end of this subset processing.
                        // Actually, standard Gaussian elimination insert:
                        // If we iterate existing basis and reduce `val`, the result `val` 
                        // has a unique MSB not present in other basis elements.
                        // Sorting the basis descending helps the greedy approach.
                        int k = basis.size() - 1;
                        while (k > 0 && basis[k] > basis[k-1]) {
                            swap(basis[k], basis[k-1]);
                            k--;
                        }
                    }
                }
            }
            
            // If B is empty, current_and_b remains 0 (as per problem statement AND([]) = 0)
            if (first_b) current_and_b = 0;

            // Now we want to choose v from basis span to maximize v + (v ^ xor_r)
            int v = 0;
            for (int b : basis) {
                // Try to include this basis element
                int v_next = v ^ b;
                long long val_curr = (long long)v + (v ^ xor_r);
                long long val_next = (long long)v_next + (v_next ^ xor_r);
                if (val_next > val_curr) {
                    v = v_next;
                }
            }

            long long current_total = (long long)v + (v ^ xor_r) + current_and_b;
            if (current_total > max_val) {
                max_val = current_total;
            }
        }

        return max_val;
    }
};
# @lc code=end