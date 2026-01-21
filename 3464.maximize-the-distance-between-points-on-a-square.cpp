#
# @lc app=leetcode id=3464 lang=cpp
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        int n = points.size();
        long long perimeter = 4LL * side;
        
        vector<pair<long long, int>> posIdx(n);
        for (int i = 0; i < n; i++) {
            int x = points[i][0], y = points[i][1];
            long long pos;
            if (y == 0) pos = x;
            else if (x == side) pos = side + (long long)y;
            else if (y == side) pos = 3LL * side - x;
            else pos = 4LL * side - y;
            posIdx[i] = {pos, i};
        }
        sort(posIdx.begin(), posIdx.end());
        
        vector<long long> pos(n);
        vector<pair<int, int>> coords(n);
        for (int i = 0; i < n; i++) {
            pos[i] = posIdx[i].first;
            int origIdx = posIdx[i].second;
            coords[i] = {points[origIdx][0], points[origIdx][1]};
        }
        
        vector<long long> extPos(2 * n);
        for (int i = 0; i < n; i++) {
            extPos[i] = pos[i];
            extPos[n + i] = pos[i] + perimeter;
        }
        
        long long lo = 0, hi = 2LL * side;
        while (lo < hi) {
            long long mid = lo + (hi - lo + 1) / 2;
            if (canAchieve(mid, extPos, coords, perimeter, k, side, n)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return (int)lo;
    }
    
    bool canAchieve(long long d, vector<long long>& extPos, vector<pair<int,int>>& coords, 
                    long long perimeter, int k, int side, int n) {
        for (int start = 0; start < n; start++) {
            long long startPos = extPos[start];
            
            if (d <= side) {
                int count = 1;
                int lastIdx = start;
                
                while (count < k) {
                    long long target = extPos[lastIdx] + d;
                    auto it = lower_bound(extPos.begin() + lastIdx + 1, extPos.begin() + start + n, target);
                    if (it == extPos.begin() + start + n || *it >= startPos + perimeter) break;
                    lastIdx = it - extPos.begin();
                    count++;
                }
                
                if (count >= k && perimeter - (extPos[lastIdx] - startPos) >= d) return true;
            } else {
                vector<int> selected = {start};
                int lastIdx = start;
                
                for (int idx = start + 1; idx < start + n && (int)selected.size() < k; idx++) {
                    if (extPos[idx] >= startPos + perimeter) break;
                    if (extPos[idx] - extPos[lastIdx] < d) continue;
                    
                    int sortedIdx = idx % n;
                    bool valid = true;
                    for (int s : selected) {
                        long long manhattan = abs(coords[sortedIdx].first - coords[s].first) + 
                                             abs(coords[sortedIdx].second - coords[s].second);
                        if (manhattan < d) {
                            valid = false;
                            break;
                        }
                    }
                    
                    if (valid) {
                        selected.push_back(sortedIdx);
                        lastIdx = idx;
                    }
                }
                
                if ((int)selected.size() >= k) {
                    int lastSorted = selected.back();
                    int firstSorted = selected.front();
                    long long manhattan = abs(coords[lastSorted].first - coords[firstSorted].first) + 
                                         abs(coords[lastSorted].second - coords[firstSorted].second);
                    if (manhattan >= d) return true;
                }
            }
        }
        return false;
    }
};
# @lc code=end