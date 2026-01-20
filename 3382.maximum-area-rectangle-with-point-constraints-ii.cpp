#
# @lc app=leetcode id=3382 lang=cpp
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class BIT {
    vector<int> tree;
    int n;
public:
    BIT(int n) : n(n), tree(n + 1, 0) {}
    void update(int i, int val) {
        for (; i <= n; i += i & -i) tree[i] += val;
    }
    int query(int i) {
        int res = 0;
        for (; i > 0; i -= i & -i) res += tree[i];
        return res;
    }
};

class Solution {
public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        int n = xCoord.size();
        struct Point {
            int x, y;
        };
        vector<Point> points(n);
        vector<int> ys;
        for (int i = 0; i < n; i++) {
            points[i] = {xCoord[i], yCoord[i]};
            ys.push_back(yCoord[i]);
        }
        
        sort(ys.begin(), ys.end());
        ys.erase(unique(ys.begin(), ys.end()), ys.end());
        auto get_y = [&](int y) {
            return lower_bound(ys.begin(), ys.end(), y) - ys.begin() + 1;
        };
        
        sort(points.begin(), points.end(), [](const Point& a, const Point& b) {
            if (a.x != b.x) return a.x < b.x;
            return a.y < b.y;
        });
        
        BIT bit(ys.size());
        map<pair<int, int>, pair<int, int>> last_segment_info;
        long long max_area = -1;
        
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && points[j].x == points[i].x) {
                j++;
            }
            
            // 1. Check segments for potential rectangles
            for (int k = i; k < j - 1; k++) {
                int y1 = points[k].y;
                int y2 = points[k+1].y;
                int cy1 = get_y(y1);
                int cy2 = get_y(y2);
                
                int s_before = bit.query(cy2) - bit.query(cy1 - 1);
                if (last_segment_info.count({y1, y2})) {
                    auto info = last_segment_info[{y1, y2}];
                    int x_prev = info.first;
                    int s_prev_after = info.second;
                    
                    if (s_before == s_prev_after) {
                        long long area = (long long)(points[i].x - x_prev) * (y2 - y1);
                        if (area > max_area) max_area = area;
                    }
                }
            }
            
            // 2. Add points of current column to BIT
            for (int k = i; k < j; k++) {
                bit.update(get_y(points[k].y), 1);
            }
            
            // 3. Update segment info for next steps
            for (int k = i; k < j - 1; k++) {
                int y1 = points[k].y;
                int y2 = points[k+1].y;
                int cy1 = get_y(y1);
                int cy2 = get_y(y2);
                int s_after = bit.query(cy2) - bit.query(cy1 - 1);
                last_segment_info[{y1, y2}] = {points[i].x, s_after};
            }
            
            i = j;
        }
        
        return max_area;
    }
};
# @lc code=end