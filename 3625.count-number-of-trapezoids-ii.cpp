#include <vector>
#include <numeric>
#include <algorithm>
#include <cstdlib>

using namespace std;

class Solution {
public:
    int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    struct Segment {
        int dx, dy;
        long long c;
        
        bool operator<(const Segment& other) const {
            if (dx != other.dx) return dx < other.dx;
            if (dy != other.dy) return dy < other.dy;
            return c < other.c;
        }
    };

    struct MidPair {
        long long mx, my;
        int dx, dy;

        bool operator<(const MidPair& other) const {
            if (mx != other.mx) return mx < other.mx;
            if (my != other.my) return my < other.my;
            if (dx != other.dx) return dx < other.dx;
            return dy < other.dy;
        }
    };

    int countTrapezoids(vector<vector<int>>& points) {
        int n = points.size();
        if (n < 4) return 0;

        vector<Segment> segments;
        segments.reserve(n * (n - 1) / 2);
        
        vector<MidPair> midPairs;
        midPairs.reserve(n * (n - 1) / 2);

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];
                
                int g = gcd(abs(dx), abs(dy));
                dx /= g;
                dy /= g;
                
                if (dx < 0 || (dx == 0 && dy < 0)) {
                    dx = -dx;
                    dy = -dy;
                }

                long long c = (long long)dx * points[i][1] - (long long)dy * points[i][0];
                segments.push_back({dx, dy, c});

                long long mx = points[i][0] + points[j][0];
                long long my = points[i][1] + points[j][1];
                midPairs.push_back({mx, my, dx, dy});
            }
        }

        sort(segments.begin(), segments.end());
        sort(midPairs.begin(), midPairs.end());

        long long total_count = 0;
        
        // Step 2: Count trapezoids based on parallel sides
        int m = segments.size();
        for (int i = 0; i < m; ) {
            int j = i;
            // Identify range with same slope
            while (j < m && segments[j].dx == segments[i].dx && segments[j].dy == segments[i].dy) {
                j++;
            }
            
            // Inside this range, group by line constant c
            long long sum_cnt = 0;
            long long sum_sq_cnt = 0;
            
            for (int k = i; k < j; ) {
                int l = k;
                while (l < j && segments[l].c == segments[k].c) {
                    l++;
                }
                long long cnt = l - k;
                sum_cnt += cnt;
                sum_sq_cnt += cnt * cnt;
                k = l;
            }
            
            total_count += (sum_cnt * sum_cnt - sum_sq_cnt) / 2;
            i = j;
        }

        long long parallelograms = 0;
        
        // Step 3: Count parallelograms
        for (int i = 0; i < m; ) {
            int j = i;
            // Identify range with same midpoint
            while (j < m && midPairs[j].mx == midPairs[i].mx && midPairs[j].my == midPairs[i].my) {
                j++;
            }
            
            long long total_pairs = j - i;
            if (total_pairs >= 2) {
                long long bad_combos = 0;
                for (int k = i; k < j; ) {
                    int l = k;
                    while (l < j && midPairs[l].dx == midPairs[k].dx && midPairs[l].dy == midPairs[k].dy) {
                        l++;
                    }
                    long long cnt = l - k;
                    bad_combos += cnt * (cnt - 1) / 2;
                    k = l;
                }
                parallelograms += total_pairs * (total_pairs - 1) / 2 - bad_combos;
            }
            
            i = j;
        }

        return (int)(total_count - parallelograms);
    }
};