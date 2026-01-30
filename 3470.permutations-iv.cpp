#
# @lc app=leetcode id=3470 lang=cpp
#
# [3470] Permutations IV
#
# @lc code=start
#include <vector>

using namespace std;

class Solution {
    long long factorial[101];
    const long long INF = 2000000000000000LL; // Cap at 2e15 to handle k <= 10^15

    void precompute() {
        factorial[0] = 1;
        for (int i = 1; i <= 100; ++i) {
            if (factorial[i - 1] > INF / i) factorial[i] = INF;
            else factorial[i] = factorial[i - 1] * i;
        }
    }

    long long safe_mul(long long a, long long b) {
        if (a == 0 || b == 0) return 0;
        if (a > INF / b) return INF;
        return a * b;
    }

    // m: remaining slots, O: remaining odd numbers, E: remaining even numbers, next_p: parity of next slot
    long long get_ways(int m, int O, int E, int next_p) {
        if (m == 0) return 1;
        // Calculate required slots for Odd and Even based on alternating parity
        int reqO = 0, reqE = 0;
        if (next_p == 1) { // Next slot must be Odd
            reqO = (m + 1) / 2;
            reqE = m / 2;
        } else { // Next slot must be Even
            reqE = (m + 1) / 2;
            reqO = m / 2;
        }
        
        if (O != reqO || E != reqE) return 0;
        return safe_mul(factorial[O], factorial[E]);
    }

public:
    vector<int> permute(int n, long long k) {
        precompute();
        vector<int> res;
        vector<bool> used(n + 1, false);
        int O = (n + 1) / 2;
        int E = n / 2;

        for (int i = 0; i < n; ++i) {
            bool found = false;
            for (int j = 1; j <= n; ++j) {
                if (!used[j]) {
                    // Check parity constraint: must alternate
                    if (!res.empty() && (j % 2 == res.back() % 2)) continue;

                    int next_O = (j % 2 == 1) ? O - 1 : O;
                    int next_E = (j % 2 == 0) ? E - 1 : E;
                    
                    // If we pick j, the next slot must have parity 1 - (j%2)
                    long long ways = get_ways(n - 1 - i, next_O, next_E, 1 - (j % 2));
                    
                    if (k <= ways) {
                        res.push_back(j);
                        used[j] = true;
                        O = next_O;
                        E = next_E;
                        found = true;
                        break;
                    } else {
                        k -= ways;
                    }
                }
            }
            if (!found) return {};
        }

        return res;
    }
};
# @lc code=end