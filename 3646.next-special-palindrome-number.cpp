#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#
# @lc app=leetcode id=3646 lang=cpp
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
class Solution {
    long long result = -1;
    long long N_val;
    string N_str;

    void findSmallest(int idx, int L, vector<int>& counts, string& current, bool isGreater) {
        int half = (L + 1) / 2;
        if (idx == half) {
            string s = current;
            for (int i = L / 2 - 1; i >= 0; --i) s += current[i];
            
            if (s.length() > 19) return;
            if (s.length() == 19 && s > "9223372036854775807") return;
            
            long long val = stoll(s);
            if (val > N_val) {
                if (result == -1 || val < result) result = val;
            }
            return;
        }

        int startDigit = (idx == 0) ? 1 : 0;
        int limit = isGreater ? 0 : (idx < N_str.length() ? N_str[idx] - '0' : 0);

        for (int d = max(startDigit, limit); d <= 9; ++d) {
            if (counts[d] > 0) {
                // If length is odd, the middle element must be the odd-frequency digit
                if (L % 2 != 0 && idx == half - 1) {
                    if (d % 2 == 0) continue;
                }
                
                counts[d]--;
                current.push_back(d + '0');
                findSmallest(idx + 1, L, counts, current, isGreater || (d > limit));
                current.pop_back();
                counts[d]++;
                
                // Since we search digits in increasing order, the first valid result for a prefix is the smallest
                if (result != -1) return; 
            }
        }
    }

public:
    long long specialPalindrome(long long n) {
        N_val = n;
        N_str = to_string(n);
        int n_len = N_str.length();
        
        vector<int> even_digits = {2, 4, 6, 8};
        vector<int> odd_digits = {1, 3, 5, 7, 9};
        
        vector<pair<int, vector<int>>> valid_multisets;
        
        // Case 1: Even length (only even digits allowed)
        for (int i = 1; i < (1 << 4); ++i) {
            int sum = 0;
            vector<int> counts(10, 0);
            for (int j = 0; j < 4; ++j) {
                if ((i >> j) & 1) {
                    sum += even_digits[j];
                    counts[even_digits[j]] = even_digits[j] / 2;
                }
            }
            if (sum > 0 && sum <= 19) valid_multisets.push_back({sum, counts});
        }
        
        // Case 2: Odd length (exactly one odd digit allowed)
        for (int i = 0; i < (1 << 4); ++i) {
            int base_sum = 0;
            vector<int> base_counts(10, 0);
            for (int j = 0; j < 4; ++j) {
                if ((i >> j) & 1) {
                    base_sum += even_digits[j];
                    base_counts[even_digits[j]] = even_digits[j] / 2;
                }
            }
            for (int o : odd_digits) {
                int sum = base_sum + o;
                if (sum <= 19) {
                    vector<int> counts = base_counts;
                    counts[o] = (o + 1) / 2; // (o-1)/2 for first half + 1 for middle
                    valid_multisets.push_back({sum, counts});
                }
            }
        }

        sort(valid_multisets.begin(), valid_multisets.end());

        for (auto& p : valid_multisets) {
            int L = p.first;
            if (L < n_len) continue;
            // If we found a result of length L, we don't need to check length L+1
            if (result != -1 && L > to_string(result).length()) break;

            string current = "";
            findSmallest(0, L, p.second, current, L > n_len);
        }
        
        return result;
    }
};
# @lc code=end