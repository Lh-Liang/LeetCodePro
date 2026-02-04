#
# @lc app=leetcode id=3734 lang=cpp
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#
# @lc code=start
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.size();
        vector<int> freq(26, 0);
        for(char c : s) freq[c-'a']++;
        int odd = 0, odd_char = -1;
        for(int i=0; i<26; ++i) if(freq[i]%2) { odd++; odd_char = i; }
        if(odd > 1) return "";
        vector<char> half;
        for(int i=0; i<26; ++i) for(int j=0; j<freq[i]/2; ++j) half.push_back('a'+i);
        string mid = (odd == 1 ? string(1, 'a'+odd_char) : "");
        string pal;
        do {
            string first(half.begin(), half.end());
            string second = first;
            reverse(second.begin(), second.end());
            pal = first + mid + second;
            if(pal > target) return pal;
        } while(next_permutation(half.begin(), half.end()));
        return "";
    }
};
# @lc code=end