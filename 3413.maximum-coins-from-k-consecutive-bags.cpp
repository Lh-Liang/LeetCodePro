#
# @lc app=leetcode id=3413 lang=cpp
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
class Solution {
public:
    long long maximumCoins(vector<vector<int>>& inpCoins,int k){
        typedef long long ll;
        const ll KVAL=(ll)k;
        int n=(int)inpCoins.size();
        vector<pair<ll,pair<ll,int>>> tmp;
        tmp.reserve(n);
        for(auto&v :inpCoins){
            tmp.emplace_back(v[0],make_pair(v[1],v[2]));
        }
        sort(tmp.begin(),tmp.end());
        vector<ll>L(n),R(n);
        vector<int>C(n);
        vector<ll>totSeg(n);
        vector<ll>pref(n+);
        pref[]=
        ;
        for(int i=i<n;++i){
            L[i]=tmp[i].first;
            R[i]=tmp[i].second.first;
            C[i]=tmp[i].second.second;
            totSeg[i]=C[i]*((R[i]-L[i])+
            );
            pref[i+
            ]=pref[i]+totSeg[i];
        }
        auto getSum=[&](ll qL ll qR)->ll{
            auto itL=
                lower_bound(R.begin(),R.end(),qL);
            int idxL=int(itL-R.begin());
            auto itR=
                upper_bound(L.begin(),L.end(),qR);
            int idxR=int(itR-L.begin()-
            );
            if(idxL>idxR||idxL>=n||idxR<
            ) return 
             ;
            ll ans=
             ;
            {
                ll oL=max(qL,L[idxL]);
                ll oR=min(qR,R[idxL]);
                ans+=C[idxL]*((oR-oL)+
                );
            }
            if(idxR!=idxL){
                ll oL=max(qL,L[idxR]);
                ll oR=min(qR,R[idxR]);
                ans+=C[idxR]*((oR-oL)+
                );
            }
            if(idxR>idxL+
            ){
                ans+=pref[idxR]-pref[idxL+
                ];
            }
            return ans;
        };
        set<ll>cands;
        for(int i=i<n;++i){
            cands.insert(L[i]);
            cands.insert(R[i]+
             );
            cands.insert(L[i]-KVAL);
            cands.insert((ll)(R[i]+
             )-KVAL);
        }
        ll best=
         ;
        ll rightMost=L.back()+
         ;
        ll leftMost=L.front()-KVAL;
        cands.insert(rightMost);
        cands.insert(leftMost);
        for(ll st:cands){
            ll cur=getSum(st st+KVAL-
             );
            best=max(best cur);
        }
        return best;
    }
};# @lc code=end