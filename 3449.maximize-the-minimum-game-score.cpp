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
        long long left = 0, right = accumulate(points.begin(), points.end(), 0LL);
        
        auto canAchieve = [&](long long minScore) {
            vector<long long> tempScore(n, 0);
            long long totalMoves = 0;
            for (int i = 0; i < n && totalMoves <= m; ++i) {
                if (tempScore[i] < minScore) {
                    long long needed = minScore - tempScore[i];
                    totalMoves += needed / points[i] + ((needed % points[i]) ? 1 : 0);
                }
            }
            return totalMoves <= m;
        };
        
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