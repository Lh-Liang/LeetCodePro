#
# @lc app=leetcode id=3721 lang=cpp
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;
class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> even_count, odd_count;
        int left = 0, right = 0, res = 0;
        int distinct_even = 0, distinct_odd = 0;
        while (right < n) {
            int num = nums[right];
            if (num % 2 == 0) {
                if (++even_count[num] == 1) distinct_even++;
            } else {
                if (++odd_count[num] == 1) distinct_odd++;
            }
            while (left <= right && distinct_even > distinct_odd) {
                int lnum = nums[left++];
                if (lnum % 2 == 0) {
                    if (--even_count[lnum] == 0) distinct_even--;
                } else {
                    if (--odd_count[lnum] == 0) distinct_odd--;
                }
            }
            while (left <= right && distinct_odd > distinct_even) {
                int lnum = nums[left++];
                if (lnum % 2 == 0) {
                    if (--even_count[lnum] == 0) distinct_even--;
                } else {
                    if (--odd_count[lnum] == 0) distinct_odd--;
                }
            }
            if (distinct_even == distinct_odd) {
                res = max(res, right - left + 1);
            }
            right++;
        }
        return res;
    }
};
# @lc code=end