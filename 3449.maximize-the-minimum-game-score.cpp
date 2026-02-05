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
        long long left = 0, right = 1e15, answer = 0;
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            // Calculate how many moves are needed to make all gameScore[i] >= mid
            long long moves = 0;
            for (int i = 0; i < n; ++i) {
                // To get gameScore[i] >= mid, need at least ceil(mid / points[i]) visits
                long long need = (mid + points[i] - 1) / points[i];
                moves += need;
            }
            // One move transitions from -1 to 0, so moves - 1 transitions
            if (moves - 1 <= m) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return answer;
    }
};
# @lc code=end