#
# @lc app=leetcode id=3686 lang=cpp
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
#include <vector>

using namespace std;

class Solution {
public:
    int countStableSubsequences(vector<int>& nums) {
        long long lastE = 0, lastEE = 0, lastO = 0, lastOO = 0;
        const int MOD = 1000000007;

        for (int x : nums) {
            if (x % 2 == 0) {
                // If current number is even, it can:
                // 1. Start a new subsequence [E]
                // 2. Append to any stable subseq ending in O or OO to form ...O, E or ...OO, E
                // 3. Append to any stable subseq ending in exactly one E to form ...E, E
                long long ways_to_make_E = (lastO + lastOO + 1) % MOD;
                long long ways_to_make_EE = lastE;
                
                lastE = (lastE + ways_to_make_E) % MOD;
                lastEE = (lastEE + ways_to_make_EE) % MOD;
            } else {
                // If current number is odd, it can:
                // 1. Start a new subsequence [O]
                // 2. Append to any stable subseq ending in E or EE to form ...E, O or ...EE, O
                // 3. Append to any stable subseq ending in exactly one O to form ...O, O
                long long ways_to_make_O = (lastE + lastEE + 1) % MOD;
                long long ways_to_make_OO = lastO;
                
                lastO = (lastO + ways_to_make_O) % MOD;
                lastOO = (lastOO + ways_to_make_OO) % MOD;
            }
        }

        long long total = (lastE + lastEE + lastO + lastOO) % MOD;
        return (int)total;
    }
};
# @lc code=end