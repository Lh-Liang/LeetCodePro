#
# @lc app=leetcode id=3474 lang=cpp
#
# [3474] Lexicographically Smallest Generated String
#

// @lc code=start
class Solution {
public:
    string generateString(string t/*str1*/, string s/*str2*/) {
        int n=t.size(),m=s.size();
        int L=n+m-1;
        vector<char> ans(L,'\0');
        
        // Step 1 : process T constrains
        bool possible=true;
        for(int i=0;i<n && possible;++i){
            if(t[i]=='T'){
                // require substring starting at i equals s
                for(int k=0;k<m;++k){
                    int idx=i+k;
                    char req=s[k];
                    if(ans[idx]=='\0'){
                        ans[idx]=req;
                    }else{
                        if(ans[idx]!=req){
                            possible=false;
                            break;
                        }
                    }
                }
            }
        }
        
        if(!possible){
            return "";
        }

        // Step 2 : collect unsatisfied f-intervals
        vector<bool> sat(n/*only f*/,false);
        vector<vector<int>> unknowPosInIntv(n);
        vector<int> unsatIdx;

        for(int i=0;i<n;++i){
            if(t[i]=='F'){
                bool mis=false;
                vector<int> tmp;
                for(int k=0;k<m;++k){
                    int idx=i+k;
                    char req=s[k];
                    if(ans[idx]=='\0'){
                        tmp.push_back(idx);
                    }else{
                        if(ans[idx]!=req){
                            mis=true;
                            break;
                        }
                    }
                }
                
                // mis==true => already satisfied
                // mis==false => no guaranteed mismatch yet
                
                // Additionally ,if tmp.empty() meaning every char inside window
                // either matches s(k) ,then whole window equals s ==> violation
                // impossible case
                
                // Actually mis==false implies ALL known chars match s,
                // and tmp holds remaining unknows
                
                sat[i]=mis;
                unknowPosInIntv[i]=tmp;
                
                // immediate check : no unknows && mis==false => impossible
                
                /**/if(!mis && tmp.empty()){
                    return "";
                }
                
                
                
            }
        }

        


        








// Now collect indexes of unsatisfied f-intervals
for(int i=0;i<n;++i)
if(t[i]=='F' && !sat[i]){
unsatIdx.push_back(i);
}

if(unsatIdx.empty()){
// All f-intervals satisfied ,just fill missing slots with 'a'
for(int i=0;i<L;++i)
if(ans[i]=='\0')ans[i]='a';
string res(ans.begin(),ans.end());
return res;
}

// Step3 : Greedy select hitting points ,cover all unsatisfied windows.
sort(unsatIdx.begin(),unsatIdx.end(),
[s,m](int a,int b){return a+m-1 < b+m-1;});
vector<bool> cov(unsatIdx.size(),false);
unordered_set<int>H;
for(size_t u=0;u<unsatIdx.size();++u){
if(cov[u])continue;
int start=unsatIdx[u];
int end=start+m-1;
int best=-1;
// pick largest available unknow inside [start,end]
for(int p=end;p>=start;--p)
if(ans[p]=='\0'){
best=p;
break;
}
// According previous logic ,best cannot be -1 .
if(best==-1)
return "";
H.insert(best);
cov[u]=true;
// Mark others containing best also satisfied .
for(size_t v=u+1;v<unsatIdx.size();++v){
int ss=unsatIdx[v];
int ee=ss+m-1;
if(best>=ss && best<=ee)
cov[v]=true;
}
}
// verify coverage just incase .
for(size_t u=0;u<unsatIdx.size();++u)
if(!cov[u]){
bool okk=false;
int ss=unsatIdx[u];
int ee=ss+m-1;
for(int h:H)
if(h>=ss && h<=ee){okk=true;break;}
if(!okk)return "";
}
// Step4 : Assign values .
// First ,assign selected hitting points .
for(int h:H){
unordered_set<char> forbid;
for(int ui :unsatIdx){
int ss=ui;
int ee=ui+m-1;
if(h>=ss && h<=ee){
int offset=h-ss;
forbid.insert(s[offset]);
}
}
char ch='a';
while(ch<='z'&& forbid.count(ch))++ch;
if(ch>'z')return "" ;// impossible .
ans[h]=ch;
}
// Fill rest unknows with 'a'
for(int i=0;i<L;++i)
if(ans[i]=='\0')ans[i]='a';
string res(ans.begin(),ans.end());
// Final verification .
for(int i=0;i<n;++i){
bool eq=true;
for(int k=0;k<m;++k){
int idx=i+k;
char ch=res[idx];
char req=s[k];
if(ch!=req){eq=false;break;}
}
if(t[i]=='T'){
if(!eq)return "";
}else{
//F
if(eq)return "";
}
}
return res ;
    }
};
// @lc code=end