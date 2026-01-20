#
# @lc app=leetcode id=3399 lang=cpp
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution {
public:
    int minLength(string s, int numOps) {
        int n = s.length();
        
        // Check specifically for length 1
        // Target patterns are "010101..." or "101010..."
        int opsPattern1 = 0;
        int opsPattern2 = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] != (i % 2 == 0 ? '0' : '1')) opsPattern1++;
            if (s[i] != (i % 2 == 0 ? '1' : '0')) opsPattern2++;
        }
        if (min(opsPattern1, opsPattern2) <= numOps) return 1;

        // Binary search for the minimum length k in range [2, n]
        int low = 2;
        int high = n;
        int ans = n;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check(s, numOps, mid)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

private:
    bool check(const string& s, int numOps, int k) {
        int opsNeeded = 0;
        int currentRun = 0;
        char lastChar = '\0';

        for (char c : s) {
            if (c == lastChar) {
                currentRun++;
            } else {
                if (currentRun > 0) {
                    opsNeeded += currentRun / (k + 1);
                }
                currentRun = 1;
                lastChar = c;
            }
        }
        if (currentRun > 0) {
            opsNeeded += currentRun / (k + 1);
        }

        return opsNeeded <= numOps;
    }
};
# @lc code=end