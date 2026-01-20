#
# @lc app=leetcode id=3420 lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # We need to maintain a data structure that supports:
        # 1. Range Add: Add v to A[l...r]
        # 2. Query: Find smallest index i such that A[i] <= k
        
        # Segment Tree Implementation
        # Tree size: 4 * n
        # Each node stores: min_val (to quickly check condition)
        # Lazy propagation for range updates
        
        tree_min = [0] * (4 * n)
        tree_lazy = [0] * (4 * n)
        
        def push(node):
            if tree_lazy[node] != 0:
                tree_lazy[2 * node] += tree_lazy[node]
                tree_min[2 * node] += tree_lazy[node]
                tree_lazy[2 * node + 1] += tree_lazy[node]
                tree_min[2 * node + 1] += tree_lazy[node]
                tree_lazy[node] = 0
        
        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                tree_min[node] += val
                tree_lazy[node] += val
                return
            push(node)
            mid = (start + end) // 2
            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)
            tree_min[node] = min(tree_min[2 * node], tree_min[2 * node + 1])
        
        # Find the smallest index i in [0, r] such that cost[i] <= k
        # Since cost[i] is non-increasing as i increases (smaller subarray costs less),
        # we are looking for the first i where condition holds.
        # Actually, wait. 
        # Cost(l, r) is the cost to make nums[l...r] non-decreasing.
        # For a fixed r, as l increases, the subarray shrinks, so cost decreases.
        # Cost(l, r) >= Cost(l+1, r).
        # So the function is monotonically non-increasing.
        # We want to find smallest l such that Cost(l, r) <= k.
        # In the segment tree, we can search for the first leaf <= k.
        # Since the function is monotonic, the condition Cost[i] <= k will be true for a suffix [valid_l, r].
        # The tree stores costs. We want the smallest index i such that tree_min query on i is <= k.
        # Because of monotonicity, we can just walk the tree.
        # If left child's min <= k, go left? 
        # Wait, if left child's min <= k, it means there is SOME index in left child with cost <= k.
        # Since it's monotonic (values decrease as index increases), if min(left) <= k, it might be the last element of left.
        # But we want the *smallest* index. 
        # If Cost is decreasing, then Cost[0] >= Cost[1] >= ... >= Cost[r].
        # We want smallest l such that Cost[l] <= k.
        # This means we want the first l where the value drops below or equal to k.
        # If tree_min[node] > k, then no index in this range works.
        # If tree_min[node] <= k, we try left. If that fails (all > k), we try right.
        
        def query_first_valid(node, start, end, limit):
            if tree_min[node] > limit:
                return -1
            if start == end:
                return start
            push(node)
            mid = (start + end) // 2
            # Try left child
            res = query_first_valid(2 * node, start, mid, limit)
            if res != -1:
                return res
            return query_first_valid(2 * node + 1, mid + 1, end, limit)

        # Stack to maintain max segments
        # Stores tuples (index, val). 
        # Actually we just need indices because values are in nums.
        # However, to be precise with ranges, let's store indices.
        # stack[i] is index. nums[stack[i]] is the max for range (stack[i-1], stack[i]].
        # We will use a slightly different approach for updates to avoid O(N) updates.
        # Notice: Cost(l, r) = Cost(l, r-1) + max(nums[l...r]) - nums[r].
        # We always subtract nums[r] from [0, r].
        # We add max(nums[l...r]).
        # The 'max' term is constant on intervals defined by the stack.
        # When we push r, we pop elements <= nums[r].
        # For a popped element at `top`, valid for range `(stack[top-1], stack[top]]`,
        # the max was `nums[stack[top]]`. Now it becomes `nums[r]`.
        # So the delta is `nums[r] - nums[stack[top]]`.
        # We apply this delta to the range `(stack[top-1], stack[top]]`.
        # The element `r` itself forms a new range `(stack[-1], r]` with max `nums[r]`.
        # But wait, the base recurrence is `Cost += ...`.
        # The previous `Cost` already included sums of previous maxes.
        # We are updating the `Cost` accumulation.
        # Let's trace:
        # At step `r`, we want `Cost[l]` to increase by `max(nums[l...r]) - nums[r]`.
        # 1. Update all `[0, r]` by `-nums[r]`.
        # 2. Update `[0, r]` by adding `max(nums[l...r])`.
        #    This is hard because we add different values to different ranges.
        #    BUT, we can maintain the accumulated cost differently.
        #    Let's track `AccumulatedMax[l]` and `AccumulatedNums[l]`.
        #    `Cost[l] = AccumulatedMax[l] - AccumulatedNums[l]`.
        #    `AccumulatedNums[l]` increases by `nums[r]` at step `r`. So we subtract `nums[r]` from Cost.
        #    `AccumulatedMax[l]` increases by `max(nums[l...r])`.
        #    Instead of adding the full `max` value every step, observe:
        #    `max(nums[l...r])` is the same as `max(nums[l...r-1])` EXCEPT when `nums[r]` is the new max.
        #    If `nums[r]` is new max for `l`, then `max` increases by `nums[r] - old_max`.
        #    If `nums[r]` is NOT new max, `max` stays same.
        #    So, we maintain a `CurrentMaxSum[l]` in the tree? No, we maintain `TotalCost`.
        #    Let's re-verify the delta.
        #    Let `M(l, r) = max(nums[l...r])`.
        #    `Cost(l, r) = ∑_{j=l}^r (M(l, j) - nums[j])`
        #    `Cost(l, r) = Cost(l, r-1) + M(l, r) - nums[r]`.
        #    We maintain `Cost` in the tree.
        #    1. Range add `-nums[r]` to `[0, r]`.
        #    2. Range add `M(l, r)` to `[0, r]`.
        #       This `M(l, r)` part is the problem. We can't do O(N) adds.
        #       Wait! We can use the stack to manage the `M(l, r)` addition efficiently?
        #       Not directly. `M(l, r)` is the value we add *this step*.
        #       But notice `M(l, r)` is piecewise constant.
        #       Actually, there is a trick. 
        #       We can maintain `CurrentMax[l]` implicitly? No.
        #       
        #       Let's look at the contribution of `nums[x]` as a maximum.
        #       `nums[x]` is the maximum for `nums[l...j]` if `l <= x <= j` and `nums[x]` is max in that range.
        #       This is getting complicated. Let's stick to the lazy propagation on Cost.
        #       We need to add `M(l, r)` to `Cost[l]` for all `l`.
        #       Is there a way to do this without adding the full value?
        #       No, `Cost` grows by roughly `O(value)` each step.
        #       
        #       Let's use the transformation: 
        #       We handle `M(l, r)` updates lazily? No.
        #       Let's look at the stack logic again.
        #       When we are at `r`, we have stack `st`.
        #       For `l` in `(st[j-1], st[j]]`, `M(l, r) = nums[st[j]]`.
        #       So we need to add `nums[st[j]]` to range `(st[j-1], st[j]]`.
        #       This requires iterating the stack. Stack depth can be N. Too slow.
        #       
        #       Is there a relationship between `M(l, r)` and `M(l, r-1)`?
        #       `M(l, r) = max(M(l, r-1), nums[r])`.
        #       So `Cost(l, r) = Cost(l, r-1) + max(M(l, r-1), nums[r]) - nums[r]`.
        #       If `nums[r] <= M(l, r-1)`, then `max(...)` is `M(l, r-1)`. We add `M(l, r-1) - nums[r]`.
        #       If `nums[r] > M(l, r-1)`, then `max(...)` is `nums[r]`. We add `nums[r] - nums[r] = 0`.
        #       THIS IS THE KEY!
        #       If `nums[r]` is the new maximum for range `l`, the cost added *at this step* is 0.
        #       If `nums[r]` is NOT the new maximum (i.e., `M(l, r-1) > nums[r]`), we add `M(l, r-1) - nums[r]`.
        #       
        #       So, for which `l` is `M(l, r-1) > nums[r]`?
        #       These are exactly the `l` such that the max of `nums[l...r-1]` is larger than `nums[r]`.
        #       In terms of the stack *before* processing `nums[r]`, the stack elements `st[j]` represent the maxes.
        #       `st` stores indices where `nums[st[0]] > nums[st[1]] > ...`.
        #       We pop elements from stack which are `<= nums[r]`.
        #       The elements remaining in the stack are strictly `> nums[r]`.
        #       For any `l` covered by the remaining stack elements, `M(l, r-1) > nums[r]`.
        #       For `l` covered by popped elements (and the new `r` itself), `M(l, r-1) <= nums[r]`, so `M(l, r) = nums[r]`, so we add 0.
        #       
        #       So we only need to update the ranges covered by the *remaining* stack elements.
        #       Wait, iterating remaining stack is also slow.
        #       But `M(l, r-1)` is constant on the intervals of the stack.
        #       Can we maintain a "lazy add" on the stack structure?
        #       Actually, we can maintain the quantity `M(l, r-1)` in the segment tree? No.
        #       We are adding `M(l, r-1) - nums[r]` to `Cost[l]` where `M > nums[r]`.
        #       This is equivalent to: Add `M(l, r-1)` to `Cost[l]`, then subtract `nums[r]`.
        #       But for `l` where `M <= nums[r]`, we add `0`.
        #       
        #       Let's rephrase:
        #       For `l` where `nums[r]` is the new max: Add 0.
        #       For `l` where `nums[r]` is NOT the new max: Add `M(l, r-1) - nums[r]`.
        #       
        #       The ranges where `nums[r]` is NOT the new max are `[0, last_remaining_index_in_stack]`.
        #       The ranges where `nums[r]` IS the new max are `(last_remaining_index, r]`.
        #       Let `split = st[-1]` (the top of stack after popping elements <= nums[r]).
        #       The range `[0, split]` has `M(l, r-1) > nums[r]`. We add `M(l, r-1) - nums[r]`.
        #       The range `(split, r]` has `M(l, r-1) <= nums[r]`. We add 0.
        #       
        #       So we need to add `M(l, r-1)` to `Cost[l]` for `l ∈ [0, split]`, and subtract `nums[r]` from `Cost[l]` for `l ∈ [0, split]`.
        #       The second part is easy: Range Add `-nums[r]` on `[0, split]`.
        #       The first part: Add `M(l, r-1)` on `[0, split]`. 
        #       Note that `M(l, r-1)` varies with `l`. It is piecewise constant based on the stack.
        #       However, notice `M(l, r-1)` is the value associated with the stack intervals.
        #       We can perform this addition efficiently if we maintain a "Coefficient" tag in the segment tree?
        #       Or maybe we can just track `SumM` separately?
        #       
        #       Alternative View:
        #       Total Cost `C_r[l] = C_{r-1}[l] + (M(l, r-1) > nums[r] ? M(l, r-1) - nums[r] : 0)`.
        #       Let's track `C[l]`.
        #       We need to add `M(l, r-1)` to `[0, split]`.
        #       The values `M(l, r-1)` are `nums[st[0]]` on `(0, st[0]]`? No, `(0, st[0]]` is not right.
        #       Ranges are `(st[j-1], st[j]]`.
        #       
        #       This looks like we need to add a history of values. 
        #       Let's look at constraints. K is large, N is 10^5. 
        #       Maybe we can just maintain the "active" adders.
        #       Let `lazy_count[l]` be the number of times `nums[idx]` contributes to the cost.
        #       When an element `val` is in the stack covering `[L, R]`, it contributes `val` to the cost of `l ∈ [L, R]` at every step `r` until it's popped.
        #       So, for each step `r` where `nums[idx]` remains the max for `l`, we add `nums[idx] - nums[r]`.
        #       Let's decompose: 
        #       We add `nums[idx]` for every step `r` it stays in stack.
        #       We subtract `nums[r]` for every `l` it dominates? No, we subtract `nums[r]` only if `nums[idx] > nums[r]`.
        #       
        #       Let's maintain the cost using a lazy segment tree with a special "add coefficient" op.
        #       Each node tracks `val` (current cost). Also `coeff` (sum of maxes active on this range).
        #       When moving `r -> r+1`:
        #       1. Pop elements from stack <= nums[r].
        #          For the ranges covered by popped elements, their "active max" was some `v <= nums[r]`. 
          # Now, for these ranges, the new max is `nums[r]`. But wait, for the *next* step, will they contribute?
          # In the recurrence `C_new = C_old + (M > x ? M - x : 0)`, if `M <= x`, we add 0.
          # So for ranges where `M <= nums[r]`, we stop adding anything.
          # Meaning their `coeff` becomes 0.
          # For ranges where `M > nums[r]` (the surviving stack), they continue to add `M - nums[r]`.
          # So `coeff` stays `M`. We just need to subtract `nums[r]` at each step.
        #       
        #       Algorithm Refined:
        #       SegTree maintains `Cost[l]`.
        #       Also maintains `Coeff[l]`: the value `M(l, current_r)` that should be added to `Cost` at each step, IF `M > next_x`.
        #       Actually, simpler:
        #       At step `r`:
        #       1. Identify `split` point (index of top of stack after popping <= nums[r]).
        #          Range `[0, split]` are indices where `M(l, r-1) > nums[r]`.
        #          Range `(split, r]` are indices where `M(l, r-1) <= nums[r]`.
        #       2. For `l ∈ [0, split]`: We add `M(l, r-1) - nums[r]`.
        #          Note `M(l, r-1)` is `Coeff[l]` stored in the tree.
        #          So we do: `Range Add Cost` on `[0, split]` by `-nums[r]`.
        #          AND `Range Add Cost` on `[0, split]` by `Coeff[l]`? No, we can't range add a variable coeff.
        #          BUT `Coeff` is static for `[0, split]` during this step? No, `Coeff` varies.
        #          However, `Coeff` doesn't change for the surviving stack part! 
        #          We can maintain `Cost` and update it lazily using `Coeff`.
        #          Wait, we can perform `Cost += Coeff * count`? 
        #          No, we just adding once per step. 
        #          We can treat `Coeff` as a value we added `count` times.
        #          Let's just track `Cost`. 
        #          We need to add `Coeff` to `Cost` on `[0, split]`.
        #          Since `Coeff` is piecewise constant, and the stack segments are the pieces.
        #          We can update the segments corresponding to the stack.
        #          BUT we can't iterate the stack.
        #          
        #          Wait. `Coeff` *is* stored in the tree? 
        #          We can use a Segment Tree that supports:
        #          - `Range Add Cost`
        #          - `Range Set Coeff`
        #          - `Range Add Cost using Coeff` (Cost += Coeff)
        #          
        #          Operations at step `r`:
        #          1. Pop stack. For each popped range `(L, R]`, we were having `Coeff = old_val`. 
        #             Now `M` becomes `nums[r]`. But we don't add `nums[r]` to cost. We add 0.
        #             So we set `Coeff` to 0 for `(split, r]`? 
        #             Wait, for the *next* step `r+1`, `M(l, r)` will be `nums[r]`. 
        #             If `nums[r] > nums[r+1]`, we will add `nums[r] - nums[r+1]`.
        #             So the `Coeff` for `(split, r]` becomes `nums[r]`.
        #             
        #          Correct Logic:
        #          Let `Coeff[l]` be `M(l, r)`. 
        #          At end of step `r`, for `l ∈ (split, r]`, `M(l, r)` becomes `nums[r]`. 
        #          So we `Range Set Coeff` to `nums[r]` on `(split, r]`. 
        #          The range `[0, split]` keeps its old `Coeff`.
        #          
        #          Now, applying the cost update for step `r+1` (value `x = nums[r+1]`):
        #          We need to add `max(0, Coeff[l] - x)` to `Cost[l]`.
        #          This is `Coeff[l] - x` for `l` where `Coeff[l] > x`.
        #          `Coeff[l] > x` corresponds to `[0, new_split]`.
        #          So on `[0, new_split]`, we add `Coeff[l]` and subtract `x`.
        #          
        #          So we need a SegTree supporting:
        #          1. `Range Add Cost` with constant val (for the `-x` part).
        #          2. `Range Add Cost` with `Coeff` (Cost += Coeff).
        #          3. `Range Set Coeff`.
        #          
        #          This is solvable with Lazy Propagation.
        #          Tags: 
        #          - `add_val`: value to add to Cost.
        #          - `add_coeff_count`: number of times we added Coeff to Cost.
        #          - `set_coeff`: value to set Coeff to (with timestamp or priority).
        #          
        #          Actually, `set_coeff` always happens on a suffix `(split, r]`. 
        #          And `add_coeff` always happens on a prefix `[0, split]`.
        #          The ranges are nice. 
        #          But `add_coeff` on `[0, split]` overlaps with `set_coeff` ranges arbitrarily? 
        #          No. `[0, split]` is always a union of existing Coeff segments.
        #          The `Coeff` is constant on stack segments.
        #          
        #          Let's implement the SegTree nodes:
        #          `min_cost`: minimum cost in range.
        #          `lazy_add`: value to add to cost.
        #          `lazy_coeff_add`: number of times Coeff has been added to cost.
        #          `coeff`: The current M value for this range (if constant). If not constant, use -1 or push down.
        #          Actually, `coeff` is set on ranges. We can just use a `lazy_set_coeff`.
        #          However, we need `sum_coeff`? No, we need `min_cost`. 
        #          We need to calculate `min_cost` after `cost += k * coeff`.
        #          This implies we need to know `min(cost + k * coeff)`.
        #          This is hard if `cost` and `coeff` vary independently.
        #          BUT `cost` is only updated by `cost += coeff - x`.
        #          And `coeff` is set to `v`.
        #          
        #          Actually, we can observe that `Cost` function is monotonic. `Cost[0] >= Cost[1] >= ...`
        #          We only query `min_cost` to find the first valid `l`.
        #          Since it is sorted, `min_cost` of a range is just `Cost[right_end]`. 
        #          Wait, `Cost` is decreasing with `l`? 
        #          `l` increases -> subarray shrinks -> Cost decreases.
        #          So `Cost[0]` is max, `Cost[r]` is 0.
        #          We want smallest `l` such that `Cost[l] <= k`.
        #          Since `Cost` is monotonic decreasing, we can use binary search on `l` from `0` to `r`.
        #          We just need Point Query for `Cost[l]`! 
        #          We don't need min query on range. We can just point query.
        #          Can we do Point Query efficiently?
        #          We have updates on ranges.
        #          1. `Range Add Cost` on `[0, split]` by `-nums[r]`.
        #          2. `Range Add Cost` on `[0, split]` by `Coeff`.
        #          3. `Range Set Coeff` on `(split, r]` to `nums[r]`.
        #          
        #          Since we only need Point Query, can we optimize?
        #          We can use a Fenwick tree? No, `Add Coeff` depends on `Coeff` which varies.
        #          But `Coeff` is constant on stack intervals.
        #          We can maintain `Cost` in a segment tree.
        #          The operations are:
        #          - `Add(0, split, -nums[r])`
        #          - `AddCoeff(0, split)` -> `Cost[l] += Coeff[l]`.
        #          - `SetCoeff(split+1, r, nums[r])`.
        #          
        #          We can implement a Segment Tree with `lazy_add`, `lazy_coeff_add`, `lazy_set_coeff`.
        #          Node stores: `val` (cost at this point? No, we need range). 
        #          Actually, if we only need point query, we can just push down everything.
        #          But we need to binary search `l`. So we need `O((log N)^2)` or `O(log N)`.
        #          Since the function is monotonic, binary search + point query is `O(log^2 N)`.
        #          Point query takes `O(log N)`. Binary search takes `O(log N)` steps. Total `O(log^2 N)`. Acceptable.
        #          
        #          Implementation details of SegTree for Point Query:
        #          We need to handle the composition of tags.
        #          State at leaf `l`: `Cost[l]`, `Coeff[l]`.
        #          Tags on node: 
        #          - `add_cost`: `c -> c + v`
        #          - `add_coeff_times`: `c -> c + times * coeff`
        #          - `set_coeff`: `coeff -> new_val`. 
        #             Note: when we set coeff, the old coeff is gone. BUT any pending `add_coeff_times` must be applied using the OLD coeff before setting new one.
        #             So order matters. `add_coeff` happens before `set_coeff` in our logic? 
        #             Logic: 
        #             1. `Add Cost` on `[0, split]`. (Modify cost)
        #             2. `Add Coeff` on `[0, split]`. (Modify cost based on CURRENT coeff)
        #             3. `Set Coeff` on `(split, r]`. (Modify coeff for FUTURE)
        #          
        #          Composition:
        #          Node has `lazy_add_cost`, `lazy_add_coeff_k`, `lazy_set_coeff_val`.
        #          `lazy_set_coeff_val` overrides existing coeff. 
        #          If we have `set_coeff` pending, and we get `add_coeff_k`:
        #             The `add_coeff` uses the *pending* set value. 
        #             So `lazy_add_cost += k * lazy_set_coeff_val`.
        #             `lazy_add_coeff_k` (on the *underlying* coeff) remains unchanged.
        #          If we don't have `set_coeff` pending:
        #             `lazy_add_coeff_k += k`.
        #          
        #          If we have `set_coeff` pending, and we get `set_coeff` (new):
        #             `lazy_set_coeff_val` updates. `lazy_set_coeff` exists flag true.
        #          
        #          If we get `add_cost`:
        #             `lazy_add_cost += val`.
        #          
        #          Push Down:
        #          Apply `lazy_add_coeff_k` to children using their current `Coeff` (or children's set_coeff? No, push down propagates tags).
        #          Order of application on a child:
        #          1. Apply `parent.lazy_add_coeff_k`: 
        #             Child `lazy_add_cost += parent.lazy_add_coeff_k * Child.current_coeff`? 
        #             Wait, if Child has a pending `set_coeff`, we use that. 
        #             If Child represents a leaf, we just do `cost += k * coeff`.
        #             If Child is internal node, we update its tags.
        #             We need to know the `coeff` of the child node to apply `add_coeff_k`. 
        #             But `coeff` might not be uniform in child range. 
        #             However, `set_coeff` makes it uniform! 
        #             And `add_coeff` is only applied to `[0, split]`. `set_coeff` is applied to `(split, r]`. 
        #             Wait. `add_coeff` is on `[0, split]`. `set_coeff` is on `(split, r]`. 
        #             These ranges are disjoint? No. `[0, split]` is the prefix. `(split, r]` is the suffix.
        #             The `set_coeff` range `(split, r]` had `Coeff` values before? Yes.
        #             But we are setting them now. 
        #             The `add_coeff` is on `[0, split]`. These nodes do NOT get `set_coeff` in this step.
        #             So we never have `add_coeff` and `set_coeff` overlapping in the same update step.
        #             BUT, over time, a node might have `set_coeff` from past, and now gets `add_coeff`.
        #             Yes. Since `set_coeff` makes a range uniform, we can track `is_uniform` and `uniform_val`?
        #             Actually, `Coeff` is always set by `Range Set`. So it is a standard Color Update problem.
        #             `Coeff` is uniform on sub-segments. 
        #             If a node has uniform `Coeff`, we can apply `add_coeff_k` easily: `lazy_add_cost += k * uniform_coeff`.
        #             If not uniform, we must push down.
        #             Since `set_coeff` corresponds to stack operations, the number of uniform segments is $O(N)$. 
        #             Amortized complexity suggests this is efficient.
        #             We maintain `min_coeff` and `max_coeff` in node. If `min == max`, it's uniform.
        #             
        #          Structure:
        #          Node: 
        #            `cost` (not needed for internal, only leaves? No, need to push down)
        #            `coeff_min`, `coeff_max`, `lazy_set_coeff` (value, exists)
        #            `lazy_add_cost`, `lazy_add_coeff_k`
        #          
        #          Update `add_coeff` on `[L, R]`: 
        #             If `coeff_min == coeff_max`: 
        #                 `lazy_add_cost += k * coeff_min`
        #                 `lazy_add_coeff_k` NOT incremented (we converted it to cost add).
        #                 return
        #             Else:
        #                 Push Down
        #                 Recurse
        #          
        #          Update `set_coeff` on `[L, R]`:
        #             `coeff_min` = `coeff_max` = val
        #             `lazy_set_coeff` = val
        #             `lazy_add_coeff_k` = 0 (since we are overwriting coeff, any past add_coeff was already processed or pushed)
        #             Wait, `lazy_add_coeff_k` accumulates additions based on OLD coeffs.
        #             If we overwrite coeff, we must ensure OLD `add_coeff` ops are done.
        #             So we must `Push Down` before `set_coeff` if there are pending ops? 
        #             Yes.
        #          
        #          Update `add_cost`:
        #             Just update `lazy_add_cost`.
        #          
        #          This works. Complexity: Since `set_coeff` corresponds to erasing stack items, and each item is added once and erased once, the number of uniform segments created/destroyed is linear. 
        #          This is the "Segment Tree Beats" or "Color Segment Tree" complexity analysis. $O(N \log N)$.
        
        st = [] # Monotonic stack of indices. nums[st[i]] > nums[st[i+1]]
        # Actually, let's use the standard definition: st stores indices with decreasing values.
        # st[0] is index of largest.
        
        # SegTree Arrays
        # Size 4*N
        # We need `cost` at leaves. But for binary search we need point query.
        # Let's just implement `query(index)`.
        
        self.tree_lazy_cost = [0] * (4 * n)
        self.tree_lazy_coeff_k = [0] * (4 * n)
        self.tree_set_coeff = [-1] * (4 * n) # -1 means no set pending
        self.tree_coeff_min = [0] * (4 * n)
        self.tree_coeff_max = [0] * (4 * n)
        
        # Initialize coeffs to 0? Or nums[i]? 
        # Initially subarray is single element, cost 0. Coeff is nums[i].
        # We iterate r. Start with empty. 
        # r=0: 
        #   split = -1. 
        #   add_coeff on [0, -1] -> nothing.
        #   set_coeff on [0, 0] to nums[0].
        #   add_cost on [0, 0] by -nums[0]. 
        #   Wait, initial cost is 0. 
        #   Recurrence: Cost(l, r) = Cost(l, r-1) + max(...) - nums[r].
        #   For r=0, Cost(0, 0) = 0 + nums[0] - nums[0] = 0.
        #   So updates work.

        # Helper to push down
        def push(node, l, r):
            mid = (l + r) // 2
            left = 2 * node
            right = 2 * node + 1
            
            # 1. Apply set_coeff if exists
            if self.tree_set_coeff[node] != -1:
                val = self.tree_set_coeff[node]
                # Push to children
                # If we set coeff, we resolve any pending coeff_k adds on children first? 
                # No, the set_coeff happened AFTER any accumulated coeff_k adds on this node.
                # But the children might have their own pending coeff_k adds.
                # Those must be applied using OLD coeffs before we overwrite.
                # So we push children first? No, standard lazy is: apply my tag to children.
                # The tag `set_coeff` overrides everything.
                # BUT `lazy_coeff_k` and `set_coeff` order matters.
                # We maintain invariant: `lazy_coeff_k` is applied, THEN `set_coeff`.
                # Wait, if we have both, it means we added K times then set.
                # So we should apply K times to children, then set.
                pass
            
            # Let's refine the push logic.
            # We have `add_cost`, `add_coeff_k`, `set_coeff`.
            # Order: `add_cost` (independent), `add_coeff_k` (uses OLD coeff), `set_coeff` (sets NEW coeff).
            
            # Apply `add_cost`
            if self.tree_lazy_cost[node] != 0:
                v = self.tree_lazy_cost[node]
                self.tree_lazy_cost[left] += v
                self.tree_lazy_cost[right] += v
                self.tree_lazy_cost[node] = 0
            
            # Apply `add_coeff_k`
            k = self.tree_lazy_coeff_k[node]
            if k != 0:
                # Left child
                if self.tree_coeff_min[left] == self.tree_coeff_max[left]:
                    self.tree_lazy_cost[left] += k * self.tree_coeff_min[left]
                else:
                    self.tree_lazy_coeff_k[left] += k
                
                # Right child
                if self.tree_coeff_min[right] == self.tree_coeff_max[right]:
                    self.tree_lazy_cost[right] += k * self.tree_coeff_min[right]
                else:
                    self.tree_lazy_coeff_k[right] += k
                
                self.tree_lazy_coeff_k[node] = 0
            
            # Apply `set_coeff`
            v = self.tree_set_coeff[node]
            if v != -1:
                self.tree_set_coeff[left] = v
                self.tree_coeff_min[left] = self.tree_coeff_max[left] = v
                self.tree_lazy_coeff_k[left] = 0 # Any old K adds are invalid/superseded? No, they are processed above.
                # Wait, if we set coeff, future K adds use new coeff. Old K adds used old coeff.
                # We processed old K adds above. So we reset K to 0 for children? 
                # If child had pending K adds, they should have been applied to its descendants using ITS old coeff.
                # But we are overwriting its coeff. 
                # If we overwrite child's coeff, we MUST ensure child's pending K adds are pushed to ITS children first.
                # This implies we need to push children of `node` before applying `set_coeff` to them?
                # That would be recursive push, O(N). Bad.
                # 
                # Let's use the property: `set_coeff` only happens on `(split, r]`. 
                # These ranges are exactly where we Popped from stack.
                # When we pop, we are conceptually "finalizing" the segment.
                # Actually, simpler: 
                # If `set_coeff` comes, it means the structure changed. 
                # But `lazy_coeff_k` is only generated on `[0, split]`. 
                # `set_coeff` is on `(split, r]`. 
                # They are disjoint in the current update.
                # So a node receiving `set_coeff` will NOT receive `add_coeff_k` in the same batch.
                # But it might represent a range that had pending `add_coeff_k` from previous steps?
                # Yes.
                # If a node has pending `add_coeff_k`, and we `set_coeff` on it:
                # We must apply the `add_coeff_k` first.
                # But we can't apply it if not uniform.
                # However, `set_coeff` is applied to ranges that correspond to stack pops.
                # Stack pops align with the uniform segments! 
                # The range `(split, r]` is a union of previously uniform segments (the stack intervals).
                # So for any node fully inside `(split, r]`, if it was a stack interval, it IS uniform.
                # So we can apply `add_coeff_k` efficiently.
                pass
                
                self.tree_set_coeff[right] = v
                self.tree_coeff_min[right] = self.tree_coeff_max[right] = v
                self.tree_lazy_coeff_k[right] = 0
                
                self.tree_set_coeff[node] = -1

        def update_add_cost(node, start, end, l, r, val):
            if l > end or r < start: return
            if l <= start and end <= r:
                self.tree_lazy_cost[node] += val
                return
            push(node, start, end)
            mid = (start + end) // 2
            update_add_cost(2*node, start, mid, l, r, val)
            update_add_cost(2*node+1, mid+1, end, l, r, val)
            # No pull needed for point query structure
        
        def update_add_coeff(node, start, end, l, r):
            if l > end or r < start: return
            if l <= start and end <= r:
                if self.tree_coeff_min[node] == self.tree_coeff_max[node]:
                    self.tree_lazy_cost[node] += self.tree_coeff_min[node]
                else:
                    self.tree_lazy_coeff_k[node] += 1
                return
            push(node, start, end)
            mid = (start + end) // 2
            update_add_coeff(2*node, start, mid, l, r)
            update_add_coeff(2*node+1, mid+1, end, l, r)
            
        def update_set_coeff(node, start, end, l, r, val):
            if l > end or r < start: return
            if l <= start and end <= r:
                # Before setting, apply any pending k adds? 
                # If this node has pending k adds, and is not uniform, we have a problem.
                # But due to stack structure, any node fully covered by set_coeff (which is a union of stack intervals)
                # should be uniform OR composed of uniform children.
                # Actually, if we just push before setting, it's safe.
                # But we can't push to leaves (O(N)).
                # We rely on the fact that `set_coeff` aligns with uniformity.
                # If not uniform, we must push.
                if self.tree_coeff_min[node] == self.tree_coeff_max[node]:
                     # Apply pending k
                    if self.tree_lazy_coeff_k[node] > 0:
                         self.tree_lazy_cost[node] += self.tree_lazy_coeff_k[node] * self.tree_coeff_min[node]
                         self.tree_lazy_coeff_k[node] = 0
                    
                    self.tree_set_coeff[node] = val
                    self.tree_coeff_min[node] = self.tree_coeff_max[node] = val
                    return
                
                # If not uniform, push down and recurse
                push(node, start, end)
                # After push, children might be uniform. 
                # Actually, we can just recurse.
                pass
            
            # If partial overlap, must push
            push(node, start, end)
            mid = (start + end) // 2
            update_set_coeff(2*node, start, mid, l, r, val)
            update_set_coeff(2*node+1, mid+1, end, l, r, val)
            self.tree_coeff_min[node] = min(self.tree_coeff_min[2*node], self.tree_coeff_min[2*node+1])
            self.tree_coeff_max[node] = max(self.tree_coeff_max[2*node], self.tree_coeff_max[2*node+1])

        def query_cost(node, start, end, idx):
            if start == end:
                return self.tree_lazy_cost[node]
            push(node, start, end)
            mid = (start + end) // 2
            if idx <= mid:
                return query_cost(2*node, start, mid, idx)
            else:
                return query_cost(2*node+1, mid+1, end, idx)

        total_subarrays = 0
        stack = [] # Stores indices
        
        for r in range(n):
            val = nums[r]
            
            # 1. Pop stack
            while stack and nums[stack[-1]] <= val:
                stack.pop()
            
            split = stack[-1] if stack else -1
            
            # 2. Add Cost: -val on [0, r]
            update_add_cost(1, 0, n-1, 0, r, -val)
            
            # 3. Add Coeff on [0, split]
            if split >= 0:
                update_add_coeff(1, 0, n-1, 0, split)
                
            # 4. Set Coeff on (split, r] to val
            # Indices split+1 to r
            update_set_coeff(1, 0, n-1, split+1, r, val)
            
            # 5. Binary Search for smallest l
            # We want smallest l in [0, r] such that Cost[l] <= k
            # Cost is monotonic decreasing. 
            # Cost[0] >= Cost[1] >= ... >= Cost[r] = 0.
            # We want first l with Cost[l] <= k.
            
            # Binary search range [0, r]
            low, high = 0, r
            ans = r + 1
            while low <= high:
                mid = (low + high) // 2
                c = query_cost(1, 0, n-1, mid)
                if c <= k:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            # Valid l are [ans, r]. Count is r - ans + 1.
            total_subarrays += (r - ans + 1)
            
            stack.append(r)
            
        return total_subarrays
```