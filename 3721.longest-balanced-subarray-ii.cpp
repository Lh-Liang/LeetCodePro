#
# @lc app=leetcode id=3721 lang=cpp
#
# [3721] Longest Balanced Subarray II
#
# @lc code=start
#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> even_count, odd_count;
        int left = 0, res = 0;
        for (int right = 0; right < n; ++right) {
            int val = nums[right];
            if (val % 2 == 0) ++even_count[val];
            else ++odd_count[val];
            while (left <= right && even_count.size() > odd_count.size()) {
                int lval = nums[left];
                if (lval % 2 == 0) {
                    if (--even_count[lval] == 0) even_count.erase(lval);
                } else {
                    if (--odd_count[lval] == 0) odd_count.erase(lval);
                }
                ++left;
            }
            while (left <= right && odd_count.size() > even_count.size()) {
                int lval = nums[left];
                if (lval % 2 == 0) {
                    if (--even_count[lval] == 0) even_count.erase(lval);
                } else {
                    if (--odd_count[lval] == 0) odd_count.erase(lval);
                }
                ++left;
            }
            if (even_count.size() == odd_count.size())
                res = max(res, right - left + 1);
        }
        return res;
    }
};
# @lc code=end