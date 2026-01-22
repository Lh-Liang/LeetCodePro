//
// @lc app=leetcode id=3677 lang=cpp
//
// [3677] Count Binary Palindromic Numbers
//
// @lc code=start
class Solution {
public:
    int countBinaryPalindromes(long long n) {
        if (n == 0) return 1;
        
        // Get binary representation of n (MSB first)
        vector<int> bits;
        long long temp = n;
        while (temp > 0) {
            bits.push_back(temp & 1);
            temp >>= 1;
        }
        reverse(bits.begin(), bits.end());
        int L = (int)bits.size();
        
        // Count starts with 1 (for the number 0)
        long long count = 1;
        
        // Count palindromes of lengths 1 to L-1 (all are strictly less than n)
        for (int len = 1; len < L; len++) {
            count += (1LL << ((len - 1) / 2));
        }
        
        // Count palindromes of length L that are <= n
        int m = (L - 1) / 2;  // front half covers positions 0 to m
        
        // Case 1: first difference at position j where p[j] = 0 < b[j] = 1
        for (int j = 1; j <= m; j++) {
            if (bits[j] == 1) {
                count += (1LL << (m - j));
            }
        }
        
        // Case 2: front half equals b's front half, construct palindrome and check
        vector<int> p(L);
        for (int i = 0; i <= m; i++) {
            p[i] = bits[i];
        }
        for (int i = m + 1; i < L; i++) {
            p[i] = p[L - 1 - i];
        }
        
        bool lessOrEqual = true;
        for (int i = 0; i < L; i++) {
            if (p[i] < bits[i]) break;
            if (p[i] > bits[i]) {
                lessOrEqual = false;
                break;
            }
        }
        if (lessOrEqual) count++;
        
        return (int)count;
    }
};
// @lc code=end