#
# @lc app=leetcode id=3458 lang=cpp
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <utility>

using namespace std;

class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        if (k == 0) return true;
        int n = s.length();
        vector<int> first(26, -1);
        vector<int> last(26, -1);
        
        // Step 1: Precompute first and last occurrences
        for (int i = 0; i < n; ++i) {
            int c = s[i] - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }

        vector<pair<int, int>> candidates;
        
        // Step 2: Generate candidate special substrings
        for (int i = 0; i < 26; ++i) {
            if (first[i] == -1) continue;
            
            int L = first[i];
            int R = last[i];
            bool valid = true;
            
            // Expand range to satisfy special substring property
            for (int j = L; j <= R; ++j) {
                int c = s[j] - 'a';
                if (first[c] < L) {
                    valid = false; // Character starts before our fixed L
                    break;
                }
                R = max(R, last[c]);
            }
            
            // Must not be the entire string
            if (valid && (R - L + 1 < n)) {
                candidates.push_back({L, R});
            }
        }

        // Step 3: Greedy Interval Scheduling
        sort(candidates.begin(), candidates.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second < b.second;
        });

        int count = 0;
        int current_end = -1;
        for (const auto& interval : candidates) {
            if (interval.first > current_end) {
                count++;
                current_end = interval.second;
            }
        }

        return count >= k;
    }
};
# @lc code=end