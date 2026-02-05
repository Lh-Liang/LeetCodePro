#
# @lc app=leetcode id=3435 lang=cpp
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
class Solution {
public:
    vector<vector<int>> supersequences(vector<string>& words) {
        // Step 1: Build all shortest common supersequences (SCS)
        // For small input size and all words length 2, enumerate all orders
        int n = words.size();
        vector<int> idx(n, 0);
        iota(idx.begin(), idx.end(), 0);
        set<vector<int>> freq_set;
        int min_len = INT_MAX;
        do {
            string scs = words[idx[0]];
            for (int i = 1; i < n; ++i) {
                // Merge scs and words[idx[i]]
                string& w = words[idx[i]];
                int p1 = 0, p2 = 0;
                string merged;
                int m = scs.size(), l = w.size();
                int common = 0;
                // Find maximal suffix of scs matching prefix of w
                for (int k = min(m, l); k >= 0; --k) {
                    if (scs.substr(m - k, k) == w.substr(0, k)) {
                        common = k; break;
                    }
                }
                scs += w.substr(common);
            }
            if ((int)scs.size() < min_len) {
                freq_set.clear();
                min_len = scs.size();
            }
            if ((int)scs.size() == min_len) {
                vector<int> freq(26, 0);
                for (char c : scs) freq[c - 'a']++;
                freq_set.insert(freq);
            }
        } while (next_permutation(idx.begin(), idx.end()));
        vector<vector<int>> result(freq_set.begin(), freq_set.end());
        return result;
    }
};
# @lc code=end