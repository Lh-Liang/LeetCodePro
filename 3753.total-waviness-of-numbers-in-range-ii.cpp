#
# @lc app=leetcode id=3753 lang=cpp
#
# [3753] Total Waviness of Numbers in Range II
#
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
    static inline int isPeakOrValley(int a, int b, int c) {
        return ((b > a && b > c) || (b < a && b < c)) ? 1 : 0;
    }

    long long solve(long long n) {
        if (n < 0) return 0;
        string s = to_string(n);
        int L = (int)s.size();

        // last1, last2 in [0..9], sentinel 10 means "not available"
        static long long cnt[2][11][11];
        static long long sum[2][11][11];
        static long long ncnt[2][11][11];
        static long long nsum[2][11][11];

        for (int t = 0; t < 2; t++)
            for (int a = 0; a <= 10; a++)
                for (int b = 0; b <= 10; b++)
                    cnt[t][a][b] = sum[t][a][b] = 0;

        // Start: tight=1, not started => last1=10, last2=10
        cnt[1][10][10] = 1;

        for (int pos = 0; pos < L; pos++) {
            for (int t = 0; t < 2; t++)
                for (int a = 0; a <= 10; a++)
                    for (int b = 0; b <= 10; b++)
                        ncnt[t][a][b] = nsum[t][a][b] = 0;

            int limDigit = s[pos] - '0';

            for (int tight = 0; tight <= 1; tight++) {
                int limit = tight ? limDigit : 9;
                for (int last2 = 0; last2 <= 10; last2++) {
                    for (int last1 = 0; last1 <= 10; last1++) {
                        long long c = cnt[tight][last2][last1];
                        if (c == 0) continue;
                        long long sm = sum[tight][last2][last1];

                        bool started = (last1 != 10);

                        for (int x = 0; x <= limit; x++) {
                            int ntight = (tight && x == limit);

                            int nlast2 = 10, nlast1 = 10;
                            int add = 0;

                            if (!started) {
                                if (x == 0) {
                                    // still not started
                                    nlast2 = 10;
                                    nlast1 = 10;
                                } else {
                                    // start number
                                    nlast2 = 10;
                                    nlast1 = x;
                                }
                            } else {
                                if (last2 == 10) {
                                    // length becomes 2, still cannot form peak/valley
                                    nlast2 = last1;
                                    nlast1 = x;
                                } else {
                                    // last1 becomes an interior digit now
                                    add = isPeakOrValley(last2, last1, x);
                                    nlast2 = last1;
                                    nlast1 = x;
                                }
                            }

                            ncnt[ntight][nlast2][nlast1] += c;
                            nsum[ntight][nlast2][nlast1] += sm + c * add;
                        }
                    }
                }
            }

            for (int t = 0; t < 2; t++)
                for (int a = 0; a <= 10; a++)
                    for (int b = 0; b <= 10; b++) {
                        cnt[t][a][b] = ncnt[t][a][b];
                        sum[t][a][b] = nsum[t][a][b];
                    }
        }

        long long total = 0;
        for (int tight = 0; tight <= 1; tight++)
            for (int last2 = 0; last2 <= 10; last2++)
                for (int last1 = 0; last1 <= 10; last1++)
                    total += sum[tight][last2][last1];
        return total;
    }

public:
    long long totalWaviness(long long num1, long long num2) {
        return solve(num2) - solve(num1 - 1);
    }
};
// @lc code=end
