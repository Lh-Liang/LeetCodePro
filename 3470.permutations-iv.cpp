#
# @lc app=leetcode id=3470 lang=cpp
#
# [3470] Permutations IV
#
# @lc code=start
class Solution {
public:
    vector<int> permute(int n, long long k) {
        const long long INF = 2e15;
        
        // Precompute factorials with overflow protection
        vector<long long> fact(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = min(INF, fact[i-1] * i);
        }
        
        // Safe multiplication
        auto safe_mult = [INF](long long a, long long b) -> long long {
            if (a == 0 || b == 0) return 0;
            if (a > INF / b) return INF;
            return a * b;
        };
        
        // Count permutations for remaining positions
        auto count_perms = [&](int rem, int next_parity, int odd_left, int even_left) -> long long {
            if (rem == 0) return 1;
            int odd_needed, even_needed;
            if (next_parity == 1) { // odd needed first
                odd_needed = (rem + 1) / 2;
                even_needed = rem / 2;
            } else { // even needed first
                even_needed = (rem + 1) / 2;
                odd_needed = rem / 2;
            }
            if (odd_left != odd_needed || even_left != even_needed) return 0;
            return safe_mult(fact[odd_left], fact[even_left]);
        };
        
        // Initialize available numbers
        set<int> odd_avail, even_avail;
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 1) odd_avail.insert(i);
            else even_avail.insert(i);
        }
        
        vector<int> result;
        k--; // Convert to 0-indexed
        
        for (int pos = 0; pos < n; pos++) {
            int rem = n - pos - 1;
            bool found = false;
            
            vector<int> candidates;
            if (pos == 0) {
                for (int x : odd_avail) candidates.push_back(x);
                for (int x : even_avail) candidates.push_back(x);
                sort(candidates.begin(), candidates.end());
            } else {
                int required_parity = 1 - (result.back() % 2);
                if (required_parity == 1) {
                    candidates.assign(odd_avail.begin(), odd_avail.end());
                } else {
                    candidates.assign(even_avail.begin(), even_avail.end());
                }
            }
            
            for (int num : candidates) {
                int parity = num % 2;
                int next_parity = 1 - parity;
                int new_odd = (int)odd_avail.size() - (parity == 1 ? 1 : 0);
                int new_even = (int)even_avail.size() - (parity == 0 ? 1 : 0);
                
                long long cnt = count_perms(rem, next_parity, new_odd, new_even);
                
                if (k < cnt) {
                    result.push_back(num);
                    if (parity == 1) odd_avail.erase(num);
                    else even_avail.erase(num);
                    found = true;
                    break;
                }
                k -= cnt;
            }
            
            if (!found) return {};
        }
        
        return result;
    }
};
# @lc code=end