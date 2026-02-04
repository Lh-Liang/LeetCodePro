#
# @lc app=leetcode id=3435 lang=cpp
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
class Solution {
public:
    vector<vector<int>> supersequences(vector<string>& words) {
        unordered_set<string> unique_scs;
        // Generate all potential SCSs for word pairs and store them in unique_scs set to filter permutations
        for (int i = 0; i < words.size(); ++i) {
            for (int j = i + 1; j < words.size(); ++j) {
                // Generate SCS for each pair using a helper function that maintains order
                string scs = generateSCS(words[i], words[j]);
                if (!scs.empty()) {
                    unique_scs.insert(scs);
                }
            }
        }
        
        vector<vector<int>> result;
        for (const string& scs : unique_scs) {
            vector<int> freq(26, 0);
            for (char c : scs) {
                freq[c - 'a']++;
            }
            result.push_back(freq);
        }
        return result;
    }
    
    string generateSCS(const string& a, const string& b) {
        // Merging two strings into a shortest common supersequence while keeping order intact
        int m = a.size(), n = b.size();
        int i = 0, j = 0;
        string scs;
        while (i < m || j < n) {
            if (i < m && j < n && a[i] == b[j]) {
                scs += a[i];
                ++i; ++j;
            } else if (i < m && (j >= n || a[i] != b[j])) {
                scs += a[i++];
            } else if (j < n && (i >= m || a[i] != b[j])) {
                scs += b[j++];
            }
        }
        return scs;
    }
};
# @lc code=end