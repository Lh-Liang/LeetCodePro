#
# @lc app=leetcode id=3677 lang=cpp
#
# [3677] Count Binary Palindromic Numbers
#
# @lc code=start
class Solution {
public:
    int countBinaryPalindromes(long long n) {
        if (n == 0) return 1;
        
        // Find bit length of n
        int bitLen = 0;
        long long temp = n;
        while (temp > 0) {
            bitLen++;
            temp >>= 1;
        }
        
        int count = 1; // Count 0
        
        // Count palindromes with length < bitLen
        for (int len = 1; len < bitLen; len++) {
            if (len == 1) {
                count += 1; // Only "1"
            } else if (len % 2 == 1) {
                count += (1 << ((len - 1) / 2));
            } else {
                count += (1 << (len / 2 - 1));
            }
        }
        
        // Count palindromes with length = bitLen that are <= n
        int halfLen = (bitLen + 1) / 2;
        
        for (long long i = 0; i < (1LL << (halfLen - 1)); i++) {
            long long half = (1LL << (halfLen - 1)) | i;
            long long num = half;
            long long mirror = (bitLen % 2 == 1) ? (half >> 1) : half;
            
            int shiftCount = (bitLen % 2 == 1) ? (halfLen - 1) : halfLen;
            for (int j = 0; j < shiftCount; j++) {
                num = (num << 1) | (mirror & 1);
                mirror >>= 1;
            }
            
            if (num <= n) {
                count++;
            } else {
                break;
            }
        }
        
        return count;
    }
};
# @lc code=end