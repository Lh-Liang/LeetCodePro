#
# @lc app=leetcode id=3449 lang=cpp
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
class Solution {
public:
    long long maxScore(vector<int>& points, int m) {
        int n = points.size();
        auto check = [&](long long mid) -> bool {
            long long cnt = 0;
            for(int p : points){
                // cnt += ceil(mid / p)
                cnt += mid % p == 0 ? mid / p : mid / p + 1;
                // early exit
                if(cnt > m) return false;
            }
            return cnt <= m;
        };

        long long mx = *max_element(points.begin(), points.end());
        long long lo = 0;
        long long hi = mx * (long long)m; // upper bound
        while(lo < hi){
            long long mid = lo + (hi-lo+1)/2;
            if(check(mid)){
                lo = mid;
            }else{
                hi = mid - 1;
            }
        }
        return lo;
    }
};
# @lc code=end