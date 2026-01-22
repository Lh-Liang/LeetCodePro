//
// @lc app=leetcode id=3782 lang=cpp
//
// [3782] Last Remaining Integer After Alternating Deletion Operations
//
// @lc code=start
class Solution {
public:
    long long lastInteger(long long n) {
        long long head = 1;
        long long step = 1;
        long long count = n;
        bool fromLeft = true;
        
        while (count > 1) {
            // For Op2 (from right) with even count, head moves
            if (!fromLeft && count % 2 == 0) {
                head += step;
            }
            // For Op1 and Op2 with odd count: head stays
            
            step *= 2;
            count = (count + 1) / 2;
            fromLeft = !fromLeft;
        }
        
        return head;
    }
};
// @lc code=end