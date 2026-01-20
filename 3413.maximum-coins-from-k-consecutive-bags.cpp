#
# @lc app=leetcode id=3413 lang=cpp
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
class Solution {
    struct Seg {
        long long l, r, c;
    };

    static long long scanStartAtL(vector<Seg>& segs, long long k) {
        sort(segs.begin(), segs.end(), [](const Seg& a, const Seg& b){
            return a.l < b.l;
        });

        int n = (int)segs.size();
        long long ans = 0;
        long long curFull = 0; // sum of fully covered segments in [i, j)
        int j = 0;

        for (int i = 0; i < n; i++) {
            if (j < i) {
                j = i;
                curFull = 0;
            }
            long long start = segs[i].l;
            long long end = start + k - 1;

            while (j < n && segs[j].r <= end) {
                long long len = segs[j].r - segs[j].l + 1;
                curFull += len * segs[j].c;
                j++;
            }

            long long partial = 0;
            if (j < n && segs[j].l <= end) {
                long long overlap = end - segs[j].l + 1;
                if (overlap > 0) partial = overlap * segs[j].c;
            }

            ans = max(ans, curFull + partial);

            // remove seg i if it was fully included in curFull
            if (i < j) {
                long long len = segs[i].r - segs[i].l + 1;
                curFull -= len * segs[i].c;
            }
        }
        return ans;
    }

public:
    long long maximumCoins(vector<vector<int>>& coins, int k) {
        int n = (int)coins.size();
        vector<Seg> segs;
        segs.reserve(n);
        for (auto &v : coins) {
            segs.push_back({(long long)v[0], (long long)v[1], (long long)v[2]});
        }

        long long kk = (long long)k;
        long long best1 = scanStartAtL(segs, kk);

        // mirrored pass to cover windows ending at some r_i
        vector<Seg> rev;
        rev.reserve(n);
        for (auto &s : segs) {
            rev.push_back({-s.r, -s.l, s.c});
        }
        long long best2 = scanStartAtL(rev, kk);

        return max(best1, best2);
    }
};
# @lc code=end
