# LeetCode Patterns — recognition + practice tracker

A pattern-first pass before the DP deep-dive, following AlgoMaster's
[15 LeetCode Patterns](https://blog.algomaster.io/p/15-leetcode-patterns). The thesis (patterns > raw volume)
matches how the data-structure walk (`data-structures.md` §1–16) was run.

**Approach:** learn each pattern in order, then solve its problems — **skip any already done in Python**, write the rest.
Fill the per-pattern **Notes** (recognition cue → template → gotchas) as you go, the same solve-plus-notes rhythm as the
data-structure walk.

**Legend:** ✅ done in Python · ⬜ to do · 🟦 *pattern already owned from prior work — these specific problems are quick reps*

**Progress: 41 / 48 done.** Recommended order (easy→hard, backtracking last as the bridge into DP):
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
- [x] ✅ **56** Merge Intervals
- [x] ✅ **57** Insert Interval
- [x] ✅ **435** Non-Overlapping Intervals

**Notes:** Sort first — but the sort key depends on what you're optimizing for, and picking the wrong one gives a wrong-but-plausible answer.
- **56 (merge overlapping):** sort by **start**; walk once, extending a running interval — `current[1] = max(current[1], next[1])`, not a plain overwrite, since that's what handles containment (`[1,10]` swallowing `[2,3]`). Extend when `next.start ≤ current.end` (touching intervals like `[1,4]`,`[4,5]` still merge), else flush and start fresh. A `None` sentinel for "no current interval yet" needs `is None`, not truthiness — an interval is a list, and `not []` is also `True`, so plain truthiness only works because LeetCode guarantees non-empty intervals.
- **57 (insert into pre-sorted, non-overlapping):** no sort — the input's ordering guarantee is the whole reason this is O(n) instead of O(n log n). Three-way single pass per original interval: fully before the new one → keep as-is; fully after → flush whatever's pending (the new interval, or something it already absorbed) and swap the pending slot to this interval; otherwise → merge (`min` of starts, `max` of ends). The "pending" variable does double duty: starts out meaning "the new interval," but the moment that's flushed it starts relaying whichever original interval hasn't been placed yet.
- **435 (remove fewest to de-overlap):** sort by **end**, not start — the greedy exchange-argument proof specifically needs "keep whichever interval finishes earliest." Track `current_end` (seed `float("-inf")` to dodge a first-iteration special case); keep an interval when `start ≥ current_end`, else count it as removed. Sorting by end also makes containment free: a wide interval that contains others always has the latest end, so it sorts last and is the one greedily dropped.
- **Touching intervals:** overlapping for merge/insert (56/57 use strict `<`/`>` to detect the *disjoint* case) but **not** overlapping for erase (435's `≥` keeps `[1,2]`,`[2,3]` as two separate intervals) — same shape of check, opposite intent, so get the direction right per problem.
- **Gotchas:** `max`/`min`, not overwrite, when merging bounds (breaks containment otherwise); binding a merge accumulator directly to an input sub-list (`current = interval`) mutates the caller's array in place — build a fresh `[start, end]` instead; wrong sort key (start vs end) is the single most common way to get 435 wrong while still looking plausible.

---

## 9. Modified Binary Search
*Recognize:* sorted-but-rotated, or a 2D sorted matrix, or "find boundary/min." Decide which half is sorted, then narrow.
- [x] ✅ **33** Search in Rotated Sorted Array
- [x] ✅ **153** Find Minimum in Rotated Sorted Array
- [x] ✅ **240** Search a 2D Matrix II

**Notes:** The reframe: binary search doesn't need "sorted" — it needs an **O(1) test that discards a predictable chunk of the search space**. Each problem breaks plain-sortedness differently and repairs the decision rule. **Two templates**, and mixing them is the classic infinite-loop bug:
- **(A) Exact target (704, 33):** closed `[left, right]`, `while left <= right`, hit returns early, both moves `±1`, exhausted → `-1`.
- **(B) Boundary converge (153):** `while left < right`, `left = mid + 1` / `right = mid` (mid may *be* the answer — keep it), no early return, answer where they meet. Pairing rule: floor-mid ⟹ `mid < right`, so `right = mid` still shrinks; `left = mid` would spin (mid can equal left). `right = mid` inside a `<=` loop = infinite loop.
- **33 (rotated, find value):** at any mid **at least one half is properly sorted**; one comparison identifies which, then range-check the target against the sorted half's endpoints and enter-or-avoid it. Canonical decoupled check: `nums[left] <= target < nums[mid]` (the `<=` carries the equality). My variant (strict `>` + early `target == nums[left]` returns) is correct but **coupled** — deleting the early return breaks `[1,2,3], target=1`.
- **153 (rotated, find min):** Template B, **anchor on `nums[right]`, never `nums[left]`**. `nums[mid] > nums[right]` ⟹ drop in `(mid, right]` → `left = mid + 1`; else `[mid..right]` ascending → `right = mid`. The left anchor is *ambiguous*: `nums[mid] > nums[left]` is true both for a fully-sorted window (min at `left`) and a kink-right window (min right of mid) — opposite moves, and the window *inevitably* becomes sorted as it converges (30/45 rotations failed). The right anchor's two worlds both put the min at-or-left-of mid — the ambiguity **folds into the same safe move**. Bonus: `mid < right` in-loop ⟹ never self-compares (the `[1,0]` trap).
- **Anchor discipline (33 vs 153):** why left worked in 33 but not 153 — 33 draws a *weak* conclusion ("this half is sorted", true in both ambiguous worlds) then discriminates with a **second signal** (target range-check); 153 has no target, so its single comparison must decide the move alone. **Every comparison must unambiguously support the exact conclusion drawn from it** — prove each discard safe in every world consistent with the comparison.
- **240 (2D row+col sorted):** not really binary search — **staircase from top-right**: `cur < target` → row can't contain it, `i += 1`; `cur > target` → column can't, `j -= 1`. One comparison discards a full row/column ⟹ O(m+n); works with duplicates (non-strict sort). Corner must have *opposing* moves (top-right / bottom-left); from top-left both moves increase — dead. Row-by-row BS is O(m log n), better only for degenerate shapes (m ≪ n).
- **Gotchas:** template mixing (see pairing rule); left-anchoring 153; C# `left + (right - left) / 2` vs overflow (Python ints don't care); duplicates variants **81/154** break the sorted-half test on `nums[mid] == nums[anchor]` — shrink by one (`left += 1`), degrades to O(n) worst case.

---

## 10. Binary Tree Traversal 🟦
*Recognize:* the traversal order encodes the problem — PreOrder (root-first, paths), InOrder (sorted, BST), PostOrder (children-first, aggregates).
- [x] ✅ **257** Binary Tree Paths *(PreOrder)*
- [x] ✅ **230** Kth Smallest Element in a BST *(InOrder)*
- [x] ✅ **124** Binary Tree Maximum Path Sum *(PostOrder)*

**Notes:** **The traversal order encodes the problem** — root-first (PreOrder) when state flows parent→child; InOrder when the BST property should hand you sorted order; children-first (PostOrder) when a node's answer aggregates its subtrees. *(+ bonus rep: 543 Diameter as the 124 warm-up.)*
- **257 (PreOrder, paths):** accumulate on the way down, emit `"->".join(...)` at leaves. Two accumulation styles, both worth owning: **shared list + append/pop** (choose → recurse → un-choose — Backtracking-pattern preview) vs **copy-on-push** (`path + [v]`, natural for the iterative stack form; push right first so left pops/emits first). **Leaf = both children `None`** — a one-child node is not a leaf. Pick ONE `None`-defense policy (guard at entry *or* at call sites), not both.
- **230 (InOrder, BST):** in-order visits a BST in sorted order ⇒ kth smallest = kth visited. The point is **early termination** — O(h + k), don't finish the walk. Recursive form: guard on `len(seen) >= k` at entry *and* after the left-recursion; list-mutation dodges `nonlocal` (mutate-don't-rebind), at O(k) memory for a 1-value answer (`nonlocal count/result` would be O(1)). *Still to do: the generator form — `yield from` in-order + `islice` makes early stop automatic (the open `yield` TODO).* k is **1-indexed**.
- **124 (PostOrder, the hard one):** every node computes **two different quantities** — **report up** the single-arm gain `val + max(0, l_b, r_b)` (a parent path can extend down only one arm), **record** the both-arms join `max(l_p, r_p, val + l_b + r_b)`. Clamps `max(0,·)` only on the *arms*, never on `val` itself. **Unify with the base case `None → (0, -inf)`** — two identities for two quantities: `0` = empty *extension* (identity of the clamp), `-inf` = *no path exists* (identity of max; can never beat a real path, which guarantees the answer is a non-empty path — all-negative trees return the least-negative node, never 0).
- **The bug I actually wrote:** four-way branch on children-existence, with the record logic duplicated per branch — correct in the two-child copy, wrong in both single-child copies (dropped the child's record: `[-10, left=5]` → -5 instead of 5). **Duplicated logic rots independently; absorb the asymmetry into the base case.** The unpacked-but-unused `left_p` was the lint-smell pointing at it. And both LC examples are *full* trees — the single-child branches never even ran on them; 1,603/3,840 brute-force trees failed. Examples ≠ coverage.
- **543 (Diameter — same skeleton, easier):** report height in *nodes*, record diameter in *edges*; through-node = `l_h + r_h`. **Sentinel contrast with 124:** empty-record identity `0` is safe here because 0 is an attainable valid answer (single node); 124 needed `-inf` because 0 would mean the forbidden empty path. *The no-answer sentinel must be unable to beat any real answer.*
- **Gotchas:** leaf ≠ one-child node (257); k 1-indexed (230); init the record to `-inf` not 0 and never clamp `val` in the record candidate (124); per-branch duplicated logic (124); the report/record pair generalizes (543, 687, most hard tree problems).

---

## 11. Depth-First Search 🟦
*Recognize:* explore all paths/branches; connectivity; topological order. Recursion or explicit stack.
- [x] ✅ **133** Clone Graph — *done*
- [x] ✅ **113** Path Sum II
- [x] ✅ **210** Course Schedule II — *done (DFS + Kahn's)*

**Notes:** DFS = exhaust every branch/path; recursion by default, explicit stack when depth threatens (Python's ~1000 recursion limit).
- **113 (path enumeration — the backtracking on-ramp):** 257's PreOrder skeleton plus a running sum, done shared-list append/pop style (choose → recurse → un-choose). **Two kinds of path-state, and only one needs un-choosing:** `path` is a *shared mutable* list — every frame sees the same object, so the exit must `pop()` what the entry appended; the running sum is a *per-frame int* — the call stack undoes it for free (the symmetric-looking `sum -= node.val` unwind in the first draft was dead code). **Copy at the leaf** (`path[:]`) — appending the live list fills the answer with aliased views of one finally-empty list; invisible on shallow examples. **No pruning** — negatives mean `path_sum > target` proves nothing. Leaf = both children `None` (an internal node whose prefix hits the target emits nothing). Reading a captured name needs no `nonlocal` — only *rebinding* does (the 6/19 rule, re-learned).
- **133 Clone Graph (prior work):** DFS with an `old → clone` map that doubles as the visited set — create the clone and map it **before** recursing into neighbors, or cycles recurse forever.
- **210 Course Schedule II (prior work):** topological order both ways — DFS finish-order reversed (needs an on-path/3-color cycle check) and Kahn's in-degree peeling (BFS cousin).
- **Gotchas:** builtin shadowing is now a *named habit* — `sum` (643), `next` (230), `sum` again (113 first draft); rename (`path_sum`) or invert to count-down `remaining - node.val`, which also deletes the outer capture. Time is O(n) traversal but **Θ(n²) worst-case output** (caterpillar-of-zeros: ~n/2 matching leaves × ~n/2 depth) — the per-leaf copy is the real cost, not the walk.

---

## 12. Breadth-First Search 🟦
*Recognize:* shortest path in an unweighted graph; level-order. Queue, process level by level.
- [x] ✅ **102** Binary Tree Level Order Traversal
- [x] ✅ **994** Rotting Oranges — *done (multi-source BFS)*
- [x] ✅ **127** Word Ladder

**Notes:** BFS = shortest path in an *unweighted* graph, and level-order processing. Queue; the whole craft is in how you delimit levels and how you avoid re-visiting.
- **102 (the level template, both forms):** ① **level-list swap** — `frontier` / `next_frontier`, swap at the bottom; materializes each level, natural when the output *is* per-level lists. ② **single `deque` + size snapshot** — `level_size = len(queue)` *before* draining; the queue grows mid-level, so the snapshot is the level boundary (the load-bearing line). Same O(n) time, O(width) space (worst ~n/2 at a full tree's bottom). Form ① is 127's shape; form ② generalizes when levels don't need to be objects.
- **127 (the meaty one — the graph is implicit):** words = nodes, one-letter edits = edges. **Never build the graph pairwise** — O(N²·L) ≈ 125M char-ops = TLE; *index* it instead. **Wildcard buckets:** `hot → *ot/h*t/ho*`, a `pattern → [words]` map (O(N·L²) build) — the 49-Group-Anagrams move, the pattern *is* the hash key; two words are adjacent ⟺ they share a bucket; a bucket holds ≤ 26 words (members differ only at the wildcard). **Drain each bucket exactly once** (a visited-set on *patterns* ≡ clearing the bucket) — safe because BFS reaches a bucket first at minimal level, so any re-scan could only rediscover words the worse way. Don't materialize word→word adjacency for a one-shot query — lazy expansion does strictly less work and stops at `endWord`. Alternative neighbor gen: 25·L mutations + set membership (O(26·L²) per word, N-independent) — less code, same order at these constraints. `beginWord`: *look up* its patterns, never store it — nothing needs to discover it. Answer counts **words including `beginWord`** (levels + 1 at discovery).
- **994 (prior):** multi-source BFS — seed every rotten orange at level 0; minutes = levels.
- **Gotchas:** mark visited **on enqueue, not on pop** — else the same node enters the queue through many parents and the queue explodes; the mid-level `len(queue)` trap without a snapshot; `endWord not in wordList → 0` before any work; a leftover debug `print` of the 50k-entry bucket map is a TLE all by itself (caught in review); going without a word-level visited set works *only* because bucket-drain-once bounds total enqueues at N·L — kept deliberately, but the proof is implicit, so be able to say it out loud.

---

## 13. Matrix Traversal 🟦
*Recognize:* grid as an implicit graph; flood-fill / region problems. 4-dir `dirs`, mark visited in place.
- [x] ✅ **733** Flood Fill — *done*
- [x] ✅ **200** Number of Islands — *done*
- [x] ✅ **130** Surrounded Regions

**Notes:** Grid = implicit graph: 4-dir `dirs` tuple, bounds-check, mark visited **in place** (sentinel or sink) instead of a `visited` set.
- **130 (the border-seed inversion):** don't hunt for surrounded regions — **invert the question: find what survives**. Seed every border `O`, flood-mark reachable cells with a sentinel (`A`), then one sweep: `O → X` (captured), `A → O` (restored). Seeding detail: column loops take all rows incl. corners; row loops run `range(1, n-1)` so corners aren't re-processed (harmless anyway — mark-before-append makes re-seeds no-ops, which is also what saves the degenerate m=1 board). O(m·n) time and worst-case space — optimal.
- **Deque-as-stack gotcha (from the 130 review):** `deque.pop()` pops the **right** end — that's a stack, i.e. iterative **DFS**, not BFS. Fine for flood fill (order-agnostic + mark-on-enqueue = each cell once), but then a plain `list` says it honestly with no import; `popleft()` is what makes it BFS. In an order-sensitive problem (127, any shortest-distance grid) the same slip breaks correctness *silently* — flood fill forgives, distance-BFS doesn't.
- **Recursion limit is a real constraint here:** 200×200 board ⇒ a region can be 40k cells ⇒ the recursive fill habit from 733/200 dies with `RecursionError` at ~1000 frames. The concrete case for P11's "recursion by default, explicit stack when depth threatens."
- **733 Flood Fill (prior):** the base operation — guard the `new color == old color` no-op case or the fill self-triggers forever.
- **200 Number of Islands (prior):** count the fills; sink visited land in place (`'1' → '0'`).
- **Gotchas:** mark **before** enqueue, not on pop; an in-place sentinel must be restored in the final sweep; `r, l` for row/column fights the `r`/`c` grid convention (and bare `l` is the E741 habit's third appearance).

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
**543 Diameter of Binary Tree** (2026-07-08) was solved as the deliberate warm-up for 124 — same report/record skeleton, lengths instead of sums.
