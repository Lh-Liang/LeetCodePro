#
# @lc app=leetcode id=3448 lang=cpp
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution {
public:
    long long countSubstrings(string s) {
        long long ans = 0;
        int n = s.size();

        // Step A: Trivial digits {1,2,5}
        for (int i = 0; i < n; ++i) {
            int dig = s[i] - '0';
            if (dig == 1 || dig == 2 || dig == 5)
                ans += i + 1;
        }

        // Step B: Groups using modular arithmetic
        unordered_map<int,int> freq[10]; // indices: m in {3,7,9}
        int idx[] = {3,7,9};             // modulus values
        int inv[] = {                    // inverses of 10 modulo idx[]
            1,
            5,
            1
        };

        int prefMod[]   = {0,0,0};       // current prefix remainders
        int curPowInv[] = {              // current power of modular inverse
            1,
            1,
            1
        };

        // initialise maps with key 0 representing empty prefix
        freq[ idx[0]-idx[0]+??? ]. Actually simpler:
        unordered_map<int,int> freq3,freq7,freq9;
        freq3[0]=freq7[0]=freq9[0]=1;

        // auxiliary lambda to get inverse under small modulus
        auto getInv = [&](int num,int mod){
            num%=mod;
            for(int x=1;x<mod;++x)
                if((num*x)%mod == 1)
                    return x;
            return -1;
        };

        // Already set inv above.

        for(int i=0;i<n;++i){
            int dig=s[i]-'0';
            
            // update prefix remainders
            prefMod[0]=(prefMod[0]*10+dig)%3;
            prefMod[1]=(prefMod[1]*10+dig)%7;
            prefMod[2]=(prefMod[2]*10+dig)%9;

            // compute U values
            int u3=(prefMod[0]*curPowInv[0])%3;
            int u7=(prefMod[1]*curPowInv[1])%7;
            int u9=(prefMod[2]*curPowInv[2])%9;

            // add contributions according to endpoint's digit
            // group {3/6}
            if(dig==3 || dig==6){
                ans+=freq3[u3];
            }
            // group {7}
            if(dig==7){
                ans+=freq7[u7];
            }
            // group {9}
            if(dig==9){
                ans+=freq9[u9];
            }

            // insert current U values into maps before updating curPowInv
            freq3[u3]++;
            freq7[u7]++;
            freq9[u9]++;

            // update powers of inverses
            curPowInv[0]=curPowInv[0]*inv[0]%3;
            curPowInv[1]=curPowInv[1]*inv[1]%7;
            curPowInv[2]=curPowInv[2]*inv[2]%9;
        }

        // Step C‑a: Digit ‘ ’
        for(int i=0;i<n;++i){
            if(s[i]==''){
                ++ans;                       // length >
                if(i>=){
                    int twoDig=(s[i‐]-'")*")+(s[i]-'")();
                    if(twoDig%"){
                        ans+=i;               // > choices
                    }
                }
                
                
                
                
                
                
                
                
                
                 
                 
                  
                  
                   
                   
                    
                    
                     
                     
                      
                      
                       
                       
                        
                        
                         
                         
                          
                          
                           
                           
                            
                            
                             
                             
                              
                              
                               
                               
                                
                                
                                 
                                 
                                  
                                  
                                   
                                   
                                    
                                    
                                     
                                     
                                      
                                      
                                       
                                       
                                        
                                        
                                         
                                         
                                          
                                          
                                           
                                           
                                            
                                            
                                             
                                             
                                              
                                              
                                               
                                               
                                                
                                                
                                                 
                                                 
                                                  
                                                  
                                                   
                                                   
                                                    
                                                    
                                                     
                                                     
                                                      
                                                      
                                                       
                                                       
                                                        
                                                        
                                                         
                                                         
                                                          
                                                          
                                                           
                                                           
                                                            
                                                            
                                                             
                                                             
                                                              
                                                              
                                                               
                                                               
                                                                
                                                                
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
         return ans;
    }
};