#
# @lc app=leetcode id=338 lang=cpp
#
# [338] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution {
public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        int n = static_cast<int>(xCoord.size());
        // ----- coordinate compression -----
        vector<int> xs(xCoord);
        vector<int> ys(yCoord);
        sort(xs.begin(),xs.end());
        sort(ys.begin(),ys.end());
        auto last_x = unique(xs.begin(),xs.end());
        auto last_y = unique(ys.begin(),ys.end());
        xs.erase(last_x,xs.end());
        ys.erase(last_y,ys.end());
        
        unordered_map<int,int> mapX;
        unordered_map<int,int> mapY;
        int mx=int(xs.size());
        int my=int(ys.size());
        for(int i=0;i<mx;++i) mapX[xs[i]]=i;
        for(int j=0;j<my;++j) mapY[ys[j]]=j;
        
        // ----- build inverted indexes -----
        vector<vector<int>> cols(mx);
        vector<vector<int>> rows(my);
        
        auto encode=[mx](int ix,int iy)->long long{
            return static_cast<long long>(ix)*mx+iy;
        };
        unordered_set<long long> ptSet;
        ptSet.reserve(n);
        
        for(int k=0;k<n;++k){
            int ix = mapX[xCoord[k]];
            int iy = mapY[yCoord[k]];
            cols[ix].push_back(iy);
            rows[iy].push_back(ix);
            ptSet.insert(encode(ix,iy));
        }
        
        // ----- sort inner lists -----
        for(int i=0;i<mx;++i){
            sort(cols[i].begin(),cols[i].end());
        }
        for(int j=0;j<my;++j){
            sort(rows[j].begin(),rows[j].end());
        }
        
        long long ans=-1;
        
        // ----- scan over consecutive global Y-pairs -----
        for(int b=0;b<my-1;++b){
            int t=b+1;
            long long height = static_cast<long long>(ys[t])-static_cast<long long>(ys[b]);
            const auto& rb = rows[b];
            const auto& rt = rows[t];
            int ib=0 , nb=int(rb.size());
            int it=0 , nt=int(rt.size());
            
            long long lastC_xval=-1;
            while(ib<nb || it<nt){
                bool isC=false;
                long long cur_xval;
                
                if(it>=nt || (ib<nb && rb[ib]<rt[it])){
                    cur_xval=xs[rb[ib++]];
                }else if(ib>=nb || rt[it]<rb[ib]){
                    cur_xval=xs[rt[it++]];
                }else{ // equal
                    cur_xval=xs[rb[ib]];
                    isC=true;
                    ++ib;++it;
                }
                
                if(isC){
                    if(lastC_xval!=-1){
                        long long width = cur_xval-lastC_xval;
                        ans=max(ans , width*height);
                    }
                    lastC_xval = cur_xval;
                }else{
                    lastC_xval=-1;
                }
            }
        }
        
        // ----- scan over consecutive global X-pairs -----
        for(int l=0;l<mx-1;++l){
            int r=l+1;
            long long width = static_cast<long long>(xs[r])-static_cast<long long>(xs[l]);
            const auto& cl = cols[l];
            const auto& cr = cols[r];
            int il=0 , nl=int(cl.size());
            int ir=0 , nr=int(cr.size());
            
            long long lastC_yval=-1;
            while(il<nl || ir<nr){
                bool isC=false;
                long long cur_yval;
                
                if(ir>=nr || (il<nl && cl[il]<cr[ir])){
                    cur_yval=ys[cl[il++]];
                }else if(il>=nl || cr[ir]<cl[il]){
                    cur_yval=ys[cr[ir++]];
                }else{ // equal
                    cur_yval=ys[cl[il]];
                    isC=true;
                    ++il;++ir;
                }
                
                if(isC){
                    if(lastC_yval!=-1){
                        long long height = cur_yval-lastC_yval;
                        ans=max(ans , width*height);
                    }
                    lastC_yval = cur_yval;
                }else{
                    lastC_yval=-1;
                }
            }
        }
        
        return ans==static_cast<long long>(-)?ans:-ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans>?-?:ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans==?-::ans == - ? - : ans;// fallback
    }
};
# @lc code=end