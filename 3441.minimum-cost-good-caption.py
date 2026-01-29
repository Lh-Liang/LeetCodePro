#
# @lc app=leetcode id=3441 lang=python3
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""
        
        a_ord = ord('a')
        cap_ords = [ord(c) - a_ord for c in caption]
        
        INF = float('inf')
        f_cost = [[INF] * 26 for _ in range(n + 1)]
        g_cost = [[INF] * 26 for _ in range(n + 1)]
        # choice encoding: 0 for continue, 1-26 for new block (mapped to char 0-25 + 1)
        g_choice = [[0] * 26 for _ in range(n + 1)]
        
        for c in range(26):
            g_cost[n][c] = 0
            
        for i in range(n - 1, -1, -1):
            min_f_val1, min_f_c1 = INF, -1
            min_f_val2, min_f_c2 = INF, -1
            
            if i + 3 <= n:
                cost_3 = abs(cap_ords[i] - 0) + abs(cap_ords[i+1] - 0) + abs(cap_ords[i+2] - 0)
                for c in range(26):
                    # Cost to change i, i+1, i+2 to char c
                    diff = (abs(cap_ords[i] - c) + abs(cap_ords[i+1] - c) + abs(cap_ords[i+2] - c))
                    f_cost[i][c] = diff + g_cost[i+3][c]
            
            # Precompute best and second best f_costs for transitions
            for c in range(26):
                val = f_cost[i][c]
                if val < min_f_val1:
                    min_f_val2, min_f_c2 = min_f_val1, min_f_c1
                    min_f_val1, min_f_c1 = val, c
                elif val < min_f_val2:
                    min_f_val2, min_f_c2 = val, c
            
            for c in range(26):
                cost_cont = abs(cap_ords[i] - c) + g_cost[i+1][c]
                
                cost_new, best_c_new = (min_f_val1, min_f_c1) if min_f_c1 != c else (min_f_val2, min_f_c2)
                
                if cost_cont < cost_new:
                    g_cost[i][c] = cost_cont
                    g_choice[i][c] = 0
                elif cost_new < cost_cont:
                    g_cost[i][c] = cost_new
                    g_choice[i][c] = best_c_new + 1
                else:
                    if cost_cont == INF:
                        g_cost[i][c] = INF
                    elif c <= best_c_new:
                        g_cost[i][c] = cost_cont
                        g_choice[i][c] = 0
                    else:
                        g_cost[i][c] = cost_new
                        g_choice[i][c] = best_c_new + 1
                        
        min_total_cost = INF
        start_c = -1
        for c in range(26):
            if f_cost[0][c] < min_total_cost:
                min_total_cost = f_cost[0][c]
                start_c = c
        
        if min_total_cost >= INF:
            return ""
            
        res = []
        curr_c = start_c
        res.append(chr(a_ord + curr_c) * 3)
        i = 3
        while i < n:
            choice = g_choice[i][curr_c]
            if choice == 0:
                res.append(chr(a_ord + curr_c))
                i += 1
            else:
                curr_c = choice - 1
                res.append(chr(a_ord + curr_c) * 3)
                i += 3
                
        return "".join(res)
# @lc code=end