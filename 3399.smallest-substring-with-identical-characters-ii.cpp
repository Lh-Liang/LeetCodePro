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

private:
    bool check(int k, const string& s, int numOps) {
        int n = s.length();
        if (k == 1) {
            int ops1 = 0; // target 010101...
            int ops2 = 0; // target 101010...
            for (int i = 0; i < n; ++i) {
                char expected1 = (i % 2 == 0) ? '0' : '1';
                if (s[i] != expected1) {
                    ops1++;
                } else {
                    ops2++;
                }
            }
            return min(ops1, ops2) <= numOps;
        }

        int totalOps = 0;
        int count = 1;
        for (int i = 1; i < n; ++i) {
            if (s[i] == s[i - 1]) {
                count++;
            } else {
                totalOps += count / (k + 1);
                count = 1;
            }
        }
        totalOps += count / (k + 1);
        return totalOps <= numOps;
    }
};
# @lc code=end