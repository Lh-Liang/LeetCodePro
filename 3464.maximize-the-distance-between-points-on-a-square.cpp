//
// @lc app=leetcode id=3464 lang=cpp
//
// [3464] Maximize the Distance Between Points on a Square
//

// @lc code=start
class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        int n = points.size();
        long long L = 4LL * side;
        vector<long long> pos(n);
        
        // Convert points to perimeter positions
        for (int i = 0; i < n; i++) {
            int x = points[i][0], y = points[i][1];
            if (y == 0) pos[i] = x;  // Bottom edge
            else if (x == side) pos[i] = (long long)side + y;  // Right edge
            else if (y == side) pos[i] = 3LL * side - x;  // Top edge
            else pos[i] = 4LL * side - y;  // Left edge
        }
        sort(pos.begin(), pos.end());
        
        // Create doubled array for circular handling
        vector<long long> ext(2 * n);
        for (int i = 0; i < n; i++) {
            ext[i] = pos[i];
            ext[i + n] = pos[i] + L;
        }
        
        // Check if we can select k points with min distance >= D
        auto check = [&](long long D) -> bool {
            for (int i = 0; i < n; i++) {
                int cnt = 1, cur = i;
                long long lim = pos[i] + L;
                for (int j = 0; j < k - 1; j++) {
                    long long tgt = ext[cur] + D;
                    int idx = lower_bound(ext.begin(), ext.end(), tgt) - ext.begin();
                    if (idx >= 2 * n || ext[idx] >= lim) break;
                    cur = idx;
                    cnt++;
                }
                // Check wrap-around distance
                if (cnt == k && lim - ext[cur] >= D) return true;
            }
            return false;
        };
        
        // Binary search for maximum minimum distance
        long long lo = 1, hi = L / k, ans = 0;
        while (lo <= hi) {
            long long mid = (lo + hi) / 2;
            if (check(mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }
};
// @lc code=end