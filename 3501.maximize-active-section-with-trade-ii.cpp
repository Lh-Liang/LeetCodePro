#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.length();
        vector<int> pref1(n + 1, 0);
        for (int i = 0; i < n; ++i) pref1[i + 1] = pref1[i] + (s[i] == '1');

        struct Block { int start, end, len; };
        vector<Block> zeros, ones;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && s[j] == s[i]) j++;
            if (s[i] == '0') zeros.push_back({i, j - 1, j - i});
            else ones.push_back({i, j - 1, j - i});
            i = j;
        }

        int nZ = zeros.size(), nO = ones.size();
        vector<int> z_starts(nZ), o_starts(nO);
        for (int i = 0; i < nZ; ++i) z_starts[i] = zeros[i].start;
        for (int i = 0; i < nO; ++i) o_starts[i] = ones[i].start;

        int K = (n > 0) ? log2(max(nZ, nO)) + 1 : 1;
        vector<vector<int>> stZmax(K, vector<int>(nZ)), stOmin(K, vector<int>(nO)), stZSum(K, vector<int>(max(0, nZ - 1)));

        for (int i = 0; i < nZ; ++i) stZmax[0][i] = zeros[i].len;
        for (int i = 0; i < nO; ++i) stOmin[0][i] = ones[i].len;
        for (int i = 0; i < nZ - 1; ++i) stZSum[0][i] = zeros[i].len + zeros[i+1].len;

        for (int k = 1; k < K; ++k) {
            for (int i = 0; i + (1 << k) <= nZ; ++i) stZmax[k][i] = max(stZmax[k - 1][i], stZmax[k - 1][i + (1 << (k - 1))]);
            for (int i = 0; i + (1 << k) <= nO; ++i) stOmin[k][i] = min(stOmin[k - 1][i], stOmin[k - 1][i + (1 << (k - 1))]);
            for (int i = 0; i + (1 << k) <= nZ - 1; ++i) stZSum[k][i] = max(stZSum[k - 1][i], stZSum[k - 1][i + (1 << (k - 1))]);
        }

        auto queryMax = [&](const vector<vector<int>>& st, int l, int r) {
            if (l > r) return -1000000000;
            int k = log2(r - l + 1);
            return max(st[k][l], st[k][r - (1 << k) + 1]);
        };
        auto queryMin = [&](const vector<vector<int>>& st, int l, int r) {
            if (l > r) return 1000000000;
            int k = log2(r - l + 1);
            return min(st[k][l], st[k][r - (1 << k) + 1]);
        };

        vector<int> results;
        for (auto& q : queries) {
            int li = q[0], ri = q[1];
            int firstO = lower_bound(o_starts.begin(), o_starts.end(), li) - o_starts.begin();
            int lastO = upper_bound(o_starts.begin(), o_starts.end(), ri) - o_starts.begin() - 1;
            int firstZ = lower_bound(z_starts.begin(), z_starts.end(), li) - z_starts.begin();
            int lastZ = upper_bound(z_starts.begin(), z_starts.end(), ri) - z_starts.begin() - 1;

            int internalO_l = firstO, internalO_r = lastO;
            if (internalO_l <= lastO && ones[internalO_l].start == li) internalO_l++;
            if (internalO_r >= firstO && ones[internalO_r].end == ri) internalO_r--;

            int gain = 0;
            if (internalO_l <= internalO_r) {
                int zMax = queryMax(stZmax, firstZ + 1, lastZ - 1);
                zMax = max({zMax, (firstZ <= lastZ ? min(zeros[firstZ].end, ri) - max(zeros[firstZ].start, li) + 1 : 0), (lastZ >= firstZ ? min(zeros[lastZ].end, ri) - max(zeros[lastZ].start, li) + 1 : 0)});
                int oMin = queryMin(stOmin, internalO_l, internalO_r);
                int zSum = queryMax(stZSum, firstZ, lastZ - 1);
                gain = max(zSum, zMax - oMin);
            }
            results.push_back(pref1[ri + 1] - pref1[li] + (gain > 0 ? gain : 0));
        }
        return results;
    }
};