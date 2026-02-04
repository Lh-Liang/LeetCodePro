#
# @lc app=leetcode id=3399 lang=cpp
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution {
public:
    int minLength(string s, int numOps) {
        int n = s.size();
        int left = 1, right = n, answer = n;
        while (left <= right) {
            int mid = (left + right) / 2;
            // Check if it's possible to break all substrings of length mid
            if (canBreak(s, numOps, mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return answer;
    }

private:
    // Returns true if all substrings of length len can be broken into not all identical
    bool canBreak(const string& s, int numOps, int len) {
        int n = s.size();
        // Try to flip to all '0' or all '1' in every window
        // Precompute prefix sums for '0' and '1'
        vector<int> pre0(n+1, 0), pre1(n+1, 0);
        for (int i = 0; i < n; ++i) {
            pre0[i+1] = pre0[i] + (s[i] == '0');
            pre1[i+1] = pre1[i] + (s[i] == '1');
        }
        for (int i = 0; i + len <= n; ++i) {
            int zeroCount = pre0[i+len] - pre0[i];
            int oneCount = pre1[i+len] - pre1[i];
            // Flips needed to make all '0' or all '1'
            int flipTo0 = len - zeroCount;
            int flipTo1 = len - oneCount;
            if (flipTo0 <= numOps || flipTo1 <= numOps) return true;
        }
        return false;
    }
};
# @lc code=end