//
// @lc app=leetcode id=3598 lang=cpp
//
// [3598] Longest Common Prefix Between Adjacent Strings After Removals
//

// @lc code=start
class Solution {
public:
    int computeLCP(const string& a, const string& b) {
        int len = 0;
        int minLen = min(a.size(), b.size());
        while (len < minLen && a[len] == b[len]) {
            len++;
        }
        return len;
    }
    
    vector<int> longestCommonPrefix(vector<string>& words) {
        int n = words.size();
        if (n == 1) return {0};
        if (n == 2) return {0, 0};
        
        // lcp[i] = LCP(words[i], words[i+1])
        vector<int> lcp(n - 1);
        for (int i = 0; i < n - 1; i++) {
            lcp[i] = computeLCP(words[i], words[i + 1]);
        }
        
        // skip_lcp[i] = LCP(words[i], words[i+2])
        vector<int> skip_lcp(n - 2);
        for (int i = 0; i < n - 2; i++) {
            skip_lcp[i] = computeLCP(words[i], words[i + 2]);
        }
        
        // prefix[i] = max(lcp[0..i])
        vector<int> prefix(n - 1);
        prefix[0] = lcp[0];
        for (int i = 1; i < n - 1; i++) {
            prefix[i] = max(prefix[i - 1], lcp[i]);
        }
        
        // suffix[i] = max(lcp[i..n-2])
        vector<int> suffix(n - 1);
        suffix[n - 2] = lcp[n - 2];
        for (int i = n - 3; i >= 0; i--) {
            suffix[i] = max(suffix[i + 1], lcp[i]);
        }
        
        vector<int> answer(n);
        for (int i = 0; i < n; i++) {
            int result = 0;
            
            // From lcp[0..i-2]
            if (i >= 2) {
                result = max(result, prefix[i - 2]);
            }
            
            // From lcp[i+1..n-2]
            if (i + 1 <= n - 2) {
                result = max(result, suffix[i + 1]);
            }
            
            // New pair (i-1, i+1) which is skip_lcp[i-1]
            if (i >= 1 && i <= n - 2) {
                result = max(result, skip_lcp[i - 1]);
            }
            
            answer[i] = result;
        }
        
        return answer;
    }
};
// @lc code=end