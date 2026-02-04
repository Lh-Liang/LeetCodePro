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
        long long left = 0, right = 1e12;
        while (left < right) {
            long long mid = left + (right - left + 1) / 2;
            if (canAchieve(points, m, mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
    
private:
    bool canAchieve(const vector<int>& points, int m, long long target) {
        vector<long long> gameScore(points.size(), 0);
        int moves = 0;
        for (int i = 0; i < points.size() && moves <= m; ++i) {
            if (gameScore[i] < target) {
                long long needed = target - gameScore[i];
                if (needed > points[i]) return false; // Can't satisfy this with available points.
                gameScore[i] += needed; // Use necessary moves to achieve target. 
                moves += needed / points[i] + ((needed % points[i]) ? 1 : 0); // Calculate moves needed. 
            } /
       } /
       return moves <= m; /
   } /
}; /
# @lc code=end