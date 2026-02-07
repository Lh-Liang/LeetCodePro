//
// @lc app=leetcode id=3646 lang=cpp
//
// [3646] Next Special Palindrome Number
//
// @lc code=start
class Solution {
public:
    long long specialPalindrome(long long n) {
        long long num = n + 1;
        while (true) {
            num = generateNextPalindrome(num);
            if (isPalindrome(num) && isValidSpecial(num)) {
                return num;
            }
        }
    }
    
    bool isPalindrome(long long num) {
        std::string s = std::to_string(num);
        return std::equal(s.begin(), s.begin() + s.size()/2, s.rbegin());
    }
    
    bool isValidSpecial(long long num) {
        std::string s = std::to_string(num);
        int count[10] = {0};
        for (char c : s) {
            int digit = c - '0';
            if (digit == 0 || digit > s.size()) return false; // Check valid range
            ++count[digit];
        }
        for (int i = 0; i < 10; ++i) {
            if (count[i] != 0 && count[i] != i) return false; // Each k occurs exactly k times
        }
        return true;
    }
    
    long long generateNextPalindrome(long long num) {
        std::string s = std::to_string(num);
        int len = s.length();

        // Mirror first half to second half
        for (int i = 0; i < len / 2; ++i) {
s[len - i - 1] = s[i];}

        // If mirrored palindrome is not greater, increment middle part
        if (std::stoll(s) <= num) {int mid = (len - 1) / 2;while (mid >= 0 && s[mid] == '9') {s[mid] = '0';--mid;}if (mid >= 0) {s[mid] += 1;} else { // Handle overflow like '999' -> '1001's[0] = '1';s += '1';}// Remirror after incrementfor (int i = 0; i < len / 2; ++i) {s[len - i - 1] = s[i];}}return std::stoll(s);}};// @lc code=end