#
# @lc app=leetcode id=3470 lang=cpp
#
# [3470] Permutations IV
#
# @lc code=start
#include <vector>

using namespace std;

class Solution {
    long long cap = 2e15; // Slightly more than the maximum k (1e15)

    // Safe multiplication to avoid overflow, capping at 'cap'
    long long safe_mul(long long a, long long b) {
        if (a == 0 || b == 0) return 0;
        if (a > cap / b) return cap;
        return a * b;
    }

    long long factorial[101];

    // Precompute factorials up to n=100, capped at 'cap'
    void precompute() {
        factorial[0] = 1;
        for (int i = 1; i <= 100; ++i) {
            factorial[i] = safe_mul(factorial[i - 1], i);
        }
    }

public:
    vector<int> permute(int n, long long k) {
        precompute();
        vector<int> res;
        vector<bool> used(n + 1, false);
        int n_odd = (n + 1) / 2;
        int n_even = n / 2;

        int last_parity = -1;

        for (int i = 0; i < n; ++i) {
            bool found = false;
            for (int v = 1; v <= n; ++v) {
                if (used[v]) continue;
                
                int p = v % 2; // 1 for odd, 0 for even
                // Check if the current number maintains the alternating parity
                if (last_parity != -1 && p == last_parity) continue;

                // Calculate the number of ways to complete the permutation
                int rem_len = n - 1 - i;
                int rem_odd = n_odd - (p == 1 ? 1 : 0);
                int rem_even = n_even - (p == 0 ? 1 : 0);

                long long ways = 0;
                if (rem_len == 0) {
                    ways = 1; // Only one way to complete an empty sequence
                } else {
                    int next_p = 1 - p;
                    // Count available numbers of the required next parity and the other parity
                    int n_req = (next_p == 1 ? rem_odd : rem_even);
                    int n_other = (next_p == 1 ? rem_even : rem_odd);

                    // For an alternating sequence of length L starting with parity P:
                    // If L is even, we need L/2 of parity P and L/2 of the other.
                    // If L is odd, we need (L+1)/2 of parity P and (L-1)/2 of the other.
                    if (rem_len % 2 == 0) {
                        if (n_req == rem_len / 2 && n_other == rem_len / 2) {
                            ways = safe_mul(factorial[n_req], factorial[n_other]);
                        }
                    } else {
                        if (n_req == (rem_len + 1) / 2 && n_other == (rem_len - 1) / 2) {
                            ways = safe_mul(factorial[n_req], factorial[n_other]);
                        }
                    }
                }

                // If k is within the number of ways, pick this number
                if (k <= ways) {
                    res.push_back(v);
                    used[v] = true;
                    if (p == 1) n_odd--; else n_even--;
                    last_parity = p;
                    found = true;
                    break;
                } else {
                    // Otherwise, skip all permutations starting with this number
                    k -= ways;
                }
            }
            // If no valid number is found for the current position, the k-th permutation doesn't exist
            if (!found) return {};
        }

        return res;
    }
};
# @lc code=end