#include <bits/stdc++.h>
using namespace std;

//
// @lc app=leetcode id=3435 lang=cpp
//
// [3435] Frequencies of Shortest Supersequences
//

// @lc code=start
class Solution {
    static bool isDAG(int subset, const vector<int>& inMask, int n) {
        int rem = subset;
        while (rem) {
            bool progress = false;
            for (int i = 0; i < n; i++) {
                if (rem & (1 << i)) {
                    // indegree within remaining nodes is 0
                    if ((inMask[i] & rem) == 0) {
                        rem &= ~(1 << i);
                        progress = true;
                    }
                }
            }
            if (!progress) return false; // cycle exists
        }
        return true;
    }

public:
    vector<vector<int>> supersequences(vector<string>& words) {
        bool present[26] = {};
        for (auto &w : words) {
            present[w[0] - 'a'] = true;
            present[w[1] - 'a'] = true;
        }

        vector<int> letters;
        letters.reserve(16);
        for (int c = 0; c < 26; c++) if (present[c]) letters.push_back(c);
        int n = (int)letters.size();

        int id[26];
        fill(begin(id), end(id), -1);
        for (int i = 0; i < n; i++) id[letters[i]] = i;

        vector<int> outMask(n, 0), inMask(n, 0);
        int reqDup = 0;

        for (auto &w : words) {
            int a = id[w[0] - 'a'];
            int b = id[w[1] - 'a'];
            if (a == b) {
                reqDup |= (1 << a);
            } else {
                if (((outMask[a] >> b) & 1) == 0) {
                    outMask[a] |= (1 << b);
                    inMask[b] |= (1 << a);
                }
            }
        }

        int allMask = (n == 32 ? -1 : ((1 << n) - 1));
        int allowed = allMask & ~reqDup; // only these can be kept non-duplicated

        int bestSize = -1;
        vector<int> bestU;

        // Enumerate all subsets U of allowed.
        for (int U = allowed;; U = (U - 1) & allowed) {
            if (isDAG(U, inMask, n)) {
                int sz = __builtin_popcount((unsigned)U);
                if (sz > bestSize) {
                    bestSize = sz;
                    bestU.clear();
                }
                if (sz == bestSize) bestU.push_back(U);
            }
            if (U == 0) break;
        }

        vector<vector<int>> ans;
        ans.reserve(bestU.size());

        for (int U : bestU) {
            int D = allMask ^ U; // duplicated letters
            vector<int> freq(26, 0);
            for (int i = 0; i < n; i++) {
                int ch = letters[i];
                freq[ch] = 1 + ((D >> i) & 1);
            }
            ans.push_back(std::move(freq));
        }
        return ans;
    }
};
// @lc code=end
