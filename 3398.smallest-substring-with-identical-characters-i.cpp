#
# @lc app=leetcode id=3398 lang=cpp
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    /**
     * Check if it is possible to make the maximum identical substring length <= k
     * using at most numOps operations.
     */
    bool check(int k, const string& s, int numOps) {
        int n = s.length();
        
        // Special case for k = 1: The string must become alternating.
        if (k == 1) {
            int flips0 = 0; // Target: 010101...
            int flips1 = 0; // Target: 101010...
            for (int i = 0; i < n; ++i) {
                if (s[i] != (i % 2 == 0 ? '0' : '1')) flips0++;
                if (s[i] != (i % 2 == 0 ? '1' : '0')) flips1++;
            }
            return min(flips0, flips1) <= numOps;
        }

        // Case k >= 2: Use greedy approach on contiguous blocks.
        int totalFlips = 0;
        int currentLen = 1;
        for (int i = 1; i < n; ++i) {
            if (s[i] == s[i - 1]) {
                currentLen++;
            } else {
                totalFlips += currentLen / (k + 1);
                currentLen = 1;
            }
        }
        totalFlips += currentLen / (k + 1);
        
        return totalFlips <= numOps;
    }

    int minLength(string s, int numOps) {
        int n = s.length();
        int left = 1, right = n;
        int ans = n;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid, s, numOps)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return ans;
    }
};
# @lc code=end