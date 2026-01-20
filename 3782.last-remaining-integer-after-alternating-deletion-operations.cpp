#
# @lc app=leetcode id=3782 lang=cpp
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#

# @lc code=start
class Solution {
public:
    /**
     * The problem asks for the last remaining integer after alternating deletions.
     * The sequence always forms an Arithmetic Progression (AP).
     * We track the first element (start), the common difference (step), and the number of elements (count).
     */
    long long lastInteger(long long n) {
        long long start = 1;
        long long step = 1;
        long long count = n;
        bool leftToRight = true;

        while (count > 1) {
            if (leftToRight) {
                // Operation 1: Starting from the left, delete every second number.
                // Positions: 1(Keep), 2(Delete), 3(Keep), 4(Delete)...
                // The first element 'start' is always kept.
                // start = start;
            } else {
                // Operation 2: Starting from the right, delete every second number.
                // Positions from right: 1(Keep), 2(Delete), 3(Keep), 4(Delete)...
                // If count is even (e.g., [x1, x2, x3, x4]):
                //   x4 (Keep), x3 (Delete), x2 (Keep), x1 (Delete).
                //   The original start (x1) is deleted, new start is x2.
                // If count is odd (e.g., [x1, x2, x3]):
                //   x3 (Keep), x2 (Delete), x1 (Keep).
                //   The original start (x1) is kept.
                if (count % 2 == 0) {
                    start += step;
                }
            }

            // In every step, the gap between numbers doubles and the count is halved (rounded up).
            step *= 2;
            count = (count + 1) / 2;
            leftToRight = !leftToRight;
        }

        return start;
    }
};
# @lc code=end