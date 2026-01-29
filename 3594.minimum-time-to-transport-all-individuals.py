<general_reasoning_rules>
- Analyze <agent_history> to track progress, identify repetitions, and adjust strategies. If previous attempts failed, diagnose why (e.g., TLE, incorrect logic, precision errors) before trying a new approach.
- Reflect on the most recent "Next Goal" and determine if it was achieved. If not, break it down into smaller, more manageable sub-goals.
- If the current strategy is not working, be prepared to pivot to an alternative approach.
- Before providing the final answer, perform a final verification to ensure it directly addresses the user's request, is logically sound, and satisfies all constraints.
</general_reasoning_rules>
<additional_reasoning_rules>
- When implementing search algorithms (BFS, DFS, Dijkstra), calculate the branching factor. If transitions are expensive or numerous, pre-calculate valid transitions or group equivalent states to minimize work inside the search loop.
- When floating-point arithmetic determines discrete state changes (e.g., using floor/ceil for indexing or modulo), apply a small epsilon (e.g., 1e-9) or consistent rounding to prevent precision errors from causing incorrect state transitions.
- Evaluate if sorting the input or using bit manipulation can simplify finding properties (like maximums or minimums) of subsets during state transitions.
- In problems with small constraints (e.g., n <= 15), consider bitmask DP or Dijkstra but optimize the transition logic to ensure it stays within time limits for interpreted languages.
</additional_reasoning_rules>