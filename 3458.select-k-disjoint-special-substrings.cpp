#
# @lc app=leetcode id=3458 lang=cpp
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        int n = s.size();
        // k == 0 always true
        if(k == 0) return true;
        
        vector<int> first(26,-1), last(26,-1);
        for(int i = 0;i<n;i++){
            int ch = s[i]-'a';
            if(first[ch]==-1){
                first[ch]=i;
            }
            last[ch]=i;
        }
        
        int cnt = 0;
        int idx = 0;
        while(idx<n && cnt<k){
            int ch_idx = s[idx]-'a';
            // skip idx if not first occurrence
            if(first[ch_idx]!=idx){
                idx++;
                continue;
            }
            int far = last[ch_idx];
            int mask = 1<<ch_idx;
            int r = idx;
            bool found=false;
            while(r<n && !found){
                // check closure
                if(r == far){
                    // verify distinct set matches mask
                    int distMask = 0;
                    bool ok=true;
                    vector<bool> seen(26);
                    for(int p = idx;p<=r;p++){
                        int cp=s[p]-'a';
                        distMask |= (1<<cp);
                        seen[cp]=true;
                    }
                    // ensure every bit set corresponds exactly
                    int diff=mask ^ distMask;
                    bool exactMatch=(diff==0);
                    // additionally ensure no extra bits
                    exactMatch &= ((mask|distMask)==mask);
                    
                    // extra verification via frequency
                    bool freqOk=true;
                    for(int cc=0;cc<26 && freqOk;cc++){
                        if(seen[cc]){
                            if(first[cc]<idx || last[cc]>r){
                                freqOk=false;
                            }
                        }
                    }
                    
                    exactMatch &= freqOk;
                    
                    if(exactMatch && r-idx+1<n){
                        cnt++;
                        idx=r+1;
                        found=true;
                        break;
                    }
                }
                // expand
                r++;
                if(r<n){
                    int nc=s[r]-'a';
                    if(first[nc]<idx){
                        break;// violation
                    }
                    far = max(far , last[nc]);
                    mask |= (1<<nc);
                }
            }
            if(!found){
                idx++;
            }
        }
        return cnt>=k;
    }
};
# @lc code=end