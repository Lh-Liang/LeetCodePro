#
# @lc app=leetcode id=3470 lang=cpp
#
# [3470] Permutations IV
#

# @lc code=start
class Solution {
public:
    vector<int> permute(int n, long long k) {
        vector<int> odds, evens;
        for (int i = 1; i <= n; ++i) {
            if (i % 2 == 0) evens.push_back(i);
            else odds.push_back(i);
        }
        
        auto combinatorial_count = [&](int odd_count, int even_count) -> long long {
            // A function to calculate valid permutation count under current configuration
            // Utilize combinatorial mathematics instead of factorials directly.
            return ...; // Implement a more efficient counting method that respects alternation constraints.
        };
        
        if (k > combinatorial_count(odds.size(), evens.size())) return {};
        
        vector<int> result;
        bool useOdds = true;

        while (!odds.empty() || !evens.empty()) {
            long long count = useOdds ? combinatorial_count(odds.size() - 1, evens.size()) : combinatorial_count(odds.size(), evens.size() - 1);
            int index = (k - 1) / count;
            k -= index * count;
            
            if (useOdds && index < odds.size()) {
                result.push_back(odds[index]);
                odds.erase(odds.begin() + index);
                useOdds = false;
            } else if (!useOdds && index < evens.size()) {
                result.push_back(evens[index]);
                evens.erase(evens.begin() + index);
                useOdds = true;
            } else {
                break;
            }
        }
        return result;
    }
};
# @lc code=end