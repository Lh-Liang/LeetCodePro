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
        long long left = 1, right = 1e12; // Define search space based on constraints
        auto is_feasible = [&](long long min_score) {
            long long moves = 0;
            for (int i = 0; i < n; ++i) {
                if (points[i] < min_score) { // Calculate required moves to reach min_score at each index
                    moves += (min_score - points[i]);
                    if (moves > m) return false; // If moves exceed m, not feasible
                }
            }
            return true; // Feasible if we never exceeded m moves
        };
        while (left < right) { // Binary search over possible minimum scores
            long long mid = left + (right - left + 1) / 2; // Midpoint of current range
            if (is_feasible(mid)) { // If mid is feasible, try higher values by moving left upward
                left = mid; 
            } else { 
                right = mid - 1; 
            } 
        } 
        return left; // The maximum possible minimum score found by binary search 
    } 
}; 
# @lc code=end