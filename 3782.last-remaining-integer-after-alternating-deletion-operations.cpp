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
     * We track the sequence using an arithmetic progression: start, step, and count.
     * 
     * Operation 1 (Left to Right): Delete every 2nd number starting from the left.
     * This means the 1st element is kept, 2nd is deleted, 3rd is kept, etc.
     * The 'start' element always remains the same.
     * 
     * Operation 2 (Right to Left): Delete every 2nd number starting from the right.
     * This means the 1st element from the right is kept, 2nd from the right is deleted, etc.
     * If the total count is even, the original 'start' (which is the last element from the right's perspective)
     * is at an even position from the right and will be deleted. New start = start + step.
     * If the total count is odd, the original 'start' is at an odd position from the right and is kept.
     */
    long long lastInteger(long long n) {
        long long start = 1;
        long long step = 1;
        long long count = n;
        bool left_to_right = true;

        while (count > 1) {
            if (left_to_right) {
                // Operation 1: Left to Right
                // Elements at indices 2, 4, 6... (1-indexed) are deleted.
                // The first element (start) is at index 1, so it is always kept.
            } else {
                // Operation 2: Right to Left
                // Elements at indices 2, 4, 6... from the right are deleted.
                // If count is even, the 'start' element is at index 'count' from the right (even), so it's deleted.
                // If count is odd, the 'start' element is at index 'count' from the right (odd), so it's kept.
                if (count % 2 == 0) {
                    start += step;
                }
            }

            // In both operations, the number of elements is reduced by half.
            count = (count + 1) / 2;
            // The distance between remaining elements doubles.
            step *= 2;
            // Flip the direction for the next turn.
            left_to_right = !left_to_right;
        }

        return start;
    }
};
# @lc code=end