#
# @lc app=leetcode id=3609 lang=cpp
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
#include <queue>
#include <map>

using namespace std;

class Solution {
public:
    int minMoves(int sx, int sy, int tx, int ty) {
        // Handle the stationary state (0,0)
        if (sx == 0 && sy == 0) return (tx == 0 && ty == 0) ? 0 : -1;
        // Already at target
        if (sx == tx && sy == ty) return 0;

        queue<pair<long long, long long>> q;
        map<pair<long long, long long>, int> dist;

        q.push({(long long)tx, (long long)ty});
        dist[{(long long)tx, (long long)ty}] = 0;

        while (!q.empty()) {
            pair<long long, long long> curr = q.front();
            q.pop();
            long long x = curr.first;
            long long y = curr.second;
            int d = dist[curr];

            if (x == sx && y == sy) return d;

            if (x > y) {
                // Predecessor must have come from the x-direction
                if (x % 2 == 0 && x / 2 >= y) {
                    long long nx = x / 2, ny = y;
                    if (nx >= sx && ny >= sy && dist.find({nx, ny}) == dist.end()) {
                        dist[{nx, ny}] = d + 1;
                        q.push({nx, ny});
                    }
                } else if (x - y < y) {
                    long long nx = x - y, ny = y;
                    if (nx >= sx && ny >= sy && dist.find({nx, ny}) == dist.end()) {
                        dist[{nx, ny}] = d + 1;
                        q.push({nx, ny});
                    }
                }
            } else if (y > x) {
                // Predecessor must have come from the y-direction
                if (y % 2 == 0 && y / 2 >= x) {
                    long long nx = x, ny = y / 2;
                    if (nx >= sx && ny >= sy && dist.find({nx, ny}) == dist.end()) {
                        dist[{nx, ny}] = d + 1;
                        q.push({nx, ny});
                    }
                } else if (y - x < x) {
                    long long nx = x, ny = y - x;
                    if (nx >= sx && ny >= sy && dist.find({nx, ny}) == dist.end()) {
                        dist[{nx, ny}] = d + 1;
                        q.push({nx, ny});
                    }
                }
            } else if (x == y && x > 0) {
                // Branching point: can come from either axis
                long long nx1 = 0, ny1 = y;
                if (nx1 >= sx && ny1 >= sy && dist.find({nx1, ny1}) == dist.end()) {
                    dist[{nx1, ny1}] = d + 1;
                    q.push({nx1, ny1});
                }
                long long nx2 = x, ny2 = 0;
                if (nx2 >= sx && ny2 >= sy && dist.find({nx2, ny2}) == dist.end()) {
                    dist[{nx2, ny2}] = d + 1;
                    q.push({nx2, ny2});
                }
            }
        }

        return -1;
    }
};
# @lc code=end