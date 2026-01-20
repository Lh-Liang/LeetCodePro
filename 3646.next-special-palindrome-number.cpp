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
public:
    long long specialPalindrome(long long n) {
        vector<long long> specials;
        // Iterate through all possible subsets of digits 1-9
        for (int i = 1; i < (1 << 9); ++i) {
            vector<int> S;
            int L = 0;
            int odd_count = 0;
            int odd_digit = -1;
            for (int j = 0; j < 9; ++j) {
                if ((i >> j) & 1) {
                    int digit = j + 1;
                    S.push_back(digit);
                    L += digit;
                    if (digit % 2 != 0) {
                        odd_count++;
                        odd_digit = digit;
                    }
                }
            }

            // Since n <= 10^15, we only need to generate up to a reasonable length L.
            // A 19-digit number is enough to cover all cases for n <= 10^15.
            if (L > 18) continue;

            if (L % 2 == 0) {
                // Even length: all digits must be even
                if (odd_count == 0) {
                    string half = "";
                    for (int d : S) half += string(d / 2, d + '0');
                    sort(half.begin(), half.end());
                    do {
                        string full = half;
                        string rev = half;
                        reverse(rev.begin(), rev.end());
                        full += rev;
                        specials.push_back(stoll(full));
                    } while (next_permutation(half.begin(), half.end()));
                }
            } else {
                // Odd length: exactly one digit must be odd
                if (odd_count == 1) {
                    string half = "";
                    for (int d : S) {
                        if (d == odd_digit) half += string((d - 1) / 2, d + '0');
                        else half += string(d / 2, d + '0');
                    }
                    sort(half.begin(), half.end());
                    do {
                        string full = half;
                        full += (char)(odd_digit + '0');
                        string rev = half;
                        reverse(rev.begin(), rev.end());
                        full += rev;
                        specials.push_back(stoll(full));
                    } while (next_permutation(half.begin(), half.end()));
                }
            }
        }

        sort(specials.begin(), specials.end());
        auto it = upper_bound(specials.begin(), specials.end(), n);
        return *it;
    }
};
# @lc code=end