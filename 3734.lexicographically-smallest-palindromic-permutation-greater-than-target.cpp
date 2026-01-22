//
// @lc app=leetcode id=3734 lang=cpp
//
// [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
//

// @lc code=start
class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.length();
        
        vector<int> freq(26, 0);
        for (char c : s) freq[c - 'a']++;
        
        int oddCount = 0;
        char middleChar = '\0';
        for (int i = 0; i < 26; i++) {
            if (freq[i] % 2 == 1) {
                oddCount++;
                middleChar = 'a' + i;
            }
        }
        
        // Check if palindrome is possible
        if ((n % 2 == 0 && oddCount > 0) || (n % 2 == 1 && oddCount != 1)) {
            return "";
        }
        
        int halfLen = n / 2;
        vector<int> halfFreq(26, 0);
        for (int i = 0; i < 26; i++) {
            halfFreq[i] = freq[i] / 2;
        }
        
        string half(halfLen, ' ');
        
        function<string(int, bool)> solve = [&](int pos, bool mustBeGreater) -> string {
            if (pos == halfLen) {
                string palindrome = half;
                if (n % 2 == 1) palindrome += middleChar;
                for (int i = halfLen - 1; i >= 0; i--) {
                    palindrome += half[i];
                }
                if (mustBeGreater || palindrome > target) {
                    return palindrome;
                }
                return "";
            }
            
            if (mustBeGreater) {
                // Fill remaining with smallest characters
                for (int i = pos; i < halfLen; i++) {
                    for (int c = 0; c < 26; c++) {
                        if (halfFreq[c] > 0) {
                            half[i] = 'a' + c;
                            halfFreq[c]--;
                            break;
                        }
                    }
                }
                string palindrome = half;
                if (n % 2 == 1) palindrome += middleChar;
                for (int i = halfLen - 1; i >= 0; i--) {
                    palindrome += half[i];
                }
                return palindrome;
            }
            
            // Try each character >= target[pos]
            for (int c = 0; c < 26; c++) {
                if (halfFreq[c] > 0) {
                    char ch = 'a' + c;
                    if (ch < target[pos]) continue;
                    
                    halfFreq[c]--;
                    half[pos] = ch;
                    
                    bool newMustBeGreater = (ch > target[pos]);
                    string result = solve(pos + 1, newMustBeGreater);
                    
                    if (!result.empty()) {
                        return result;
                    }
                    
                    halfFreq[c]++;
                }
            }
            
            return "";
        };
        
        return solve(0, false);
    }
};
// @lc code=end