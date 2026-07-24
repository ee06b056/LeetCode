# Dynamic Programming

Working notes for the DP climb. Opened at the 15-pattern sweep close-out (2026-07-23, 48/48) with the ladder's lessons — **70 · 509 · 198 · 322 · 1143 · 300 · 416** (plus 53, 1696, 124 as earlier DP under other names). Grows alongside the endlesscheng 动态规划 题单 (~810 problems, 15 sections) per the workspace `Plan.md` curriculum: recognize → state → transition → base case, one section at a time. Tracker: `curriculum.md`.

## The 5-question derivation checklist

Run these in order on any new DP problem; answer them in words before writing code.

1. **Last decision** — what choice does the final step make? (The last coin. The last char pair. Which predecessor to attach to. In the subset or not.) The options become the branches of the recurrence.
2. **Minimal state** — the least information that makes subproblems self-contained. Test: does the answer depend only on the state, not on *how* you reached it (path independence)? If extending needs something extra, that something belongs **in** the state (300: extension needs the last element, so the state is "ends exactly at i").
3. **Recurrence** — combine the branches (`min` / `max` / `sum` / `or`). A *forced* case takes no `max` — prove domination instead (1143's equal-chars case).
4. **Base case + sentinel** — the base is the **identity / empty problem** (amount 0, empty prefixes, sum 0). Absorb special cases into it; hand-coded extras (322's "amount == coin → 1") are the recurrence's own job and rot independently. Sentinel for "no answer": must never beat a real answer — **∞ for min, −∞ for max, 0 for counting** (the 124 rule).
5. **Order & complexity** — top-down: evaluation order is free (recursion resolves it). Bottom-up: dependencies must already be filled. Time = state count × transition cost.

## The pipeline: brute recursion → memo → table

1. Write the brute-force recursion straight from the checklist. Correct first; slow is fine.
2. Overlapping subproblems → memoize. Seed the memo with the identity (322: `dp = {0: 0}` — the base case living inside the cache).
3. Flip mechanically: memo keys → array indices, recursion → loops obeying dependency order.

Write **both** forms every time (also the curriculum's advice). The Python-specific reason the table matters: top-down depth ≈ amount / min-step, and the default recursion limit is ~1000 — 322 with `coins=[1], amount=1500` dies locally on cue (LeetCode's judge raises the limit; your terminal doesn't). The table can never die this way.

## One invariant, three mechanisms (0/1 knapsack)

**This round's reads must see last round's state** — otherwise the current item gets used twice.

| Mechanism | Seen in |
|---|---|
| Two rows (`dp` / `dp_next`, or copy-then-build) | 1143 rolled LCS · 416 set form |
| Snapshot before iterating (`list(sum_set)`) | 416 draft · 78's doubling |
| **Backward** 1-D inner loop | 416 canonical boolean array |

**Forward on 1-D = unbounded knapsack** — exactly 322's bottom-up, where forward is *correct* because coins are reusable. The inner-loop direction is the entire difference between "each item once" and "unlimited supply": one loop header, two different problems.

## Rolling rows and their classic bug

- The rolled array is indexed by the **inner** loop variable, so array size = inner dimension + 1 — and therefore **the inner loop decides your space** (shorter string inner ⇒ O(min(m, n))).
- Loop order and index naming are independent choices. LCS is symmetric so either string may be outer; **not every DP grants this** (knapsack's inner direction is load-bearing — see above).
- The classic bug: writing **diagonal** (`dp[j-1]`) where **up** (`dp[j]`) belongs. In the full 2-D table `dp[i-1][j]` vs `dp[i-1][j-1]` are hard to confuse; rolled, they blur into near-identical expressions. Effect: value flows right and down-right but never straight down (`"ab"`/`"acb"` → 1 instead of 2; 428/5,005 draft failures). **2-D first, verify, then roll.**

## Where the answer lives (part of the state design)

- **Prefix state** ("first i" / "first i, j") → answer in the **last cell**; correct tables are monotone toward the corner (1143 — which is also why its running-max tracker was redundant and bug-masking).
- **Ends-exactly-here state** → answer = **max over all cells**; any index can host the ending (300, Kadane 53).

Choosing the state chooses where you harvest.

## Sentinels, seeds, and type honesty

- Identity base case, not enumerated specials. The dead-guard habit (198's `len == 1`, 70's `n == 1` — loop already covers them) is the same instinct in loop form.
- Sentinel must lose to every real answer: ∞ (min) / −∞ (max) / 0 (count). Origin: 124's `None → (0, -inf)` — two different identities from one base case.
- **Truthiness hides wrong types.** `dp[0] = [True]` (a list) survived 6,620 checks because it was only ever truth-tested and never returned (`target ≥ 1` kept it off the return path). Cousin of 56's `if not ci:`. Type-check the seeds — the signature says `bool`, make the seed say `True`.

## Not-DP neighbor: patience sorting (300's O(n log n))

Greedy + binary search — say it in interviews: "O(n²) is the DP; O(n log n) replaces it with a greedy invariant plus binary search."

- `tails[k]` = smallest tail among all increasing subsequences of length k+1.
- Sorted **by construction** (a length-k subsequence contains a shorter one with a smaller tail) → bisect is legal.
- Per element: `bisect_left`; append (the only way length grows) or replace (same length, easier future — replacing with a smaller tail can never hurt).
- `bisect_left` = strictly increasing; `bisect_right` = non-decreasing. One character, opposite meaning.
- `tails` is a summary, **not a witness**: `[3, 4, 1]` ends with `tails = [1, 4]` — right length, not a real subsequence. Recovering the actual LIS needs extra bookkeeping (the O(n²) DP recovers it more easily).

## When is DP *needed*? The greedy-failure cue

Coins `[1, 3, 4]`, amount 6: greedy takes 4+1+1 = 3 coins; optimal is 3+3 = 2. When the locally best choice can strand you, you must enumerate the decision — that is DP's job.

## Up next (per `curriculum.md`)

入门 DP → 网格图 → 背包 → 经典线性 → 划分型 → 状态机 → 树形 (+ 区间 taste). ≤1700 rating first pass; first problem of each section as a case study; both memo and table forms every time.
