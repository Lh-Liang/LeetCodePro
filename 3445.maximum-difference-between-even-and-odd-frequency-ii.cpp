#
# @lc app=leetcode id=3445 lang=cpp
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution {
public:
    int maxDifference(string s, int k) {
        // Step 1: Extract constraints and requirements (already done above)
        // Step 2: Use a sliding window approach for all substrings of length >= k
        // Step 3: For each window, maintain a frequency array for digits '0' to '4'
        // Step 4: For each possible (odd-freq a, even-nonzero-freq b) pair, compute difference
        // Step 5: Track the maximum difference overall
        int n = s.size();
        int res = INT_MIN;
        for (int len = k; len <= n; ++len) {
            vector<int> freq(5, 0);
            // Initialize frequency for first window of length 'len'
            for (int i = 0; i < len; ++i) freq[s[i] - '0']++;
            // Check window
            res = max(res, getMaxDiff(freq));
            // Slide window
            for (int i = len; i < n; ++i) {
                freq[s[i - len] - '0']--;
                freq[s[i] - '0']++;
                res = max(res, getMaxDiff(freq));
            }
        }
        return res;
    }
    
    int getMaxDiff(const vector<int>& freq) {
        int ans = INT_MIN;
        for (int a = 0; a < 5; ++a) {
            if (freq[a] % 2 == 1) { // odd freq
                for (int b = 0; b < 5; ++b) {
                    if (a == b) continue;
                    if (freq[b] > 0 && freq[b] % 2 == 0) { // even and nonzero
                        ans = max(ans, freq[a] - freq[b]);
                    }
                }
            }
        }
        return ans;
    }
};
# @lc code=end