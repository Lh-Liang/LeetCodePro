class Solution {
public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        int n = xCoord.size();
        // Coordinate compression for scalable preprocessing
        vector<int> xs = xCoord, ys = yCoord;
        sort(xs.begin(), xs.end());
        xs.erase(unique(xs.begin(), xs.end()), xs.end());
        sort(ys.begin(), ys.end());
        ys.erase(unique(ys.begin(), ys.end()), ys.end());
        unordered_map<int, int> x_map, y_map;
        for (int i = 0; i < xs.size(); ++i) x_map[xs[i]] = i;
        for (int i = 0; i < ys.size(); ++i) y_map[ys[i]] = i;
        int X = xs.size(), Y = ys.size();
        // Build 2D prefix sum grid
        vector<vector<int>> grid(X+1, vector<int>(Y+1, 0));
        for (int i = 0; i < n; ++i) {
            grid[x_map[xCoord[i]]+1][y_map[yCoord[i]]+1] = 1;
        }
        for (int i = 1; i <= X; ++i)
            for (int j = 1; j <= Y; ++j)
                grid[i][j] += grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1];
        auto getSum = [&](int x1, int y1, int x2, int y2) {
            return grid[x2][y2] - grid[x1][y2] - grid[x2][y1] + grid[x1][y1];
        };
        set<pair<int, int>> points;
        for (int i = 0; i < n; ++i) points.insert({xCoord[i], yCoord[i]});
        long long max_area = -1;
        // Test all pairs as diagonals
        for (int i = 0; i < n; ++i) {
            for (int j = i+1; j < n; ++j) {
                int x1 = xCoord[i], y1 = yCoord[i], x2 = xCoord[j], y2 = yCoord[j];
                if (x1 == x2 || y1 == y2) continue;
                // Form rectangle corners
                if (points.count({x1, y2}) && points.count({x2, y1})) {
                    int minX = min(x_map[x1], x_map[x2]), maxX = max(x_map[x1], x_map[x2]);
                    int minY = min(y_map[y1], y_map[y2]), maxY = max(y_map[y1], y_map[y2]);
                    // Use prefix sum to check if only the four corners are inside/on border
                    int total = getSum(minX, minY, maxX+1, maxY+1);
                    if (total == 4) {
                        long long area = 1LL * abs(x1 - x2) * abs(y1 - y2);
                        if (area > max_area) max_area = area;
                    }
                }
            }
        }
        return max_area;
    }
};