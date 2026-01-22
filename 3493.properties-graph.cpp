#
# @lc app=leetcode id=3493 lang=cpp
#
# [3493] Properties Graph
#

# @lc code=start
class Solution {
public:
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size();
        // convert each row to a bitset of presence of numbers 1..100
        vector<bitset<101>> sets(n);
        for (int i = 0; i < n; ++i) {
            // note: values are between 1 and 100 inclusive
            for (int val : properties[i]) {
                sets[i].set(val);
            }
        }
        // DSU initialization
        vector<int> parent(n);
        vector<int> rank(n,0);
        for(int i=0;i<n;++i) parent[i]=i;
        function<int(int)> find = [&](int x)->int{
            if(parent[x]!=x) parent[x]=find(parent[x]);
            return parent[x];
        };
        auto unite = [&](int x,int y){
            int rx=find(x), ry=find(y);
            if(rx==ry) return;
            if(rank[rx]<rank[ry]) parent[rx]=ry;
            else if(rank[rx]>rank[ry]) parent[ry]=rx;
            else{ parent[ry]=rx; rank[rx]++; }
        };
        // iterate over all pairs
        for(int i=0;i<n;++i){
            for(int j=i+1;j<n;++j){
                // compute intersection size
                int cnt=0;
                // iterate over possible numbers from 1 to 100
                // we can use bitwise AND on bitsets and count bits
                bitset<101> common = sets[i] & sets[j];
                cnt = common.count(); // number of set bits
                if(cnt>=k){
                    unite(i,j);
                }
            }
        }
        // count distinct roots
        unordered_set<int> roots;
        for(int i=0;i<n;++i){
            roots.insert(find(i));
        }
        return roots.size();
    }};# @lc code=end