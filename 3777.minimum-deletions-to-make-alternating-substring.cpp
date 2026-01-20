#
# @lc app=leetcode id=3777 lang=cpp
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
#include <vector>
#include <string>

using namespace std;

class Solution {
    vector<int> bit;
    int n;

    // Helper to add value to BIT (1-based index)
    void add(int idx, int val) {
        for (; idx < bit.size(); idx += idx & -idx) {
            bit[idx] += val;
        }
    }

    // Helper to query prefix sum from BIT (1-based index)
    int query(int idx) {
        int sum = 0;
        for (; idx > 0; idx -= idx & -idx) {
            sum += bit[idx];
        }
        return sum;
    }

public:
    vector<int> minDeletions(string s, vector<vector<int>>& queries) {
        n = s.length();
        // bad[i] represents equality of s[i] and s[i+1]
        // mapped to BIT index i + 1
        // Max BIT index needed is n-1 (for bad[n-2]), so size n is sufficient.
        // Using n + 1 for safety and 1-based indexing alignment.
        bit.assign(n + 1, 0);

        // Initialize BIT based on initial string s
        for (int i = 0; i < n - 1; ++i) {
            if (s[i] == s[i + 1]) {
                add(i + 1, 1);
            }
        }

        vector<int> ans;
        ans.reserve(queries.size());

        for (const auto& q : queries) {
            if (q[0] == 1) {
                int j = q[1];
                
                // Update effect on left neighbor pair (j-1, j)
                if (j > 0) {
                    // If equal before flip, they become unequal -> -1
                    // If unequal before flip, they become equal -> +1
                    int delta = (s[j - 1] == s[j]) ? -1 : 1;
                    add(j, delta);
                }
                
                // Update effect on right neighbor pair (j, j+1)
                if (j < n - 1) {
                    int delta = (s[j] == s[j + 1]) ? -1 : 1;
                    add(j + 1, delta);
                }
                
                // Perform the flip
                s[j] = (s[j] == 'A' ? 'B' : 'A');
            } else {
                int l = q[1];
                int r = q[2];
                
                if (l >= r) {
                    ans.push_back(0);
                } else {
                    // We need sum of bad indices from l to r-1
                    // In BIT (1-based), this is range [l+1, r]
                    // Sum is query(r) - query(l)
                    ans.push_back(query(r) - query(l));
                }
            }
        }
        return ans;
    }
};
# @lc code=end