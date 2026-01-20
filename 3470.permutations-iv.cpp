#
# @lc app=leetcode id=3470 lang=cpp
#
# [3470] Permutations IV
#

# @lc code=start
class Solution {
public:
    vector<int> permute(int n, long long k) {
        // Precompute factorials with capping to prevent overflow
        // Since k <= 10^15, we can cap factorials slightly above that.
        long long MAX_K = 2000000000000000LL; // 2e15
        vector<long long> fact(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; ++i) {
            if (__builtin_mul_overflow(fact[i - 1], i, &fact[i])) {
                fact[i] = MAX_K;
            } else if (fact[i] > MAX_K) {
                fact[i] = MAX_K;
            }
        }

        vector<int> odds;
        vector<int> evens;
        for (int i = 1; i <= n; ++i) {
            if (i % 2 != 0) odds.push_back(i);
            else evens.push_back(i);
        }

        long long n_odd = odds.size();
        long long n_even = evens.size();
        
        // Calculate total valid permutations to check if k is valid
        long long total_permutations = 0;
        
        // Case 1: Start with Odd (O E O E ...)
        // Valid if n_odd == n_even or n_odd == n_even + 1
        // Since n_odd >= n_even always, this is always possible.
        long long ways_start_odd = 0;
        if (n_odd > 0) {
             // ways = (n_odd!) * (n_even!)
             // Using capped multiplication
             long long f_odd = fact[n_odd];
             long long f_even = fact[n_even];
             if (__builtin_mul_overflow(f_odd, f_even, &ways_start_odd)) ways_start_odd = MAX_K;
             else if (ways_start_odd > MAX_K) ways_start_odd = MAX_K;
        }

        // Case 2: Start with Even (E O E O ...)
        // Valid only if n_even == n_odd
        long long ways_start_even = 0;
        if (n_even == n_odd && n_even > 0) {
            long long f_odd = fact[n_odd];
            long long f_even = fact[n_even];
            if (__builtin_mul_overflow(f_odd, f_even, &ways_start_even)) ways_start_even = MAX_K;
            else if (ways_start_even > MAX_K) ways_start_even = MAX_K;
        }

        total_permutations = ways_start_odd + ways_start_even;
        if (total_permutations > MAX_K) total_permutations = MAX_K;

        if (k > total_permutations) return {};

        vector<int> result;
        bool next_is_odd = false; // Placeholder

        // Determine first element
        // Iterate 1 to n. 
        for (int val = 1; val <= n; ++val) {
            bool is_val_odd = (val % 2 != 0);
            long long ways = 0;

            if (is_val_odd) {
                // If we pick this odd number, we have (n_odd-1) odds and (n_even) evens left.
                // The pattern is fixed: next must be Even.
                // Remaining permutations count: (n_odd-1)! * (n_even)!
                long long rem_o = n_odd - 1;
                long long rem_e = n_even;
                
                // Check if this path is valid. 
                // If we start O, next is E. We need rem_e == rem_o or rem_e == rem_o + 1? 
                // No, pattern is O E O E... remaining length is n-1.
                // If start O, remaining pattern starts E.
                // Remaining counts: rem_o, rem_e.
                // Valid if rem_e == rem_o or rem_e == rem_o + 1.
                // Since original n_odd >= n_even, rem_o = n_odd - 1. 
                // If n_odd == n_even, rem_o = n_even - 1. rem_e = n_even. rem_e = rem_o + 1. Valid.
                // If n_odd == n_even + 1, rem_o = n_even. rem_e = n_even. rem_e = rem_o. Valid.
                // So starting with Odd is always valid structure-wise.

                long long f1 = fact[rem_o];
                long long f2 = fact[rem_e];
                if (__builtin_mul_overflow(f1, f2, &ways)) ways = MAX_K;
                else if (ways > MAX_K) ways = MAX_K;

                if (k <= ways) {
                    result.push_back(val);
                    // Remove val from odds
                    for(auto it = odds.begin(); it != odds.end(); ++it) if(*it == val) { odds.erase(it); break; }
                    next_is_odd = false;
                    goto first_found;
                } else {
                    k -= ways;
                }
            } else {
                // val is Even
                // Valid only if we can start with Even. i.e., n_even == n_odd.
                if (n_even != n_odd) continue; 

                long long rem_o = n_odd;
                long long rem_e = n_even - 1;
                
                // Remaining pattern starts O. Valid if rem_o == rem_e or rem_o == rem_e + 1.
                // Since n_even == n_odd, rem_o = n_even, rem_e = n_even - 1. rem_o = rem_e + 1. Valid.

                long long f1 = fact[rem_o];
                long long f2 = fact[rem_e];
                if (__builtin_mul_overflow(f1, f2, &ways)) ways = MAX_K;
                else if (ways > MAX_K) ways = MAX_K;

                if (k <= ways) {
                    result.push_back(val);
                    for(auto it = evens.begin(); it != evens.end(); ++it) if(*it == val) { evens.erase(it); break; }
                    next_is_odd = true;
                    goto first_found;
                } else {
                    k -= ways;
                }
            }
        }

        first_found:
        
        // Fill the rest
        for (int i = 1; i < n; ++i) {
            long long rem_o = odds.size();
            long long rem_e = evens.size();
            
            vector<int>* candidates = next_is_odd ? &odds : &evens;
            
            // We iterate through available candidates of the required parity
            // We can't use a range-based for loop easily because we might erase. 
            // But we break immediately after erasing, so it's okay, but index based is safer or just careful iterators.
            // Since we need to find the specific one, let's just iterate by index.
            for (int j = 0; j < candidates->size(); ++j) {
                int val = (*candidates)[j];
                long long ways = 0;
                
                // Calculate ways if we pick this val
                // Remaining counts will decrease by 1 for the chosen parity
                long long next_rem_o = rem_o;
                long long next_rem_e = rem_e;
                if (next_is_odd) next_rem_o--;
                else next_rem_e--;

                long long f1 = fact[next_rem_o];
                long long f2 = fact[next_rem_e];
                if (__builtin_mul_overflow(f1, f2, &ways)) ways = MAX_K;
                else if (ways > MAX_K) ways = MAX_K;

                if (k <= ways) {
                    result.push_back(val);
                    candidates->erase(candidates->begin() + j);
                    next_is_odd = !next_is_odd;
                    break; // Move to next position i
                } else {
                    k -= ways;
                }
            }
        }

        return result;
    }
};
# @lc code=end