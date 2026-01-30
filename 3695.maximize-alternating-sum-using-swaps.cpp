#include <vector>
#include <numeric>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums, vector<vector<int>>& swaps) {
        int n = nums.size();
        vector<int> parent(n);
        iota(parent.begin(), parent.end(), 0);

        // DSU Find with path compression
        auto find_root = [&](auto self, int i) -> int {
            if (parent[i] == i) return i;
            return parent[i] = self(self, parent[i]);
        };

        // Build connected components of indices
        for (const auto& s : swaps) {
            int root_u = find_root(find_root, s[0]);
            int root_v = find_root(find_root, s[1]);
            if (root_u != root_v) {
                parent[root_u] = root_v;
            }
        }

        // Group indices and values by their component root
        // component_data[root] = {vector_of_values, count_of_even_indices}
        struct Component {
            vector<int> values;
            int even_count = 0;
        };
        map<int, Component> groups;

        for (int i = 0; i < n; ++i) {
            int root = find_root(find_root, i);
            groups[root].values.push_back(nums[i]);
            if (i % 2 == 0) {
                groups[root].even_count++;
            }
        }

        long long total_max_sum = 0;

        // Process each component independently
        for (auto& [root, comp] : groups) {
            sort(comp.values.begin(), comp.values.end());
            
            int total_in_comp = comp.values.size();
            int odd_count = total_in_comp - comp.even_count;

            // Smallest 'odd_count' values are assigned to odd indices (subtracted)
            for (int i = 0; i < odd_count; ++i) {
                total_max_sum -= (long long)comp.values[i];
            }
            // Largest 'even_count' values are assigned to even indices (added)
            for (int i = odd_count; i < total_in_comp; ++i) {
                total_max_sum += (long long)comp.values[i];
            }
        }

        return total_max_sum;
    }
};