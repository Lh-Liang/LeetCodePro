//
// @lc app=leetcode id=3448 lang=cpp
//
// [3448] Count Substrings Divisible By Last Digit
//

// @lc code=start
class Solution {
public:
    long long countSubstrings(string s) {
        int n = s.length();
        long long result = 0;
        
        // For digit 3, 6: prefix sum of digits mod 3
        vector<int> cnt3(3, 0);
        int prefixSum3 = 0;
        cnt3[0] = 1;
        
        // For digit 9: prefix sum of digits mod 9
        vector<int> cnt9(9, 0);
        int prefixSum9 = 0;
        cnt9[0] = 1;
        
        // For digit 7: transformed prefixes mod 7
        vector<int> cnt7(7, 0);
        int prefix7 = 0;
        int inv10_power = 1;
        cnt7[0] = 1;
        
        const int inv10 = 5;  // 10 * 5 ≡ 1 (mod 7)
        
        for (int j = 0; j < n; j++) {
            int d = s[j] - '0';
            
            // Update prefix values
            prefixSum3 = (prefixSum3 + d) % 3;
            prefixSum9 = (prefixSum9 + d) % 9;
            prefix7 = (prefix7 * 10 + d) % 7;
            inv10_power = (inv10_power * inv10) % 7;
            int transformed7 = (prefix7 * inv10_power) % 7;
            
            if (d != 0) {
                switch (d) {
                    case 1:
                    case 2:
                    case 5:
                        result += j + 1;
                        break;
                    case 3:
                    case 6:
                        result += cnt3[prefixSum3];
                        break;
                    case 9:
                        result += cnt9[prefixSum9];
                        break;
                    case 4:
                        result += 1;
                        if (j >= 1) {
                            int last2 = (s[j-1] - '0') * 10 + d;
                            if (last2 % 4 == 0) {
                                result += j;
                            }
                        }
                        break;
                    case 7:
                        result += cnt7[transformed7];
                        break;
                    case 8:
                        result += 1;
                        if (j >= 1) {
                            int last2 = (s[j-1] - '0') * 10 + d;
                            if (last2 % 8 == 0) {
                                result += 1;
                            }
                        }
                        if (j >= 2) {
                            int last3 = (s[j-2] - '0') * 100 + (s[j-1] - '0') * 10 + d;
                            if (last3 % 8 == 0) {
                                result += j - 1;
                            }
                        }
                        break;
                }
            }
            
            // Update counts
            cnt3[prefixSum3]++;
            cnt9[prefixSum9]++;
            cnt7[transformed7]++;
        }
        
        return result;
    }
};
// @lc code=end