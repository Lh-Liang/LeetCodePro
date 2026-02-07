#
# @lc app=leetcode id=3310 lang=golang
#
# [3310] Remove Methods From Project
#

# @lc code=start
func remainingMethods(n int, k int, invocations [][]int) []int {
    // Step 1: Create adjacency list for invocations
    adj := make([][]int, n)
    for _, invocation := range invocations {
        adj[invocation[0]] = append(adj[invocation[0]], invocation[1])
    }
    
    // Step 2: Use BFS/DFS to find all reachable nodes from k (suspicious nodes)
    var dfs func(int) []bool
    dfs = func(node int) []bool {
        visited := make([]bool, n)
        var stack []int
        stack = append(stack, node)
        visited[node] = true
        for len(stack) > 0 {
            current := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            for _, neighbor := range adj[current] {
                if !visited[neighbor] {
                    visited[neighbor] = true
                    stack = append(stack, neighbor)
                }
            }
        }
        return visited 
n}
n   
suspicious := dfs(k) 
n   
inDegree := make([]int, n) 
n   
outDegree := make([][]int, n) 
n   
forsource , targets:= range adj{ 
n       for _, target := range targets { 
n           outDegree[source] = append(outDegree[source], target) 
n           inDegree[target]++ 
n       } 
n   } 
n   
successfullyIsolated := true
   
sfor i:= 0; i< n; i++{ 
successfullyIsolated = successfullyIsolated && (suspicious[i] || inDegree[i]==0)
forsuccessfullyIsolated && !suspicious[i]{
successfullyIsolated=false
break
}
s}
sif successfullyIsolated{output:=[]int{}
sfor j:=0; j<n;j++{
sif !suspicious[j]{
soutput=append(output,j)
g}
g}
greturn output
g}
greturn []int{}
g}g
# @lc code=end