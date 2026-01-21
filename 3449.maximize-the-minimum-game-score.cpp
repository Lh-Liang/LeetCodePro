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
        
        auto canAchieve = [&](long long T) -> bool {
            if (T == 0) return true;
            
            long long moves = 1;  // Move to position 0
            long long carry = 0;
            
            for (int i = 0; i < n - 1; i++) {
                long long need = (T + points[i] - 1) / points[i];
                long long visits = carry + 1;
                
                if (visits < need) {
                    long long extra = need - visits;
                    moves += 2 * extra;
                    carry = extra;
                } else {
                    carry = 0;
                }
                
                if (moves > m) return false;
                
                // Check if the last position is already satisfied by carry
                if (i + 1 == n - 1) {
                    long long need_last = (T + points[n-1] - 1) / points[n-1];
                    if (carry >= need_last) {
                        return moves <= m;
                    }
                }
                
                moves += 1;  // Move to position i+1
                if (moves > m) return false;
            }
            
            // Process the last position
            long long need_last = (T + points[n-1] - 1) / points[n-1];
            long long visits_last = carry + 1;
            
            if (visits_last < need_last) {
                long long extra = need_last - visits_last;
                moves += 2 * extra;
            }
            
            return moves <= m;
        };
        
        long long left = 0;
        long long right = (long long)m * (*max_element(points.begin(), points.end()));
        
        while (left < right) {
            long long mid = left + (right - left + 1) / 2;
            if (canAchieve(mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        
        return left;
    }
};
# @lc code=end