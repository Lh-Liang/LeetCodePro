#
# @lc app=leetcode id=3449 lang=cpp
#
# [3449] Maximize the Minimum Game Score
#
# @lc code=start
class Solution {
public:
    long long maxScore(vector<int>& points, int m) {
        int n = points.size();
        
        auto canAchieve = [&](long long minScore) -> bool {
            if (minScore == 0) return true;
            
            long long moves = 0;
            long long carry = 0;  // visits position i has from oscillation with i-1
            
            for (int i = 0; i < n; i++) {
                long long required = (minScore + points[i] - 1) / points[i];  // ceil division
                
                if (i == 0) {
                    moves += 1;  // move from -1 to 0
                    long long need_more = required - 1;
                    if (need_more > 0) {
                        moves += 2 * need_more;  // oscillate with position 1
                        carry = need_more;       // position 1 gets these visits
                    }
                } else {
                    if (carry < required) {
                        moves += 1;  // move from i-1 to i
                        long long visits = carry + 1;
                        long long need_more = required - visits;
                        if (need_more > 0) {
                            moves += 2 * need_more;
                            carry = (i < n - 1) ? need_more : 0;
                        } else {
                            carry = 0;
                        }
                    } else {
                        // carry >= required, position i is satisfied
                        if (i < n - 1) {
                            moves += 1;  // still need to pass through to reach later positions
                        }
                        carry = 0;
                    }
                }
                
                if (moves > (long long)m) return false;
            }
            
            return true;
        };
        
        long long lo = 0, hi = 2e15;
        while (lo < hi) {
            long long mid = lo + (hi - lo + 1) / 2;
            if (canAchieve(mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
};
# @lc code=end