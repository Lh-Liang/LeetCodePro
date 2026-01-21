#include <bits/stdc++.h>
using namespace std;

#
# @lc app=leetcode id=3782 lang=cpp
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#
# @lc code=start
class Solution {
public:
    long long lastInteger(long long n) {
        long long head = 1;
        long long step = 1;
        long long cnt = n;
        bool op1 = true; // start with operation 1

        while (cnt > 1) {
            if (op1) {
                // Operation 1: from left, keep 1st,3rd,5th,...
                step = (long long)((__int128)step * 2);
                cnt = (cnt + 1) / 2;
            } else {
                // Operation 2: from right, keep indices with same parity as cnt
                if (cnt % 2 == 0) head += step; // keep even indices
                step = (long long)((__int128)step * 2);
                cnt = (cnt + 1) / 2;
            }
            op1 = !op1;
        }
        return head;
    }
};
# @lc code=end
