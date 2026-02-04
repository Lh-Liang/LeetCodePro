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
        long long left = 0;
        // Calculating a realistic upper bound based on maximum possible single index score contribution
        long long right = *min_element(points.begin(), points.end()) * (m / n + 1);
        
        auto canAchieve = [&](long long target) {
            vector<long long> gameScore(n, 0);
            int movesUsed = 0;
            for (int i = 0; i < n; ++i) {
                if (gameScore[i] < target) {
                    // Calculate how much we need and how many moves it would take
                    long long needed = target - gameScore[i];
                    long long maxAdditions = needed / points[i] + ((needed % points[i]) != 0);
                    if ((movesUsed += maxAdditions) > m) return false;
                    gameScore[i] += maxAdditions * points[i];
                }
            }
            return true; // If all indices can achieve at least "target"
        };
        
        while (left < right) {
            long long mid = left + (right - left + 1) / 2; // Upper mid for correct convergence
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