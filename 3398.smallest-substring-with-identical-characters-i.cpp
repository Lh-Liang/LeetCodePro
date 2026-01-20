#
# @lc app=leetcode id=3398 lang=cpp
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution {
public:
    bool check(int maxLen, const string& s, int numOps) {
        int n = s.length();
        if (maxLen == 1) {
            // Special case for maxLen = 1: the string must be strictly alternating.
            // Pattern 1: 010101...
            // Pattern 2: 101010...
            int ops1 = 0;
            int ops2 = 0;
            for (int i = 0; i < n; ++i) {
                if (s[i] != (i % 2 == 0 ? '0' : '1')) ops1++;
                if (s[i] != (i % 2 == 0 ? '1' : '0')) ops2++;
            }
            return min(ops1, ops2) <= numOps;
        }

        int opsNeeded = 0;
        int currentRun = 0;
        char currentChar = 0;

        for (int i = 0; i < n; ++i) {
            if (i == 0 || s[i] == currentChar) {
                currentRun++;
                currentChar = s[i];
            } else {
                // End of a run
                if (currentRun > maxLen) {
                    opsNeeded += currentRun / (maxLen + 1);
                }
                currentRun = 1;
                currentChar = s[i];
            }
        }
        // Check the last run
        if (currentRun > maxLen) {
            opsNeeded += currentRun / (maxLen + 1);
        }

        return opsNeeded <= numOps;
    }

    int minLength(string s, int numOps) {
        int n = s.length();
        int low = 1, high = n;
        int ans = n;

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