#
# @lc app=leetcode id=3341 lang=cpp
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size();
        int m = moveTime[0].size();
        vector<vector<int>> minTime(n, vector<int>(m, INT_MAX));
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;
        pq.emplace(0, 0, 0); // (current_time, row_index, col_index)
        minTime[0][0] = 0;
        constexpr static int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!pq.empty()) {
            auto [current_time, x, y] = pq.top(); pq.pop();
            if (x == n - 1 && y == m - 1) return current_time; // reached destination
            for (auto& dir : directions) {
                int nx = x + dir[0], ny = y + dir[1];
                if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
                    int wait_time = max(0, moveTime[nx][ny] - (current_time + 1)); // wait if needed until room is open
                    int new_time = current_time + 1 + wait_time; // add moving time + waiting time if any
                    if (new_time < minTime[nx][ny]) { // update only if found a better way/time to reach there
                        minTime[nx][ny] = new_time;
                        pq.emplace(new_time, nx, ny); // push new state into priority queue for exploration
                    } /1}/1}/1}/1}/1 /1 } /1 }; # @lc code=end