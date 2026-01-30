#include <vector>
#include <numeric>
#include <map>

using namespace std;

class Solution {
public:
    long long countTrapezoids(vector<vector<int>>& points) {
        int n = points.size();
        // Map slope -> {Map line_constant -> count of segments}
        // Slope represented as normalized (dx, dy)
        map<pair<int, int>, map<long long, int>> slope_groups;

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];
                int g = std::gcd(dx, dy);
                dx /= g; dy /= g;
                if (dx < 0 || (dx == 0 && dy < 0)) {
                    dx = -dx;
                    dy = -dy;
                }
                
                // Line equation: dy * x - dx * y = C
                long long C = (long long)dy * points[i][0] - (long long)dx * points[i][1];
                slope_groups[{dx, dy}][C]++;
            }
        }

        long long total_pairs = 0;
        for (auto const& [slope, lines] : slope_groups) {
            long long slope_total_segments = 0;
            long long sum_sq = 0;
            for (auto const& [C, count] : lines) {
                slope_total_segments += count;
                sum_sq += (long long)count * count;
            }
            // Number of pairs of segments with same slope on different lines
            total_pairs += (slope_total_segments * slope_total_segments - sum_sq) / 2;
        }

        // Count parallelograms using midpoint property: (x1+x2, y1+y2)
        map<pair<int, int>, int> midpoints;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int mx = points[i][0] + points[j][0];
                int my = points[i][1] + points[j][1];
                midpoints[{mx, my}]++;
            }
        }

        long long parallelograms = 0;
        for (auto const& [mid, count] : midpoints) {
            if (count >= 2) {
                parallelograms += (long long)count * (count - 1) / 2;
            }
        }

        // Total = (Trapezoids with 1 pair) + 2 * (Parallelograms)
        // We want (Trapezoids with 1 pair) + (Parallelograms)
        return total_pairs - parallelograms;
    }
};