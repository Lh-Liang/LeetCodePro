#
# @lc app=leetcode id=3387 lang=python3
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        # Build graph for day 1 and day 2
        def build_graph(pairs, rates):
            graph = defaultdict(dict)
            for (src, dst), rate in zip(pairs, rates):
                graph[src][dst] = rate
                graph[dst][src] = 1.0 / rate
            return graph
        
        graph1 = build_graph(pairs1, rates1)
        graph2 = build_graph(pairs2, rates2)
        
        # Get all reachable currencies from initialCurrency on day 1 with max amounts
        # Use Bellman-Ford like relaxation since no negative cycles (but we have positive multipliers)
        # Actually we can use DFS/BFS with multiplication, but because rates > 0 and we want max,
        # we can treat it as finding max product paths. Since no contradictions, the graph is consistent.
        # We can use a variant of Dijkstra for max product (using log to convert to sum) but simpler:
        # Since n <= 10 edges per day, we can do DP over currencies by relaxing repeatedly.
        
        # Day 1: start with 1.0 in initialCurrency, others 0 (or -inf).
        # We want max amount for each currency after any number of conversions on day 1.
        currencies = set()
        for src, dst in pairs1:
            currencies.add(src)
            currencies.add(dst)
        for src, dst in pairs2:
            currencies.add(src)
            currencies.add(dst)
        currencies.add(initialCurrency)
        
        # Initialize amounts for day 1
        amount1 = {c: -float('inf') for c in currencies}
        amount1[initialCurrency] = 1.0
        
        # Relax edges repeatedly up to |currencies| times (Bellman-Ford for max)
        # Since we have at most 20 nodes (10 edges each day), we can do up to |V|-1 relaxations.
        for _ in range(len(currencies)):
            updated = False
            for src in list(amount1.keys()):
                if amount1[src] == -float('inf'):
                    continue
                for dst, rate in graph1.get(src, {}).items():
                    new_amount = amount1[src] * rate
                    if new_amount > amount1[dst]:
                        amount1[dst] = new_amount
                        updated = True
            if not updated:
                break
        
        # Now for day 2, we need to consider that we can start with any currency from day 1.
        # We want max amount of initialCurrency at the end of day 2.
        # So we need to compute for each starting currency (with amount from day 1) the max amount of initialCurrency after day 2.
        # Let's compute max amount of each currency after day 2 if we start with 1 unit of that currency.
        # Then final amount = amount1[start] * conversion_factor from start to initialCurrency after day2.
        
        # Compute best conversion from each currency to initialCurrency on day2.
        # We can reverse the graph and compute from initialCurrency? Actually we want max product from any currency to initialCurrency.
        # Since conversions are reversible with inverse rates, we can treat the graph as undirected with multiplicative weights.
        # But careful: the conversion from A to B is rate r, and B to A is 1/r. So the graph is symmetric in terms of multiplication.
        # So the max product from start to target is the same as max product from target to start? Not exactly because direction matters but inverse edges exist.
        # Actually because for every edge we have its inverse, the graph is effectively undirected with weights as multipliers.
        # Then the maximum product from start to target is the same as maximum product from target to start? Let's see: if there's a path from start to target with product P, then there's a path from target to start with product 1/P. So not same. But we want maximum product from start to target; that's equivalent to minimum product from target to start? No.
 	# However we can compute all-pairs shortest paths (max product) using Floyd-Warshall like algorithm but with multiplication.																							   	   	   	   	   	   	   	   	   	   	   	   	   	   Since number of currencies small (<=21 maybe), we can compute all-pairs max product using repeated relaxation or Floyd-Warshall.	    	    	    Let's compute a matrix dist where dist[a][b] = max product from a to b using day2 conversions. Initialize with -inf except dist[a][a]=1.0 and edges given.	    Then run Floyd-Warshall style updates: For each k, i, j: dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j]).	    Because we have inverse edges already added in graph2, this will capture all possibilities.	    After computing all pairs, the final answer is max over start currency: amount1[start] * dist[start][initialCurrency].	    Note that we might also choose not to convert on day2: that means start remains same and dist[start][initialCurrency] might be less than if we convert; but if start == initialCurrency and no conversion gives factor 1.	    Also note that we could also not convert on day1: that means starting with initialCurrency and factor 1.	    So overall answer is max_{start} amount1[start] * dist[start][initialCurrency].	    This covers both days possibly zero conversions.	    Let's implement that.	    First get list of all unique currencies.	t    Build adjacency dict for day2 already done (graph2). Now compute all-pairs max product.	t    We'll use dictionary of dictionaries.	ttttttttttttttttttttttttttttttttttttttttttttttt      cur_list = list(currencies)	n = len(cur_list)	id_to_cur = {i: cur_list[i] for i in range(n)}	cur_to_id = {cur_list[i]: i for i in range(n)}	dist = [[-float('inf')] * n for _ in range(n)]	for i in range(n):	dist[i][i] = 1.0	for src in cur_list:	i = cur_to_id[src]	for dst, rate in graph2.get(src, {}).items():	j = cur_to_id[dst]	dist[i][j] = max(dist[i][j], rate)   # note: there might be multiple edges? but problem says no contradictions so consistent; but still take max just in case?	fActually since no contradictions, rates should be consistent; but there could be multiple paths yielding different products; we want maximum so taking max is fine. Also our initialization includes inverse edges so both directions present.ttNow run Floyd-Warshall updates:	forkinrange(n):foriinrange(n):forjinrange(n):ifdist[i][k]>0anddist[k][j]>0:# avoid negative inf multiplicationnew=dist[i][k]*dist[k][j]ifnew>dist[i][j]:dist[i][j]=newAfter this compute answer:ans=0.0forstartincur_list:i=cur_to_id[start]j=cur_to_id[initialCurrency]ifamount1[start]==-float('inf'):continuefactor=dist[i][j]iffactor==-float('inf'):continuecandidate=amount1[start]*factorans=max(ans,candidate)returnansBut wait: The final answer must be the maximum amount of initialCurrency. So we need to end up with initialCurrency after day2. That's why we multiply by factor converting start currency back to initialCurrency via day2 conversions.If there is no path from start back to initialCurrency on day2 then factor is -inf; ignore.Finally return ans as float.We should also consider that after day2 you could end up with some other currency and not convert back? But requirement is you want maximum amount of initialCurrency. So you must convert back at some point on day2 or never leave it.So above approach works.Edge cases:- No conversions on either day -> ans should be 1.0.- Day2 may not have path back -> then only consider starting currencies that can be converted back.Note constraints: output at most5e10so float should handle.Test examples.We'll implement accordingly.