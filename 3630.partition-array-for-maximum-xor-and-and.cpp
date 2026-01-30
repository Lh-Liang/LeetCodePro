#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maximizeXorAndXor(vector<int>& nums) {
        int n = nums.size();
        int num_masks = 1 << n;
        
        // Precompute XOR and AND for all possible subsets in O(2^n)
        vector<unsigned int> xor_vals(num_masks, 0);
        vector<unsigned int> and_vals(num_masks, 0);

        for (int i = 0; i < n; ++i) {
            int bit = 1 << i;
            for (int mask = 0; mask < bit; ++mask) {
                xor_vals[mask | bit] = xor_vals[mask] ^ (unsigned int)nums[i];
                if (mask == 0) {
                    and_vals[mask | bit] = (unsigned int)nums[i];
                } else {
                    and_vals[mask | bit] = and_vals[mask] & (unsigned int)nums[i];
                }
            }
        }

        long long max_total = 0;
        int full_mask = num_masks - 1;

        // Iterate through all 2^n possible subsets for subsequence B
        // The remaining elements (R) are partitioned into A and C to maximize XOR(A) + XOR(C)
        for (int b_mask = 0; b_mask <= full_mask; ++b_mask) {
            unsigned int b_and = and_vals[b_mask];
            int r_mask = full_mask ^ b_mask;
            unsigned int r_xor = xor_vals[r_mask];
            
            // Mathematical identity: XOR(A) + XOR(C) = XOR(R) + 2 * (XOR(A) & XOR(C))
            // We maximize (XOR(A) & XOR(C)) by finding max XOR sum of {nums[i] & ~XOR(R) | i in R}
            unsigned int target_mask = ~r_xor;
            unsigned int basis[31] = {0};
            
            int temp_r = r_mask;
            while (temp_r > 0) {
                int i = __builtin_ctz(temp_r);
                unsigned int val = (unsigned int)nums[i] & target_mask;
                
                // Insert into linear basis
                for (int j = 29; j >= 0; --j) {
                    if (!(val & (1U << j))) continue;
                    if (!basis[j]) {
                        basis[j] = val;
                        break;
                    }
                    val ^= basis[j];
                }
                temp_r &= (temp_r - 1); // Remove the lowest set bit
            }

            // Find maximum XOR sum achievable from the basis
            unsigned int max_and_bits = 0;
            for (int j = 29; j >= 0; --j) {
                if ((max_and_bits ^ basis[j]) > max_and_bits) {
                    max_and_bits ^= basis[j];
                }
            }

            long long current_val = (long long)r_xor + 2LL * max_and_bits + b_and;
            if (current_val > max_total) {
                max_total = current_val;
            }
        }

        return max_total;
    }
};