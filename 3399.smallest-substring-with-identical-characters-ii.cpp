#
# @lc app=leetcode id=3399 lang=cpp
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    /**
     * Helper function to check if it is possible to achieve a maximum identical substring length of k
     * within numOps operations.
     */
    bool check(int k, const string& s, int numOps) {
        int n = s.length();
        
        // Special case for k = 1: The string must be alternating (0101... or 1010...)
        if (k == 1) {
            int ops1 = 0;
            for (int i = 0; i < n; ++i) {
                // Check against pattern 0101...
                if (s[i] - '0' != (i % 2)) {
                    ops1++;
                }
            }
            // ops1 is flips for 0101..., ops2 for 1010... is n - ops1
            return min(ops1, n - ops1) <= numOps;
        }

        // General case for k > 1: Use greedy approach on contiguous blocks
        int totalOps = 0;
        int currentBlockLen = 0;
        for (int i = 0; i < n; ++i) {
            if (i > 0 && s[i] == s[i - 1]) {
                currentBlockLen++;
            } else {
                totalOps += currentBlockLen / (k + 1);
                currentBlockLen = 1;
            }
        }
        // Add flips for the last block
        totalOps += currentBlockLen / (k + 1);
        
        return totalOps <= numOps;
    }

    int minLength(string s, int numOps) {
        int n = s.length();
        int left = 1, right = n;
        int result = n;

        // Binary search for the minimum possible k
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid, s, numOps)) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return result;
    }
};
# @lc code=end