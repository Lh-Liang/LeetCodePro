#
# @lc app=leetcode id=3503 lang=cpp
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution {
public:
    int longestPalindrome(string s, string t) {
        int m = s.size();
        int n = t.size();
        int ans = 0;
        // Collect options for substrings of s including empty
        vector<pair<int,int>> opts_s;
        // Add empty substring option
        opts_s.push_back({-1, 0}); // start -1 indicates invalid but length zero
        // Add non-empty substrings
        for (int l = 1; l <= m; ++l) {
            for (int i = 0; i + l <= m; ++i) {
                opts_s.push_back({i,l});
            }
        }
        // Options for t
        vector<pair<int,int>> opts_t;
        opts_t.push_back({-1,0}); //empty
        for (int l = 1; l <= n; ++l) {
            for (int i = 0; i + l <= n; ++i) {
                opts_t.push_back({i,l});
            }
        }
        
        // Helper lambda to get character of concatenated string given position
        auto get_char = [&](int pos,
                            const pair<int,int>& opt_a,
                            const pair<int,int>& opt_b){
            int len_a = opt_a.second;
            int start_a = opt_a.first;
            int start_b = opt_b.first;
            if(pos < len_a){
                return s[start_a + pos]; // safe because start_a valid when len_a>0
            }else{
                return t[start_b + pos - len_a]; // safe because start_b valid when opt_b.second>0
The lambda assumes that opt_a.second>0 implies opt_a.first>=0 ; similarly opt_b.second>0 implies opt_b.first>=0 ; However when opt_a.second==0 , the branch goes into else regardless ; but then pos >=len_a , so else branch uses start_b ; however if also opt_b.second==0 , there will never call this lambda because total length would be zero ; In our loops skip total_len==zero . Therefore safe . 	}		};		// Iterate over all pairs		for(auto& opt_s : opts_s){			for(auto& opt_t : opts_t){				int total_len = opt_s.second + opt_t.second;				if(total_len == 0 || total_len <= ans)	 continue ; // skip both empty or cannot beat current ans early prune optional 			// Check palindrome using two pointers	bool ok=true;	int left=0 , right=total_len-1 ; while(left<right){	char left_char=get_char(left ,opt_s ,opt_t); 	char right_char=get_char(right ,opt_s ,opt_t); 	if(left_char !=right_char){ok=false ; break ;} 	left++ ; right-- ; } 	if(ok){ans=max(ans,total_len);}	}}return ans ;}};"}}}