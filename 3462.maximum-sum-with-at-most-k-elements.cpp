#
# @lc app=leetcode id=3462 lang=cpp
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution {
public:
    long long maxSum(vector<vector<int>>& grid , vector< int >& limits , int k ) {
        vector < pair < int , int >> elems ; // pair : value , rownumber
        int n = grid.size();
        for(int i = 0 ; i < n ; ++ i ){
            int m = grid [ i ].size();
            for(int j = 0 ; j < m ; ++ j ){
                elems.emplace_back(grid [ i ] [ j ] , i );
            }
        }
        // sort descending by value
        sort(elems.begin(), elems.end(), []( const pair < int , int >& a , const pair < int , int >& b){
            return a.first > b.first;
        });
        
        vector < int > cntPerRow ( n , 0 );
        long long totalSum = 0 ;
        int taken = 0 ;
        
        for(auto & p : elems){
            int val = p.first;
            int r   = p.second;
            if(cntPerRow[r] < limits[r]){
                totalSum += val;
                cntPerRow[r]++;
                taken++;
                if(taken == k ) break;
            }
        }
        return totalSum;
    }
};
n# @lc code=en