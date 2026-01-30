#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
    struct Point {
        int x, y;
        long long p;
    };

    inline int get_dist(const Point& a, const Point& b) {
        return abs(a.x - b.x) + abs(a.y - b.y);
    }

public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        int n = points.size();
        vector<Point> pts(n);
        for (int i = 0; i < n; ++i) {
            int x = points[i][0], y = points[i][1];
            long long p;
            if (y == 0) p = x;
            else if (x == side) p = (long long)side + y;
            else if (y == side) p = (long long)2 * side + (side - x);
            else p = (long long)3 * side + (side - y);
            pts[i] = {x, y, p};
        }

        sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
            return a.p < b.p;
        });

        vector<Point> double_pts = pts;
        for (int i = 0; i < n; ++i) {
            double_pts.push_back(pts[i]);
        }

        auto check = [&](int mid) {
            int total = 2 * n;
            vector<int> next_idx(total, -1);
            int right = 0;
            for (int left = 0; left < total; ++left) {
                if (right <= left) right = left + 1;
                while (right < total && get_dist(double_pts[left], double_pts[right]) < mid) {
                    right++;
                }
                if (right < total) next_idx[left] = right;
            }

            // Binary lifting or simple greedy. Since k is small (<= 25), simple greedy is O(n/k * k) = O(n).
            // We only need to check starting points in the first "segment" to guarantee finding a solution.
            int limit = n / k + 1;
            for (int start = 0; start <= limit && start < n; ++start) {
                int curr = start;
                int count = 1;
                while (count < k && curr != -1 && curr < start + n) {
                    curr = next_idx[curr];
                    count++;
                }
                if (count == k && curr != -1 && curr < start + n) {
                    if (get_dist(double_pts[curr], double_pts[start]) >= mid) {
                        return true;
                    }
                }
            }
            return false;
        };

        int low = 1, high = side, ans = 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check(mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
};