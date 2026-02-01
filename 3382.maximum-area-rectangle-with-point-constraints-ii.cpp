#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class FenwickTree {
    vector<int> tree;
public:
    FenwickTree(int n) : tree(n + 1, 0) {}
    void add(int i, int val) {
        for (; i < tree.size(); i += i & -i) tree[i] += val;
    }
    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
    int query(int l, int r) {
        return query(r) - query(l - 1);
    }
};

class Solution {
public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        int n = xCoord.size();
        vector<pair<int, int>> points(n);
        vector<int> ys = yCoord;
        sort(ys.begin(), ys.end());
        ys.erase(unique(ys.begin(), ys.end()), ys.end());
        
        auto get_y = [&](int y) {
            return lower_bound(ys.begin(), ys.end(), y) - ys.begin() + 1;
        };

        for (int i = 0; i < n; ++i) {
            points[i] = {xCoord[i], yCoord[i]};
        }
        sort(points.begin(), points.end());

        map<pair<int, int>, pair<int, int>> last_seen; // {y1, y2} -> {last_x, last_cnt}
        FenwickTree ft(ys.size());
        long long max_area = -1;

        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && points[j].first == points[i].first) j++;

            // Check pairs at current X
            for (int k = i; k < j - 1; ++k) {
                int y1 = points[k].second;
                int y2 = points[k + 1].second;
                int py1 = get_y(y1);
                int py2 = get_y(y2);
                
                int current_cnt = ft.query(py1, py2);
                if (last_seen.count({y1, y2})) {
                    auto [prev_x, prev_cnt] = last_seen[{y1, y2}];
                    if (current_cnt == prev_cnt) {
                        max_area = max(max_area, (long long)(points[i].first - prev_x) * (y2 - y1));
                    }
                }
                last_seen[{y1, y2}] = {points[i].first, current_cnt};
            }

            // Add current X points to Fenwick after checking to handle "on the border"
            // Actually, to handle points on the border, we update the map before updating FT,
            // but we must ensure the count includes points on the vertical edges.
            for (int k = i; k < j; ++k) {
                ft.add(get_y(points[k].second), 1);
                // Update counts in map to include the points just added on the right edge
            }
            for (int k = i; k < j - 1; ++k) {
                last_seen[{points[k].second, points[k+1].second}].second = ft.query(get_y(points[k].second), get_y(points[k+1].second));
            }

            i = j;
        }

        return max_area;
    }
};