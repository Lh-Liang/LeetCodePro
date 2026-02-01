#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        int n = points.size();
        vector<pair<long long, int>> mapped;
        
        // Step 1: Map 2D boundary points to 1D
        for (int i = 0; i < n; ++i) {
            int x = points[i][0], y = points[i][1];
            long long pos = 0;
            if (y == 0) pos = x;
            else if (x == side) pos = (long long)side + y;
            else if (y == side) pos = (long long)2 * side + (side - x);
            else if (x == 0) pos = (long long)3 * side + (side - y);
            mapped.push_back({pos, i});
        }
        
        sort(mapped.begin(), mapped.end());

        auto getManhattan = [&](int i, int j) {
            return abs(points[mapped[i].second][0] - points[mapped[j].second][0]) + 
                   abs(points[mapped[i].second][1] - points[mapped[j].second][1]);
        };

        // Step 4 & 5: Checker function with cyclic handling
        auto check = [&](int d) {
            // We only need to try starting points within the first 'gap'
            // to ensure we don't miss the optimal selection.
            // Given k is small, we can try several starting points.
            for (int i = 0; i < n / k + 1 && i < n; ++i) {
                int count = 1;
                int lastIdx = i;
                for (int j = i + 1; j < n && count < k; ++j) {
                    if (getManhattan(lastIdx, j) >= d) {
                        lastIdx = j;
                        count++;
                    }
                }
                if (count == k && getManhattan(lastIdx, i) >= d) return true;
            }
            return false;
        };

        // Step 3: Binary Search
        int low = 1, high = 2 * side, ans = 0;
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