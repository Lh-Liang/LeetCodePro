#
# @lc app=leetcode id=3776 lang=cpp
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    long long minMoves(vector<int>& balance) {
        long long total = 0; // To store total moves needed.
        int n = balance.size();
        int negIndex = -1; // Index of negative balance if any.
        for (int i = 0; i < n; ++i) {
            if (balance[i] < 0) negIndex = i; // Identify negative balance index.
            total += abs(balance[i]); // Calculate total absolute balances.
        }
        if (negIndex == -1) return 0; // No need to move if no negatives.
        vector<long long> prefix(n+1, 0); 
        for (int i = 1; i <= n; ++i) prefix[i] = prefix[i-1] + balance[i-1]; // Prefix sum calculation.
        auto check = [&]() -> bool { 
            for (int i = 0; i < n; ++i) { 
                if (prefix[i] - prefix[negIndex] < 0 || prefix[n] - prefix[negIndex] + prefix[i] < 0) return false; 
            } 
            return true; 
        }; 
        return check() ? total : -1; // Return total moves or -1 if impossible.
    }
};
# @lc code=end