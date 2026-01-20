#
# @lc app=leetcode id=3458 lang=cpp
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        if (k == 0) return true;
        int n = s.length();
        vector<int> first(26, -1);
        vector<int> last(26, -1);

        for (int i = 0; i < n; ++i) {
            int c = s[i] - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }

        vector<pair<int, int>> intervals;
        for (int i = 0; i < 26; ++i) {
            if (first[i] == -1) continue;

            int L = first[i];
            int R = last[i];
            bool valid = true;
            
            // Expand the range to include all occurrences of all characters within [L, R]
            for (int j = L; j <= R; ++j) {
                int currChar = s[j] - 'a';
                if (first[currChar] < L) {
                    valid = false;
                    break;
                }
                R = max(R, last[currChar]);
            }

            if (valid && !(L == 0 && R == n - 1)) {
                intervals.push_back({L, R});
            }
        }

        // Sort intervals by their end points for greedy selection
        sort(intervals.begin(), intervals.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second < b.second;
        });

        int count = 0;
        int lastEnd = -1;
        for (const auto& interval : intervals) {
            if (interval.first > lastEnd) {
                count++;
                lastEnd = interval.second;
            }
        }

        return count >= k;
    }
};
# @lc code=end