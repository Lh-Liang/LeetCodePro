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
        bool left = true;
        
        while (n > 1) {
            if (!left) {
                // Moving Right -> Left
                // We keep the last element.
                // If n is even, the first element (leftmost) is deleted.
                // If n is odd, the first element (leftmost) is kept.
                if (n % 2 == 0) {
                    head += step;
                }
            } 
            // If moving Left -> Right
            // We keep the first element (leftmost).
            // So head never changes.
            
            step *= 2;
            n = n - n / 2;
            left = !left;
        }
        
        return head;
    }
};
# @lc code=end