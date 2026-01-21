#
# @lc app=leetcode id=3782 lang=cpp
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#

# @lc code=start
#include <vector>
class Solution {
public:
    long long lastInteger(long long n) {
        std::vector<long long> sizes;
        sizes.push_back(n);
        while (sizes.back() > 1) {
            sizes.push_back((sizes.back() + 1LL) / 2);
        }
        long long pos = 1;
        for (int i = sizes.size() - 2; i >= 0; --i) {
            long long old_size = sizes[i];
            bool is_left_op = (i % 2 == 0);
            if (is_left_op) {
                pos = 2 * pos - 1;
            } else {
                if (old_size % 2 == 1) {
                    pos = 2 * pos - 1;
                } else {
                    pos = 2 * pos;
                }
            }
        }
        return pos;
    }
};
# @lc code=end