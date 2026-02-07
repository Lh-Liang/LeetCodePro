#
# @lc app=leetcode id=3387 lang=golang
#
# [3387] Maximize Amount After Two Days of Conversions
#
# @lc code=start
func maxAmount(initialCurrency string, pairs1 [][]string, rates1 []float64, pairs2 [][]string, rates2 []float64) float64 {
    // Helper to build a bidirectional graph
    buildGraph := func(pairs [][]string, rates []float64) map[string]map[string]float64 {
        graph := map[string]map[string]float64{}
        for i, pair := range pairs {
            from, to := pair[0], pair[1]
            r := rates[i]
            if graph[from] == nil { graph[from] = map[string]float64{} }
            if graph[to] == nil { graph[to] = map[string]float64{} }
            graph[from][to] = r
            graph[to][from] = 1.0 / r
        }
        return graph
    }
    // Bellman-Ford like: propagate maximal values
    propagate := func(graph map[string]map[string]float64, start string, amount float64) map[string]float64 {
        best := map[string]float64{start: amount}
        for iter := 0; iter < 15; iter++ {
            updated := false
            for u, vmap := range graph {
                for v, r := range vmap {
                    if best[u] > 0 {
                        newAmt := best[u] * r
                        if newAmt > best[v]+1e-12 {
                            best[v] = newAmt
                            updated = true
                        }
                    }
                }
            }
            if !updated { break }
        }
        // Final verification: ensure no further improvements possible
        for u, vmap := range graph {
            for v, r := range vmap {
                if best[u] > 0 {
                    newAmt := best[u] * r
                    if newAmt > best[v]+1e-12 {
                        // If found, additional iterations would increase value, so repeat
                        return propagate(graph, start, amount)
                    }
                }
            }
        }
        return best
    }
    g1 := buildGraph(pairs1, rates1)
    g2 := buildGraph(pairs2, rates2)
    // Day 1: get all possible currencies & max amounts
    afterDay1 := propagate(g1, initialCurrency, 1.0)
    ans := 1.0
    // For each currency after day 1, try all paths on day 2 to maximize initialCurrency
    for cur, amt := range afterDay1 {
        afterDay2 := propagate(g2, cur, amt)
        if v, ok := afterDay2[initialCurrency]; ok {
            if v > ans { ans = v }
        }
    }
    return ans
}
# @lc code=end