#include <bits/stdc++.h>
using namespace std;

// @lc app=leetcode id=3441 lang=cpp
//
// [3441] Minimum Cost Good Caption
//

// @lc code=start
class Solution {
public:
    string minCostGoodCaption(string caption) {
        int n = (int)caption.size();
        if (n < 3) return "";

        const int INF = 1e9;
        const int ALPHA = 26;
        const int STATES = ALPHA * 3 + 1; // (letter,cat=1..3) + START
        const int START = ALPHA * 3;

        auto idx = [&](int letter, int cat) { // cat in {1,2,3}
            return letter * 3 + (cat - 1);
        };

        // dp[(i*STATES)+s]
        vector<int> dp((n + 1) * STATES, INF);

        // base at i=n
        for (int l = 0; l < ALPHA; ++l) {
            dp[n * STATES + idx(l, 3)] = 0;
            dp[n * STATES + idx(l, 1)] = INF;
            dp[n * STATES + idx(l, 2)] = INF;
        }
        dp[n * STATES + START] = INF;

        // fill from back
        vector<int> switchCost(ALPHA);
        for (int i = n - 1; i >= 0; --i) {
            int a = caption[i] - 'a';

            // Precompute switchCost[y] = cost of placing y here and starting/being in run length 1.
            int best1 = INF, best2 = INF;
            int best1Letter = -1;
            for (int y = 0; y < ALPHA; ++y) {
                int cost = abs(a - y) + dp[(i + 1) * STATES + idx(y, 1)];
                switchCost[y] = cost;
                if (cost < best1 || (cost == best1 && y < best1Letter)) {
                    best2 = best1;
                    best1 = cost;
                    best1Letter = y;
                } else if (cost < best2) {
                    best2 = cost;
                }
            }

            // START state: choose any letter -> (y,1)
            dp[i * STATES + START] = best1;

            for (int l = 0; l < ALPHA; ++l) {
                // cat=1: must continue same letter -> cat=2
                dp[i * STATES + idx(l, 1)] = abs(a - l) + dp[(i + 1) * STATES + idx(l, 2)];

                // cat=2: must continue same letter -> cat=3
                dp[i * STATES + idx(l, 2)] = abs(a - l) + dp[(i + 1) * STATES + idx(l, 3)];

                // cat=3: can continue (l,3) or switch to y!=l (y,1)
                int cont = abs(a - l) + dp[(i + 1) * STATES + idx(l, 3)];
                int sw = (best1Letter != l ? best1 : best2);
                dp[i * STATES + idx(l, 3)] = min(cont, sw);
            }
        }

        if (dp[0 * STATES + START] >= INF) return "";

        // Reconstruct lexicographically smallest optimal answer.
        string ans;
        ans.reserve(n);
        int prevState = START;
        for (int i = 0; i < n; ++i) {
            int a = caption[i] - 'a';
            int targetCost = dp[i * STATES + prevState];

            int prevLetter = -1, prevCat = 0;
            if (prevState != START) {
                prevLetter = prevState / 3;
                prevCat = (prevState % 3) + 1;
            }

            bool placed = false;
            if (prevState != START && prevCat < 3) {
                // Forced to continue the same letter.
                int y = prevLetter;
                int newCat = prevCat + 1;
                int newState = idx(y, newCat);
                int total = abs(a - y) + dp[(i + 1) * STATES + newState];
                if (total == targetCost) {
                    ans.push_back(char('a' + y));
                    prevState = newState;
                    placed = true;
                }
            } else {
                // Can choose any letter (START or prevCat==3).
                for (int y = 0; y < ALPHA; ++y) {
                    int newState;
                    if (prevState == START) {
                        newState = idx(y, 1);
                    } else {
                        if (y == prevLetter) newState = idx(y, 3); // continue
                        else newState = idx(y, 1);                 // switch
                    }
                    int total = abs(a - y) + dp[(i + 1) * STATES + newState];
                    if (total == targetCost) {
                        ans.push_back(char('a' + y));
                        prevState = newState;
                        placed = true;
                        break;
                    }
                }
            }

            if (!placed) return ""; // should not happen
        }

        // Ensure last run length >= 3
        if (prevState == START) return "";
        int finalCat = (prevState % 3) + 1;
        if (finalCat != 3) return "";

        return ans;
    }
};
// @lc code=end
