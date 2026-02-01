#
# @lc app=leetcode id=3398 lang=cpp
#
# [3398] Smallest Substring With Identical Characters I
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
        int result = n;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canAchieve(s, mid, numOps)) {
                result = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return result;
    }

private:
    bool canAchieve(const string& s, int k, int numOps) {
        int n = s.length();
        if (k == 1) {
            int opsTo01 = 0;
            for (int i = 0; i < n; ++i) {
                char expected = (i % 2 == 0) ? '0' : '1';
                if (s[i] != expected) {
                    opsTo01++;
                }
            }
            int opsTo10 = n - opsTo01;
            return min(opsTo01, opsTo10) <= numOps;
        } else {
            int totalOps = 0;
            int currentRun = 1;
            for (int i = 1; i < n; ++i) {
                if (s[i] == s[i - 1]) {
                    currentRun++;
                } else {
                    totalOps += currentRun / (k + 1);
                    currentRun = 1;
                }
            }
            totalOps += currentRun / (k + 1);
            return totalOps <= numOps;
        }
    }
};
# @lc code=end