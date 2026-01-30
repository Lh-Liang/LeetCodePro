#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int getLCP(const string& s1, const string& s2) {
        int len = min((int)s1.length(), (int)s2.length());
        for (int i = 0; i < len; ++i) {
            if (s1[i] != s2[i]) return i;
        }
        return len;
    }

    vector<int> longestCommonPrefix(vector<string>& words) {
        int n = words.size();
        vector<int> ans(n, 0);
        if (n <= 1) return ans;

        vector<int> adjLCP(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            adjLCP[i] = getLCP(words[i], words[i + 1]);
        }

        vector<int> preMax(n, 0);
        preMax[0] = adjLCP[0];
        for (int i = 1; i < n - 1; ++i) {
            preMax[i] = max(preMax[i - 1], adjLCP[i]);
        }

        vector<int> sufMax(n, 0);
        sufMax[n - 2] = adjLCP[n - 2];
        for (int i = n - 3; i >= 0; --i) {
            sufMax[i] = max(sufMax[i + 1], adjLCP[i]);
        }

        for (int i = 0; i < n; ++i) {
            int currentMax = 0;
            // Max from pairs to the left of i: adjLCP[0...i-2]
            if (i >= 2) {
                currentMax = max(currentMax, preMax[i - 2]);
            }
            // Max from pairs to the right of i: adjLCP[i+1...n-2]
            if (i + 1 <= n - 2) {
                currentMax = max(currentMax, sufMax[i + 1]);
            }
            // Max from the bridge pair (i-1, i+1)
            if (i > 0 && i < n - 1) {
                currentMax = max(currentMax, getLCP(words[i - 1], words[i + 1]));
            }
            ans[i] = currentMax;
        }
        return ans;
    }
};