# LeetCode Patterns — recognition + practice tracker

A pattern-first pass before the DP deep-dive, following AlgoMaster's
[15 LeetCode Patterns](https://blog.algomaster.io/p/15-leetcode-patterns). The thesis (patterns > raw volume)
matches how the data-structure walk (`data-structures.md` §1–16) was run.

**Approach:** learn each pattern in order, then solve its problems — **skip any already done in Python**, write the rest.
Fill the per-pattern **Notes** (recognition cue → template → gotchas) as you go, the same solve-plus-notes rhythm as the
data-structure walk.

**Legend:** ✅ done in Python · ⬜ to do · 🟦 *pattern already owned from prior work — these specific problems are quick reps*

**Progress: 28 / 48 done.** Recommended order (easy→hard, backtracking last as the bridge into DP):
**1 Prefix Sum → 2 Two Pointers → 3 Sliding Window → 6 Monotonic Stack → 7 Top-K → 8 Intervals → 9 Modified Binary Search → 5 LinkedList Reversal → 4 Fast/Slow → 10–13 Tree/DFS/BFS/Matrix (quick) → 14 Backtracking → 15 DP.**

---

## 1. Prefix Sum
*Recognize:* many range-sum queries, or "count subarrays whose sum = K." Precompute cumulative sums; range = `P[j] - P[i-1]`. For "subarray sum = K / equal 0s and 1s," pair a running sum with a hash map of seen sums.
- [x] ✅ **303** Range Sum Query - Immutable
- [x] ✅ **525** Contiguous Array
- [x] ✅ **560** Subarray Sum Equals K

**Notes:** Two forms.
- **(a) Static array** — precompute cumulative sums with a **sentinel** (`prefix[0]=0`, length n+1); range `(l..r) = prefix[r+1] - prefix[l]`. `itertools.accumulate(nums, initial=0)` is the idiomatic builder; the sentinel kills the `l==0` special case (303).
- **(b) Running sum + hash map** — sweep a running sum `s`; the pivot is **`subarray (i..j) sum = k ⟺ prefix[i] = s - k`**, so look up `s - k` in a map of prefixes seen so far. *Payload depends on the question:* `sum → count` when **counting** subarrays (560: `count += seen[s-k]`, then `seen[s] += 1`; seed `{0:1}`); `sum → first index` when finding the **longest** (525: store first occurrence only, `len = i - first[s]`; seed `{0:-1}`; transform `0→-1` so "equal 0s/1s" becomes "sum 0").
- **Gotchas:** seed the base-case key or you miss subarrays starting at index 0; **never reset/decrement a seen-count** — repeats are *distinct* subarrays, not double-counts (the `seen[target]=0` under-counting bug); for "longest," store **first** occurrence only (don't overwrite).
- **Not DP** — it's complement-lookup (Two Sum over running sums), no choice/optimization. Prefix sums are a *tool* DP uses, not a DP pattern.

---

## 2. Two Pointers
*Recognize:* sorted array, find a pair/triple meeting a condition; or partition in place. Pointers from both ends, move based on comparison.
- [x] ✅ **167** Two Sum II - Input Array Is Sorted
- [x] ✅ **15** 3Sum
- [x] ✅ **11** Container With Most Water

**Notes:** Sorted array, pointers at both ends, move inward by comparison — sortedness lets each step discard a whole set of candidates in O(1). Three flavors:
- **Converge to a target (167):** `l=0, r=n-1`; `sum < target → l += 1`, `sum > target → r -= 1`. (1-indexed return here.)
- **Fix one + converge + dedup (15, 3Sum):** sort; for each `i`, two-pointer `(i+1, n-1)` for pairs summing to `-nums[i]`. **Decouple progress from dedup** — `elif/else` are *pure single moves* (`l += 1`/`r -= 1`); dedup is a *separate additive step* that fires **only** after a match (skip equal `l`/`r`) and at the outer `i` (`if i>0 and nums[i]==nums[i-1]: continue`). Use `for i in range(...)`, **not** `while` — `continue` in a `while` skips the bottom `i += 1` → infinite loop. Optional prune: `if nums[i] > 0: break`.
- **Greedy, move the limiter (11, Container):** maximize `min(h[l], h[r])·(r-l)`; move the pointer at the **shorter** line. *Why safe:* the shorter line caps the height, and its widest partner is the current opposite end, so `(l,r)` is the best container it can ever be in — record it, then discard it. Moving the *taller* could skip the optimum (its potential isn't exhausted). On a tie, either side is safe.
- **Gotchas:** every branch must **advance a pointer** (guarantees termination); dedup is never a substitute for the move; `while`-loop `continue` trap.

---

## 3. Sliding Window
*Recognize:* longest/shortest/contains subarray or substring meeting a constraint. Grow the right edge; shrink the left when the window violates the constraint. (Distinct from the window-**DP** of 1696.)
- [x] ✅ **643** Maximum Average Subarray I
- [x] ✅ **3** Longest Substring Without Repeating Characters
- [x] ✅ **76** Minimum Window Substring

**Notes:** Keep a window `[left, right]` and update an **incremental aggregate** (sum, char-count map) as it moves — never recompute. Two shapes:
- **Fixed-size (643):** window of exactly `k`. Seed the first window, then slide: `window_sum += nums[right] - nums[left]`. O(n·k) → O(n).
- **Variable, maximize (3):** expand `right`; when a constraint breaks (a repeat), shrink `left` to restore it; record max *while valid*. Index-jump variant: map `char → last index`, `left = max(left, last[c] + 1)` (the `max` stops `left` rewinding past an earlier duplicate).
- **Variable, minimize with coverage (76):** expand until the window **covers** `t`, then shrink *while still covering*, recording the min. `need = Counter(t)` (multiplicity!), `required = len(need)`, `formed` counter; `formed += 1` only when `have[c] == need[c]` (cross **up**, `==`), `formed -= 1` only when `have[c] < need[c]` (cross **down**, `<`). `formed == required` is the O(1) validity check.
- **The inversion:** longest-valid (3) shrinks to *escape* invalidity; shortest-covering (76) shrinks *while still valid* to tighten. Same `left`-shrink, opposite trigger.
- **Gotchas:** 643 seed the first window then slide; 3 `max(left, last+1)` so `left` never rewinds; 76 use `Counter` not a set (dups in `t`), and update `formed` on **both** add and remove with `==`/`<` (not `>=`/`<=`).

---

## 4. Fast & Slow Pointers 🟦
*Recognize:* cycle detection / find a meeting point in a linked list or implicit functional graph. Slow +1, fast +2; they meet iff a cycle exists.
- [x] ✅ **141** Linked List Cycle — *done (set + Floyd's)*
- [x] ✅ **202** Happy Number
- [x] ✅ **287** Find the Duplicate Number

**Notes:** Tortoise (+1) and hare (+2); if there's a cycle, the hare laps the tortoise and they meet inside it. **The big leap: the "linked list" can be implicit** — any `next = f(current)` defines one.
- **141** — literal list, `next = node.next`. Meet ⇒ cycle.
- **202** — functional graph, `next = sum of digit squares`. `1` is a fixed point (`1→1`), so happy numbers meet at `1`, unhappy ones in a non-`1` cycle → `return slow == 1`. O(1) space (vs the seen-set variant).
- **287** — array as list, `next = nums[i]`. `[1,n]` values + `n+1` of them ⇒ a cycle exists (pigeonhole), and its **entrance is the duplicate**; value range excludes `0`, so index `0` has in-degree 0 (a clean tail-start). **Full two-phase Floyd's:** ① find the meeting point (`slow = nums[slow]`, `fast = nums[nums[fast]]`); ② reset `slow = 0`, advance **both by one** → they meet at the entrance. Phase 2 works because `dist(start→entrance) = dist(meet→entrance)`.
- **Gotchas:** the meeting point is **not** the entrance — phase 2 is required (287); emulate do-while (unroll the first step) so `slow == fast == 0` doesn't exit immediately; the entrance proof needs the start *outside* the loop.

---

## 5. LinkedList In-place Reversal 🟦
*Recognize:* reverse a list or a sub-segment with O(1) space. Thread `prev / curr / next`; for sub-ranges, anchor a dummy head before the segment.
- [x] ✅ **206** Reverse Linked List — *iterative + recursive*
- [x] ✅ **92** Reverse Linked List II
- [x] ✅ **24** Swap Nodes in Pairs

**Notes:** The base move (O(1) space): `nxt = curr.next; curr.next = prev; prev = curr; curr = nxt`. Canonical full reversal: `prev, curr = None, head` → loop → `return prev` (empty/single fall out for free, no guard needed).
- **206** — reverse the whole list.
- **92 (segment):** **dummy head** (left can be 1), walk `prev` to node `left-1`, reverse `right-left+1` nodes, then **reconnect both boundaries** (`prev.next` → new segment head; old segment head → node after `right`). The bugs live in the reconnection and the walk — an off-by-`(left-1)` if the walk loop misfires.
- **24 (fixed 2-chunks):** dummy head; per pair `(p1, p2)`: `cp.next = p2; p2.next = p1; p1.next = next_p; cp = p1`. Loop while `cp.next` and `cp.next.next` exist. Recursive form: swap first two, `head.next = recurse(rest)`.
- **Gotchas:** **save `next` before overwriting** any `.next` (or you lose the tail); reach for a **dummy head** whenever the head can change or you need a stable "node before the action"; a true recursive variant must call **itself**, not delegate to the iterative one.

---

## 6. Monotonic Stack
*Recognize:* "next/previous greater or smaller element," or histogram-style spans. Keep a stack in monotonic order; pop while the incoming element breaks the order, resolving the popped element's answer.
- [x] ✅ **496** Next Greater Element I
- [x] ✅ **739** Daily Temperatures
- [x] ✅ **84** Largest Rectangle in Histogram

**Notes:** Keep the stack monotonic; when a new element **breaks the order, pop — and the pop resolves the popped element's answer**. Each element pushed/popped once → O(n). **Two decisions:** increasing-vs-decreasing (*next greater* → decreasing, pop when `cur > top`; *next smaller / rectangle* → increasing, pop when `cur < top`) and values-vs-indices (store **indices** for positions/distances).
- **496 (next greater, value map):** build `num → next greater` over `nums2` (right-to-left, pop `≤ cur`), then look up `nums1`.
- **739 (next greater, distance):** store indices; `ans[j] = i - j` on pop.
- **84 (largest rectangle):** increasing stack of indices; the bar that pops `j` is `j`'s next-smaller-right, the newly-exposed top is its prev-smaller-left → `width = i - stack[-1] - 1`, `area = h * width`. Flush with a `0` sentinel via a **copy** (`heights + [0]`, don't mutate); handle the empty stack with `width = i` (cleaner than a `-1` sentinel — avoids the `heights[-1]` negative-index trap).
- **Key insight: pop = resolve** — the popper is one bound, the newly-exposed top is the other. (Cousin of the monotonic-*deque* in 1696.)
- **Gotchas:** the `heights[-1]` trap if you use a `-1` sentinel without an explicit `!= -1` guard; don't mutate the input to add a sentinel; choose `<`/`<=`/`>`/`>=` deliberately.

---

## 7. Top-K Elements
*Recognize:* k largest/smallest/most-frequent. Min-heap of size k (largest), max-heap (smallest), or bucket sort by frequency. Heap = O(n log k).
- [x] ✅ **215** Kth Largest Element in an Array
- [x] ✅ **347** Top K Frequent Elements
- [x] ✅ **373** Find K Pairs with Smallest Sums

**Notes:** The counterintuitive core: **a MIN-heap of size k gives the k LARGEST** — the smallest of your top-k sits at the root, evicted in O(log k) when a bigger one arrives. O(n log k), beats an O(n log n) sort when `k ≪ n`. (k smallest → max-heap of size k; `heapq` is min-only, so **negate for max**.)
- **215 (kth largest):** heapify the first k, `heappushpop` the rest, `heap[0]` is the answer. (Bonus: **quickselect** is O(n) average.)
- **347 (top-k frequent):** `Counter`, then min-heap of size k keyed by `(freq, num)` — ties fall back to the int `num`, so it stays comparable. (Alt: **bucket sort** by frequency = O(n), since freq ≤ n; or `Counter.most_common(k)`.)
- **373 (k smallest pairs):** the sums form an **implicit sorted matrix** `M[i][j]=nums1[i]+nums2[j]`. Seed the heap with column 0 of `min(k, len1)` rows; pop the smallest, record it, push only its right neighbor `(i, j+1)` — j-only advance ⇒ each cell reached once, no dupes. **Guard the empty heap** (`if not h: break`) so `k > #pairs` returns all instead of crashing.
- **Gotchas:** size-k **min**-heap for k-*largest* (not size-n max-heap); use **tuples** `(priority, …)` with a comparable tiebreaker; for 373, j-only advance + empty-heap guard.

---

## 8. Overlapping Intervals
*Recognize:* merge/insert/count overlaps. Sort by start; merge when `end ≥ next.start`. For "remove fewest," sort by end and greedily keep.
- [ ] ⬜ **56** Merge Intervals
- [ ] ⬜ **57** Insert Interval
- [ ] ⬜ **435** Non-Overlapping Intervals

**Notes:** _(fill as you go)_

---

## 9. Modified Binary Search
*Recognize:* sorted-but-rotated, or a 2D sorted matrix, or "find boundary/min." Decide which half is sorted, then narrow.
- [ ] ⬜ **33** Search in Rotated Sorted Array
- [ ] ⬜ **153** Find Minimum in Rotated Sorted Array
- [ ] ⬜ **240** Search a 2D Matrix II

**Notes:** _(fill as you go — builds on the §iterative-binary-search template, 704)_

---

## 10. Binary Tree Traversal 🟦
*Recognize:* the traversal order encodes the problem — PreOrder (root-first, paths), InOrder (sorted, BST), PostOrder (children-first, aggregates).
- [ ] ⬜ **257** Binary Tree Paths *(PreOrder)*
- [ ] ⬜ **230** Kth Smallest Element in a BST *(InOrder)*
- [ ] ⬜ **124** Binary Tree Maximum Path Sum *(PostOrder)*

**Notes:** _(fill as you go — you own trees from §10/§12; 124 is the tricky one)_

---

## 11. Depth-First Search 🟦
*Recognize:* explore all paths/branches; connectivity; topological order. Recursion or explicit stack.
- [x] ✅ **133** Clone Graph — *done*
- [ ] ⬜ **113** Path Sum II
- [x] ✅ **210** Course Schedule II — *done (DFS + Kahn's)*

**Notes:** _(fill as you go)_

---

## 12. Breadth-First Search 🟦
*Recognize:* shortest path in an unweighted graph; level-order. Queue, process level by level.
- [ ] ⬜ **102** Binary Tree Level Order Traversal
- [x] ✅ **994** Rotting Oranges — *done (multi-source BFS)*
- [ ] ⬜ **127** Word Ladder

**Notes:** _(fill as you go)_

---

## 13. Matrix Traversal 🟦
*Recognize:* grid as an implicit graph; flood-fill / region problems. 4-dir `dirs`, mark visited in place.
- [x] ✅ **733** Flood Fill — *done*
- [x] ✅ **200** Number of Islands — *done*
- [ ] ⬜ **130** Surrounded Regions

**Notes:** _(fill as you go — 130's trick: seed from the border)_

---

## 14. Backtracking
*Recognize:* enumerate all permutations/combinations/subsets/placements under constraints. Choose → recurse → un-choose.
- [ ] ⬜ **46** Permutations
- [ ] ⬜ **78** Subsets
- [ ] ⬜ **51** N-Queens

**Notes:** _(fill as you go — the bridge into DP; 212 used grid backtracking)_

---

## 15. Dynamic Programming *(the deep-dive — separate `dynamic-programming.md` to follow)*
*Recognize:* overlapping subproblems + optimal substructure. Sub-families: Fibonacci/1-D, 0/1 knapsack, LCS, LIS, subset-sum.
- [x] ✅ **70** Climbing Stairs — *done (O(1) Fibonacci)*
- [ ] ⬜ **198** House Robber
- [ ] ⬜ **322** Coin Change
- [ ] ⬜ **1143** Longest Common Subsequence
- [ ] ⬜ **300** Longest Increasing Subsequence
- [ ] ⬜ **416** Partition Equal Subset Sum

**Notes:** _(deferred to the DP ladder — `dynamic-programming.md`)_

---

## Not in this article (already done, complementary)
Your recent **Trie** (208/211/212) and **Union-Find** (547/684/323/1319) work isn't among these 15 patterns —
they're additional coverage. Likewise 49, 121, 125, 217, 235, 278, 383, 409, 704 and others sit outside the article's picks.
