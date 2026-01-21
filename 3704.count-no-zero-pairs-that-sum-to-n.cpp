#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3704 lang=cpp
 *
 * [3704] Count No-Zero Pairs That Sum to N
 */

// @lc code=start
class Solution {
public:
    long long countNoZeroPairs(long long n) {
        vector<int> dig;
        while (n > 0) {
            dig.push_back((int)(n % 10));
            n /= 10;
        }
        int L = (int)dig.size();

        long long memo[20][2][2][2];
        for (int i = 0; i < 20; i++)
            for (int c = 0; c < 2; c++)
                for (int ea = 0; ea < 2; ea++)
                    for (int eb = 0; eb < 2; eb++)
                        memo[i][c][ea][eb] = -1;

        function<long long(int,int,int,int)> dfs = [&](int i, int carry, int endedA, int endedB) -> long long {
            if (i == L) return (carry == 0) ? 1LL : 0LL;
            long long &res = memo[i][carry][endedA][endedB];
            if (res != -1) return res;
            res = 0;

            int nd = dig[i];

            auto digitsFor = [&](int i, int ended) {
                vector<int> v;
                if (i == 0) {
                    // least significant digit must exist and cannot be 0
                    for (int d = 1; d <= 9; d++) v.push_back(d);
                } else {
                    if (ended) {
                        v.push_back(0);
                    } else {
                        // continue with 1..9, or choose 0 to end here (and all higher digits will be 0)
                        v.push_back(0);
                        for (int d = 1; d <= 9; d++) v.push_back(d);
                    }
                }
                return v;
            };

            vector<int> A = digitsFor(i, endedA);
            vector<int> B = digitsFor(i, endedB);

            for (int da : A) {
                int nEndedA = endedA;
                if (i > 0 && endedA == 0 && da == 0) nEndedA = 1;
                for (int db : B) {
                    int nEndedB = endedB;
                    if (i > 0 && endedB == 0 && db == 0) nEndedB = 1;

                    int total = da + db + carry;
                    if (total % 10 != nd) continue;
                    int ncarry = total / 10;
                    res += dfs(i + 1, ncarry, nEndedA, nEndedB);
                }
            }

            return res;
        };

        return dfs(0, 0, 0, 0);
    }
};
// @lc code=end
