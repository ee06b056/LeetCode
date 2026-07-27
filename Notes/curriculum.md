# Interview curriculum tracker (2026-07-27 → 09-11)

Adopted 2026-07-21 (workspace `Plan.md`). Sources: [endlesscheng topic lists](https://leetcode.cn/discuss/post/3141566/ru-he-ke-xue-shua-ti-by-endlesscheng-q3yd/) (难度分 ≤ 1700 first pass, 1700–2000 second pass, > 2000 never) + [AlgoMaster 20 DP patterns](https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming) as the English checklist. Prerequisite — the 15-pattern sweep (`patterns.md`): **completed 48/48 on 2026-07-23.**

Rules: first problem of each new section = case study; both memo + table forms for every DP problem; tick a section when its ≤1700 pass feels *closed*, not when every listed problem is done (the DP list alone is ~810). Update the solved counters as you go; named problems get their own boxes. Notes accumulate in `dynamic-programming.md`.

## DP backbone (endlesscheng 动态规划 题单, in list order)

- [ ] **入门 DP** (climbing-stairs family) — solved: 3 (746 · 213 · 740, 2026-07-26) *(ladder credit: 70 · 509 · 198 · 322)*
- [ ] **网格图 DP** (grid paths) — solved: 0
- [ ] **背包** (0/1 · unbounded · counting) — solved: 0 *(ladder credit: 416 0/1 · 322 unbounded)*
- [ ] **经典线性 DP** (LCS / edit-distance family) — solved: 0 *(ladder credit: 1143 · 300)*
- [ ] **划分型 DP** (partition / word-break family) — solved: 0
- [ ] **状态机 DP** (stock series) — solved: 0
- [ ] **树形 DP** — [ ] 337 House Robber III · [ ] 968 BT Cameras *(prior credit: 124)*
- [ ] **区间 DP taste** — [ ] 516 Longest Palindromic Subsequence · [ ] 1039 Min Score Triangulation
- [ ] **Second pass 1700–2000** (favorite sections only)

## Side threads (one per week, per `Plan.md`)

### Bits (week of 7/27) — **complete 2026-07-26, a day early**
- [x] 136 Single Number · [x] 190 Reverse Bits · [x] 191 Number of 1 Bits · [x] 268 Missing Number · [x] 338 Counting Bits · [x] 260 Single Number III

### Binary search on the answer (week of 8/3)
- [ ] 875 Koko Eating Bananas · [ ] 1011 Ship Packages · [ ] 410 Split Array Largest Sum · [ ] 1482 M Bouquets · [ ] 1552 Magnetic Force · [ ] 2226 Candies for K Children

### Graphs 1 — topological sort + union-find refresh (week of 8/10)
- [ ] 207 Course Schedule · [ ] 210 Course Schedule II · [ ] 802 Eventual Safe States · [ ] 310 Min Height Trees · [ ] 2115 Possible Recipes · [ ] 721 Accounts Merge · [ ] 990 Equality Equations

### Graphs 2 — Dijkstra + bipartite (week of 8/17)
- [ ] 743 Network Delay Time · [ ] 1631 Path With Min Effort · [ ] 1514 Max Probability · [ ] 787 Cheapest Flights (K stops) · [ ] 1976 Ways to Arrive · [ ] 785 Is Graph Bipartite

### Math tricks / identity drill (week of 8/24) — identity → anchor problem → writable cold in < 2 min
- [ ] 50 fast exponentiation · [ ] 204 prime sieve · [ ] 1071 GCD · [ ] 169 Boyer-Moore · [ ] 382 reservoir sampling · [ ] 384 Fisher-Yates · [ ] 202 Floyd's cycle · [ ] 62 combinatorics formula · [ ] 172 factorial structure · [x] 53 Kadane *(done, 2026-05)*

### Anytime warm-ups
- [ ] 55 Jump Game · [ ] 45 Jump Game II · [ ] 134 Gas Station · [ ] 763 Partition Labels · [ ] 621 Task Scheduler *(greedy)*
- [ ] 295 Find Median from Data Stream *(dual-heap — interview classic the sweep skipped)*
- [ ] 5 Longest Palindromic Substring · [ ] 8 String to Integer · [ ] 28 KMP intro *(strings)*

## Grind169 backfill (audited 2026-07-23)

Grind75 at the 8 wk × 19 h setting = the full 169-question list. Audit result: **73/169 already solved** (59 in Python, 14 C#-only), **16 more already scheduled** in the sections above (295 · 169 · 721 · 8 · 62 · 310 · 621 · 134 · 338 · 191 · 55 · 136 · 50 · 268 · 787 · 190), **80 remaining below** (~39 h total; *(P)* = LC Premium — skip or substitute if no subscription). Use as the pool for anytime warm-ups, Method B random sets, and September mocks. The **DP bucket will arrive naturally via the backbone** (139/91 划分型 · 152 入门 · 221 网格图 · 377 背包 counting · 329 网格图+记忆化) — tick them there when they do.

### Stack & parsing
- [ ] 150 Evaluate RPN · [ ] 155 Min Stack · [ ] 224 Basic Calculator *(Hard)* · [ ] 227 Basic Calculator II · [ ] 394 Decode String · [ ] 735 Asteroid Collision · [ ] 895 Max Frequency Stack *(Hard)* · [ ] 32 Longest Valid Parentheses *(Hard)* · [ ] 42 Trapping Rain Water *(Hard)*

### Arrays, strings & matrix
- [ ] 238 Product Except Self · [ ] 75 Sort Colors · [ ] 189 Rotate Array · [ ] 283 Move Zeroes · [ ] 844 Backspace Compare · [ ] 977 Squares of Sorted Array · [ ] 16 3Sum Closest · [ ] 41 First Missing Positive *(Hard)* · [ ] 48 Rotate Image · [ ] 54 Spiral Matrix · [ ] 73 Set Matrix Zeroes · [ ] 36 Valid Sudoku · [ ] 179 Largest Number · [ ] 31 Next Permutation · [ ] 271 Encode/Decode Strings *(P)* · [ ] 67 Add Binary

### Sliding window & binary search
- [ ] 424 Longest Repeating Char Replacement · [ ] 438 Find All Anagrams · [ ] 239 Sliding Window Maximum *(Hard; 1696's deque)* · [ ] 658 Find K Closest Elements · [ ] 74 Search a 2D Matrix · [ ] 4 Median of Two Sorted Arrays *(Hard)*

### Linked list
- [ ] 876 Middle of LL · [ ] 19 Remove Nth From End · [ ] 234 Palindrome LL · [ ] 328 Odd Even LL · [ ] 143 Reorder List · [ ] 148 Sort List · [ ] 61 Rotate List · [ ] 25 Reverse k-Group *(Hard)* · [ ] 23 Merge k Sorted Lists *(Hard)*

### Trees & BST
- [ ] 98 Validate BST · [ ] 105 Build from Preorder+Inorder · [ ] 108 Sorted Array → BST · [ ] 103 Zigzag Level Order · [ ] 437 Path Sum III · [ ] 572 Subtree of Another Tree · [ ] 662 Max Width · [ ] 863 All Nodes Distance K · [ ] 285 Inorder Successor *(P)* · [ ] 297 Serialize/Deserialize *(Hard)*

### Graphs & BFS
- [ ] 261 Graph Valid Tree *(P)* · [ ] 269 Alien Dictionary *(Hard, P)* · [ ] 815 Bus Routes *(Hard)* · [ ] 1730 Shortest Path to Food *(P)* · [ ] 1197 Min Knight Moves *(P)* · [ ] 329 Longest Increasing Path *(Hard)*

### Backtracking
- [ ] 39 Combination Sum · [ ] 17 Letter Combinations · [ ] 22 Generate Parentheses · [ ] 79 Word Search · [ ] 37 Sudoku Solver *(Hard)*

### DP (auto-covered by backbone — tick when they arrive)
- [ ] 139 Word Break · [ ] 152 Max Product Subarray · [ ] 91 Decode Ways · [ ] 221 Maximal Square · [ ] 377 Combination Sum IV · [ ] 1235 Job Scheduling *(Hard)*

### Intervals
- [ ] 252 Meeting Rooms *(P)* · [ ] 253 Meeting Rooms II *(P)* · [ ] 759 Employee Free Time *(Hard, P)*

### Design
- [ ] 146 LRU Cache · [ ] 981 Time-Based KV Store · [ ] 380 Insert/Delete/GetRandom O(1) · [ ] 362 Hit Counter *(P)* · [ ] 528 Random Pick with Weight · [ ] 588 In-Memory File System *(Hard, P)*

### Heap & hard mixed
- [ ] 692 Top K Frequent Words · [ ] 632 Smallest Range K Lists *(Hard)* · [ ] 336 Palindrome Pairs *(Hard)* · [ ] 7 Reverse Integer

## September — simulation

- [ ] Method B: random untagged sets started (week of 8/31)
- [ ] Hack2Hire timed mocks, 2/week
- [ ] Method C: company-frequency lists for scheduled loops
