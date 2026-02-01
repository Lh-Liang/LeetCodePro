#include <string>
#include <algorithm>
#include <vector>

using namespace std;

# @lc app=leetcode id=3398 lang=cpp
# [3398] Smallest Substring With Identical Characters I

# @lc code=start
class Solution {
public:
    /**
     * Helper function to check if it's possible to make the longest identical substring length <= k
     * using at most numOps flips.
     */
    bool check(int k, const string& s, int numOps) {
        int n = s.length();
        if (k == 1) {
            // For k=1, the string must alternate: 0101... or 1010...
            int count1 = 0, count2 = 0;
            for (int i = 0; i < n; ++i) {
                // Compare with 010101...
                if (s[i] != (i % 2 == 0 ? '0' : '1')) count1++;
                // Compare with 101010...
                if (s[i] != (i % 2 == 0 ? '1' : '0')) count2++;
            }
            return min(count1, count2) <= numOps;
        } else {
            // For k > 1, greedily break blocks of identical characters.
            int total_flips = 0;
            int current_len = 1;
            for (int i = 1; i < n; ++i) {
                if (s[i] == s[i - 1]) {
                    current_len++;
                } else {
                    // Minimum flips to break a block of length L into segments of max length k is L / (k + 1).
                    total_flips += current_len / (k + 1);
                    current_len = 1;
                }
            }
            total_flips += current_len / (k + 1);
            return total_flips <= numOps;
        }
    }

    int minLength(string s, int numOps) {
        int n = s.length();
        int low = 1, high = n;
        int ans = n;

        // Binary search for the smallest possible maximum length k.
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check(mid, s, numOps)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return ans;
    }
};
# @lc code=end