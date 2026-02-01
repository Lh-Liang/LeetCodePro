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
    int minLength(string s, int numOps) {
        int n = s.length();
        int low = 1, high = n;
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
        int n = s.length();
        if (k == 1) {
            int cnt0 = 0; // target 0101...
            for (int i = 0; i < n; ++i) {
                if (s[i] != (i % 2 == 0 ? '0' : '1')) cnt0++;
            }
            int cnt1 = 0; // target 1010...
            for (int i = 0; i < n; ++i) {
                if (s[i] != (i % 2 == 0 ? '1' : '0')) cnt1++;
            }
            return min(cnt0, cnt1) <= numOps;
        } else {
            int totalOps = 0;
            int currentLen = 0;
            char currentChar = ' ';
            for (int i = 0; i < n; ++i) {
                if (s[i] == currentChar) {
                    currentLen++;
                } else {
                    totalOps += currentLen / (k + 1);
                    currentChar = s[i];
                    currentLen = 1;
                }
            }
            totalOps += currentLen / (k + 1);
            return totalOps <= numOps;
        }
    }
};
# @lc code=end