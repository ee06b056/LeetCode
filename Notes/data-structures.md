# Data Structures — .NET / LeetCode reference

A working reference for the data structures used in LeetCode practice, written in .NET / C# terms. Focuses on what's actually useful when solving problems, not full BCL surface.

Coverage so far: array, `List<T>`, linked list (BCL + LeetCode `ListNode`).

---

## 1. Array — `T[]`

**Underlying:** Fixed-size contiguous block of memory. Length is decided at allocation and cannot grow.

**Declarations**

```csharp
int[] a = new int[10];          // zero-initialized, length 10
int[] b = { 1, 2, 3 };          // length 3
int[] c = new int[] { 1, 2, 3 };
int[,] grid = new int[3, 4];    // rectangular 2D — rare in LeetCode
int[][] jagged = new int[3][];  // jagged 2D — what LeetCode usually gives you
```

**The only property you use:** `arr.Length`.

**Operations & complexity**

| Operation               | Code                            | Time       |
| ----------------------- | ------------------------------- | ---------- |
| Read / write            | `arr[i] = x`                    | O(1)       |
| Sort                    | `Array.Sort(arr)`               | O(n log n) |
| Reverse                 | `Array.Reverse(arr)`            | O(n)       |
| Linear search           | `Array.IndexOf(arr, x)`         | O(n)       |
| Binary search (sorted)  | `Array.BinarySearch(arr, x)`    | O(log n)   |
| Fill                    | `Array.Fill(arr, val)`          | O(n)       |
| Copy                    | `Array.Copy(src, dst, n)`       | O(n)       |

**LeetCode patterns**

- **Hash by index** (small integer keys): `int[26]` for lowercase letters, `int[128]` for ASCII.
- **Two-pointer / sliding window** — the bread-and-butter array patterns.
- **Prefix sums** — `prefix[i] = sum of arr[0..i-1]`, then range sum is `prefix[r+1] - prefix[l]`.
- **In-place tricks** — sign-flipping to mark visited, swapping to sort into known positions.

**Gotcha:** `Array.BinarySearch` returns a *negative* number `~insertion_point` when the value is not found — not just `-1`. Bitwise-complement the return value to get the insertion index.

---

## 2. `List<T>` — the dynamic array

**Underlying:** An internal `T[]` (`Capacity`) plus a `Count`. When `Count == Capacity` and you `Add`, it allocates a new array of typically **2x capacity** and copies everything over.

**Two numbers, not one:**

- `Count` — how many items you actually have. **This is what you read.**
- `Capacity` — size of the underlying array. Rarely matters in LeetCode; you can preallocate with `new List<int>(n)` to avoid resizes, that is all.

**Operations**

| Operation         | Code                                     | Time             |
| ----------------- | ---------------------------------------- | ---------------- |
| Indexed access    | `list[i]`                                | O(1)             |
| Append            | `list.Add(x)`                            | O(1) amortized   |
| Insert            | `list.Insert(i, x)`                      | O(n) — shifts tail |
| Remove by value   | `list.Remove(x)`                         | O(n)             |
| Remove by index   | `list.RemoveAt(i)`                       | O(n) — shifts tail |
| **Pop last**      | `list.RemoveAt(list.Count - 1)`          | **O(1)**         |
| Contains          | `list.Contains(x)`                       | O(n)             |
| Sort              | `list.Sort()`                            | O(n log n)       |
| To array          | `list.ToArray()`                         | O(n)             |
| Last element      | `list[^1]` (C# 8+) or `list[list.Count - 1]` | O(1)         |

**LeetCode patterns**

- **Building a result of unknown size** — `var result = new List<int>();`, then `result.Add(...)`. LeetCode signatures usually want `IList<int>`, which `List<int>` implements.
- **Use it as a stack** when you do not want to import `Stack<T>`: push = `Add`, peek = `list[^1]`, pop = `RemoveAt(list.Count - 1)`. All O(1).
- **Never use it as a queue.** `RemoveAt(0)` is O(n) — use `Queue<T>` instead.

---

## 3. Linked lists — two different things

The phrase "linked list" covers **two unrelated concepts** in LeetCode work:

### 3a. `LinkedList<T>` — the BCL collection (rarely useful in LeetCode)

**Underlying:** Doubly-linked list. Each item is wrapped in a `LinkedListNode<T>` with `.Value`, `.Next`, `.Previous`.

| Operation        | Code                                    | Time |
| ---------------- | --------------------------------------- | ---- |
| Add at head      | `ll.AddFirst(x)`                        | O(1) |
| Add at tail      | `ll.AddLast(x)`                         | O(1) |
| Remove head/tail | `ll.RemoveFirst()` / `ll.RemoveLast()`  | O(1) |
| Find             | `ll.Find(x)`                            | O(n) |
| Indexed access   | none                                    | n/a  |
| `Count`          | property                                | O(1) |

**When to reach for it:** You need O(1) at both ends and do not have a node reference. In LeetCode this is almost never the right tool — `Queue<T>`, `Stack<T>`, or `List<T>` (used as a stack) usually fit better.

### 3b. The LeetCode `ListNode` — this is what you actually use

```csharp
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}
```

**Singly-linked.** Two fields: `val` and `next`. You are given the `head` and have to traverse manually.

**Core idioms**

```csharp
// Traverse
for (var node = head; node != null; node = node.next) { ... }

// Dummy head — eliminates the "is this the first node?" branch
var dummy = new ListNode();
var tail = dummy;
// ... tail.next = something; tail = tail.next; ...
return dummy.next;

// Two pointers (slow/fast) — find middle, detect cycle
var slow = head; var fast = head;
while (fast != null && fast.next != null) {
    slow = slow.next;
    fast = fast.next.next;
}
// slow is now at the middle

// Reverse a linked list — prev/curr/next triple
ListNode prev = null, curr = head;
while (curr != null) {
    var next = curr.next;  // save
    curr.next = prev;      // flip
    prev = curr;           // advance prev
    curr = next;           // advance curr
}
return prev;  // new head
```

**Problem patterns**

- **Merging two sorted lists** (see `0021_MergeTwoSortedLists`) — dummy + tail, compare both heads, take the smaller, advance.
- **Removing a node** — `prev.next = curr.next`. Need `prev` reference; dummy head makes the first-node case uniform.
- **Splicing** — order of assignments matters. Save what you will overwrite before overwriting it.

**Gotchas**

- Always check `node != null` before `node.next`.
- When splicing, save references before overwriting — otherwise you lose the rest of the list.
- LeetCode may hand you an empty list (`head == null`). Handle as the first check in most problems.

---

## When to reach for what (LeetCode lens)

| Need                                                  | Reach for                                                     |
| ----------------------------------------------------- | ------------------------------------------------------------- |
| Fixed size, random access, O(1) lookup by integer key | **Array**                                                     |
| Dynamic size, random access, building unknown-length output | **`List<T>`**                                           |
| Stack semantics (LIFO)                                | **`Stack<T>`** (or `List<T>` if you do not want the import)   |
| Queue semantics (FIFO)                                | **`Queue<T>`** — never `List<T>` for this                     |
| Deque (both ends O(1))                                | **`LinkedList<T>`** — one of its few good uses                |
| Problem hands you a `ListNode head`                   | **Manual traversal** with the patterns above                  |

---

## 4. `Stack<T>` — LIFO

**Underlying:** Internal `T[]` that grows like `List<T>` (doubles on overflow). Top of stack is the **end** of the array, so push/pop are O(1) amortized.

**Operations**

| Operation       | Code                            | Time           |
| --------------- | ------------------------------- | -------------- |
| Push            | `s.Push(x)`                     | O(1) amortized |
| Pop             | `s.Pop()`                       | O(1)           |
| Peek            | `s.Peek()`                      | O(1)           |
| Safe pop/peek   | `s.TryPop(out var x)` / `TryPeek` | O(1)         |
| `Count`         | property                        | O(1)           |
| Contains        | `s.Contains(x)`                 | O(n)           |

**Init quirk:** `new Stack<int>(new[] {1, 2, 3})` pushes in iteration order, so **3 ends up on top**. Same for `Queue<T>` — but for queue the iteration order *is* the FIFO order, so it feels natural.

**LeetCode patterns**

- **Matched-pairs / parentheses** (see `0020_ValidParentheses`) — push openers, pop and compare on closers.
- **Monotonic stack** — keep the stack sorted (increasing or decreasing) by popping anything that breaks the invariant before pushing. Used for "next greater element", "largest rectangle in histogram", "daily temperatures".
- **Iterative DFS** — replace recursion with an explicit `Stack<TNode>` to avoid stack-overflow on deep trees/graphs.

---

## 5. `Queue<T>` — FIFO

**Underlying:** Circular buffer in an internal `T[]` with head/tail indices. Both `Enqueue` and `Dequeue` are O(1).

**Operations**

| Operation     | Code                             | Time           |
| ------------- | -------------------------------- | -------------- |
| Enqueue       | `q.Enqueue(x)`                   | O(1) amortized |
| Dequeue       | `q.Dequeue()`                    | O(1)           |
| Peek          | `q.Peek()`                       | O(1)           |
| Safe variants | `q.TryDequeue(out var x)` / `TryPeek` | O(1)      |
| `Count`       | property                         | O(1)           |

**LeetCode patterns**

- **BFS** — the canonical use. Enqueue the start, loop while non-empty, dequeue, process, enqueue unvisited neighbors. See `0542_01Matrix`.
- **Level-order traversal** of a tree — `Queue<TreeNode>`; snapshot `q.Count` at the start of each level to know how many nodes belong to that level.
- **Sliding window of fixed size** — sometimes a queue of indices works, but `Deque` is usually better (and C# does not have one — use `LinkedList<T>` if you really need both ends).

**Gotcha:** `Queue<T>` is not a deque. No `EnqueueFirst` / `DequeueLast`. If you need both ends, reach for `LinkedList<T>` or maintain two stacks.

---

## 6. `PriorityQueue<TElement, TPriority>` — min-heap by default

**Underlying:** Binary heap (array-backed). Built into .NET 6+. **Min-heap by `TPriority`** unless you supply a comparer.

**Two type parameters, not one:**

- `TElement` — what you store and get back from `Dequeue`.
- `TPriority` — the key the heap orders by. Often the same as `TElement` (e.g. `PriorityQueue<int, int>`), but separating them is the main reason this API is nice — you can store a node and prioritize by distance without writing a wrapper struct.

**Operations**

| Operation                    | Code                                                        | Time      |
| ---------------------------- | ----------------------------------------------------------- | --------- |
| Enqueue                      | `pq.Enqueue(elem, priority)`                                | O(log n)  |
| Dequeue smallest             | `pq.Dequeue()`                                              | O(log n)  |
| Peek smallest                | `pq.Peek()`                                                 | O(1)      |
| Safe variants                | `pq.TryDequeue(out var e, out var p)` / `TryPeek`           | O(1)/O(log n) |
| Enqueue + dequeue in one     | `pq.EnqueueDequeue(elem, priority)`                         | O(log n)  |
| Dequeue + enqueue in one     | `pq.DequeueEnqueue(elem, priority)`                         | O(log n)  |
| `Count`                      | property                                                    | O(1)      |

**Max-heap:** pass a reversed comparer.

```csharp
var maxHeap = new PriorityQueue<int, int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
```

**Compound priority** with tuples (lexicographic):

```csharp
// Order by distance asc, then by id asc
var pq = new PriorityQueue<Node, (int dist, int id)>();
pq.Enqueue(node, (d, node.id));
```

**LeetCode patterns**

- **Top-K** — keep a heap of size K. For *K smallest*, use a **max-heap** of size K and pop when it exceeds K (the largest is on top, ready to be evicted). For *K largest*, use a min-heap symmetrically. See `0973_KClosestPointsToOrigin`.
- **Dijkstra / shortest path with weights** — `PriorityQueue<int, int>` of `(node, distance)`.
- **Merging K sorted lists** — push one head from each list, pop the smallest, push its `.next`.

**Gotchas**

- **No decrease-key.** If a node's priority improves, you re-enqueue it and skip stale entries when you pop them (`if (dist > best[node]) continue;`).
- **Not stable** — equal priorities can come out in any order. If order matters, encode a tiebreaker into the priority (tuple).
- **Never** write a comparer that returns a constant (`(x, y) => 1`) — it violates the comparer contract and breaks the heap silently.

---

## 7. `HashSet<T>` — unordered uniqueness

**Underlying:** Hash table. O(1) average for the three operations you care about.

**Operations**

| Operation | Code                | Time         |
| --------- | ------------------- | ------------ |
| Add       | `set.Add(x)`        | O(1) average |
| Contains  | `set.Contains(x)`   | O(1) average |
| Remove    | `set.Remove(x)`     | O(1) average |
| `Count`   | property            | O(1)         |
| Set ops   | `UnionWith`, `IntersectWith`, `ExceptWith` | O(n) |

`Add` returns `bool` — `true` if the element was new, `false` if already present. Useful: `if (!seen.Add(x)) { /* duplicate */ }`.

**Custom equality:** `new HashSet<string>(StringComparer.OrdinalIgnoreCase)`. Same pattern for `Dictionary`.

**LeetCode patterns**

- **"Have I seen this?"** — duplicate detection (`0217_ContainsDuplicate`), cycle detection in linked lists, visited-set in graph traversal.
- **Set membership for O(1) lookup** — convert an array to a set so subsequent `Contains` checks are O(1). The trick behind `0128_LongestConsecutiveSequence`: build a set, then for each element that is the *start* of a run (`!set.Contains(x - 1)`), walk forward.

**Gotchas**

- For composite keys, use a **tuple** (`HashSet<(int, int)>`). Tuples implement value equality and a sensible `GetHashCode`. Do not use arrays as keys — they use reference equality.
- For your own classes as keys, override `Equals` and `GetHashCode` (or implement `IEquatable<T>`), or pass an `IEqualityComparer<T>`.

---

## 8. `Dictionary<TKey, TValue>` — the hash map

**Underlying:** Same hash table as `HashSet<T>`. The single most useful collection in LeetCode after arrays.

**Operations**

| Operation                | Code                                            | Time         |
| ------------------------ | ----------------------------------------------- | ------------ |
| Insert / overwrite       | `d[k] = v`                                      | O(1) average |
| Add (throws if exists)   | `d.Add(k, v)`                                   | O(1) average |
| Add if absent            | `d.TryAdd(k, v)`                                | O(1) average |
| Read (throws if missing) | `d[k]`                                          | O(1) average |
| Safe read                | `d.TryGetValue(k, out var v)`                   | O(1) average |
| Default if missing       | `d.GetValueOrDefault(k, fallback)`              | O(1) average |
| ContainsKey              | `d.ContainsKey(k)`                              | O(1) average |
| ContainsValue            | `d.ContainsValue(v)`                            | **O(n)**     |
| Remove                   | `d.Remove(k)`                                   | O(1) average |
| Iterate                  | `foreach (var kvp in d) { kvp.Key; kvp.Value; }`| O(n)         |

**Prefer `TryGetValue` over `ContainsKey` + indexer** — one hash lookup instead of two.

```csharp
if (d.TryGetValue(k, out var v)) { /* use v */ }
```

**Counter idiom** (frequency map):

```csharp
counts[ch] = counts.GetValueOrDefault(ch, 0) + 1;
// or:
counts.TryGetValue(ch, out var c);
counts[ch] = c + 1;
```

**Group-by idiom** (`Dictionary<TKey, List<TValue>>`):

```csharp
if (!groups.TryGetValue(key, out var bucket)) {
    bucket = new List<int>();
    groups[key] = bucket;
}
bucket.Add(value);
```

**LeetCode patterns**

- **Two Sum family** (`0001_TwoSum`) — store `value -> index`, then for each `x` look up `target - x`.
- **Anagram / frequency comparison** (`0242_ValidAnagram`) — for ASCII-lowercase, prefer `int[26]` over a dictionary; for arbitrary Unicode, use `Dictionary<char, int>`.
- **Memoization** in DP — `Dictionary<TState, TResult>` when state is not array-indexable.
- **Adjacency list** — `Dictionary<int, List<int>>` when node ids are not dense; otherwise `List<int>[]`.

**Gotchas**

- Iteration order is **insertion order** in modern .NET, but treat it as **unspecified** for correctness — never rely on it.
- Reading a missing key with `d[k]` throws `KeyNotFoundException`. This trips people coming from Python (`dict[k]` returning `None`-ish) — there is no such fallback; use `TryGetValue` or `GetValueOrDefault`.
- Mutating a dictionary during `foreach` throws. Snapshot the keys first: `foreach (var k in d.Keys.ToList()) { ... }`.

---

## 9. `SortedDictionary<TKey,TValue>` and `SortedSet<T>` — ordered, tree-backed

**Underlying:** Red-black tree. Everything is O(log n), but you get **ordered iteration** and range queries.

| Operation                     | `SortedSet<T>`              | `SortedDictionary<K,V>`         | Time      |
| ----------------------------- | --------------------------- | ------------------------------- | --------- |
| Add / Remove                  | `Add` / `Remove`            | `Add` / `Remove`                | O(log n)  |
| Contains / lookup             | `Contains`                  | `ContainsKey` / `TryGetValue`   | O(log n)  |
| Min / Max                     | `s.Min`, `s.Max`            | `d.Keys.First()` / `Last()` (O(log n) via tree, but awkward) | O(log n) |
| Range                         | `s.GetViewBetween(lo, hi)`  | n/a directly                    | O(log n) per traversal step |
| In-order iteration            | `foreach (var x in s)`      | `foreach (var kvp in d)`        | O(n)      |

**When you actually need these:** when `Dictionary` / `HashSet` are not enough because you need **order**, **min/max**, or **range**. If you only need lookup, the hashed versions are faster (O(1) vs O(log n)) and use less memory.

**LeetCode patterns**

- **Sliding-window with a sorted multiset** — e.g. "find the largest value in the window ≤ x". `SortedSet<T>` is a set, not a multiset; for duplicates use `SortedDictionary<int, int>` (value → count) as a poor man's multiset.
- **Calendar / interval scheduling** — keep events in a `SortedDictionary<int, int>` keyed by time.
- **Order statistics** — rarer in LeetCode; usually a heap or sort is enough.

**Gotchas**

- `SortedSet<T>` is **not** a multiset — adding an equal element returns `false` and does nothing.
- `GetViewBetween` returns a **live view**, not a copy. Mutations through the view affect the underlying set.
- Constant-comparer trap is the same as `PriorityQueue` — never `(x, y) => 1`. Use `Comparer<T>.Create((x, y) => y.CompareTo(x))` for reverse order.

---

## 10. `TreeNode` — the LeetCode binary tree

There is no built-in binary-tree class in .NET. LeetCode hands you this shape:

```csharp
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
```

Three fields, no parent pointer. You are given the `root` and traverse from there. `root` may be `null` — handle it first in almost every problem.

### The four traversal orders

**Recursive (the default — short, clear, and risks stack overflow only on pathologically deep trees):**

```csharp
void Preorder(TreeNode node) {        // root, left, right
    if (node == null) return;
    Visit(node);
    Preorder(node.left);
    Preorder(node.right);
}

void Inorder(TreeNode node) {         // left, root, right  — sorted order for a BST
    if (node == null) return;
    Inorder(node.left);
    Visit(node);
    Inorder(node.right);
}

void Postorder(TreeNode node) {       // left, right, root  — process children before parent
    if (node == null) return;
    Postorder(node.left);
    Postorder(node.right);
    Visit(node);
}
```

**Iterative DFS with `Stack<TreeNode>`** — same orders, but you control the stack:

```csharp
// Iterative preorder
var stack = new Stack<TreeNode>();
if (root != null) stack.Push(root);
while (stack.Count > 0) {
    var node = stack.Pop();
    Visit(node);
    if (node.right != null) stack.Push(node.right);  // push right first so left pops first
    if (node.left != null) stack.Push(node.left);
}
```

**BFS / level-order with `Queue<TreeNode>`** — the most common iterative pattern in LeetCode:

```csharp
var result = new List<IList<int>>();
if (root == null) return result;
var q = new Queue<TreeNode>();
q.Enqueue(root);
while (q.Count > 0) {
    int levelSize = q.Count;            // snapshot before the inner loop
    var level = new List<int>(levelSize);
    for (int i = 0; i < levelSize; i++) {
        var node = q.Dequeue();
        level.Add(node.val);
        if (node.left  != null) q.Enqueue(node.left);
        if (node.right != null) q.Enqueue(node.right);
    }
    result.Add(level);
}
```

### Patterns you'll see over and over

- **Recursive "return a thing from each subtree"** (the post-order shape). `MaxDepth`, `IsBalanced`, `Diameter`, `InvertTree`, `LowestCommonAncestor` all fit this mold:
  ```csharp
  int MaxDepth(TreeNode node) {
      if (node == null) return 0;
      return 1 + Math.Max(MaxDepth(node.left), MaxDepth(node.right));
  }
  ```
  You already have this shape in [0104_MaximumDepthOfBinaryTree.cs](LeetCode.CSharp/Algorithms/0104_MaximumDepthOfBinaryTree.cs) and [0226_InvertBinaryTree.cs](LeetCode.CSharp/Algorithms/0226_InvertBinaryTree.cs).
- **Level-order + per-level work** — right side view, level averages, zigzag. Always the `levelSize = q.Count` snapshot trick.
- **BST invariant** — left subtree values < node < right subtree values. **In-order traversal of a BST yields sorted values** — that single fact powers a lot of BST problems (validate BST, kth smallest, two-sum in BST).
- **Path problems** — pass an accumulator down (current path sum / current path list) and either return when you hit a leaf or collect at every node. Remember to backtrack (`path.RemoveAt(path.Count - 1)`) if you mutate a shared list.

### Gotchas

- **`null` checks first.** Every recursive helper starts with `if (node == null) return ...;`. Forgetting this is the #1 source of `NullReferenceException` in tree problems.
- **Recursion depth.** C# does not do tail-call elimination reliably. A 10,000-node skewed tree can blow the stack. If a problem hints at deep trees, switch to an explicit `Stack<TreeNode>`.
- **Don't confuse traversal order with problem semantics.** "Bottom-up" usually means *post-order* (children before parent). "Top-down" usually means *pre-order* (parent first, pass info down). Pick the order that matches the data flow you need.
- **Returning a list from recursion** — prefer passing a shared `List<int> result` accumulator down rather than concatenating returned lists (concatenation is O(n) per call → O(n²) total).

---

## 11. Graphs — a representation, not a type

There is no `Graph<T>` in the BCL. A "graph" in LeetCode is **nodes connected by edges**, and your first job on every graph problem is to pick the right shape for the inputs you're handed.

### Representations

| Representation         | Shape                                    | When                                                          |
| ---------------------- | ---------------------------------------- | ------------------------------------------------------------- |
| Adjacency list (array) | `List<int>[]` of length `n`              | Node IDs are `0..n-1` — the LeetCode default                  |
| Adjacency list (dict)  | `Dictionary<int, List<int>>`             | Node IDs are sparse, negative, strings, or otherwise non-dense |
| Adjacency matrix       | `bool[,]` or `int[,]` of size `n × n`    | Dense graphs, or small `n` (≤ ~500) and you need O(1) edge lookup |
| Edge list              | `int[][]` rows of `[u, v]` or `[u, v, w]`| What LeetCode usually *hands* you. Convert before traversing. |

For 95% of problems, **`List<int>[]`** is the right answer.

**Weighted edges:** store tuples — `List<(int neighbor, int weight)>[]`.

### Edge list → adjacency list

```csharp
// Given: int n, int[][] edges  (each row = [u, v], undirected)
var adj = new List<int>[n];
for (int i = 0; i < n; i++) adj[i] = new List<int>();
foreach (var e in edges) {
    adj[e[0]].Add(e[1]);
    adj[e[1]].Add(e[0]);   // both directions for undirected; omit for directed
}
```

### Grids are graphs

A 2D grid where each cell connects to its 4 neighbors is an **implicit** graph — no adjacency list needed. The neighbors function:

```csharp
int[][] dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];   // up, down, left, right
foreach (var d in dirs) {
    int nr = r + d[0], nc = c + d[1];
    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
    // visit (nr, nc)
}
```

This is the single most reused snippet in grid problems — memorize it. For 8-directional, iterate `{-1, 0, 1} × {-1, 0, 1}` and skip `(0, 0)`. See [0542_01Matrix.cs](LeetCode.CSharp/Algorithms/0542_01Matrix.cs).

### BFS template

Shortest path in **unweighted** graphs, level-by-level exploration.

```csharp
var visited = new bool[n];
var q = new Queue<int>();
q.Enqueue(start);
visited[start] = true;
while (q.Count > 0) {
    int node = q.Dequeue();
    foreach (int nei in adj[node]) {
        if (visited[nei]) continue;
        visited[nei] = true;          // mark when ENQUEUING, not when dequeuing
        q.Enqueue(nei);
    }
}
```

**Critical:** mark visited when you enqueue. Marking on dequeue lets the same node get enqueued many times before processing, blowing up the queue.

**Multi-source BFS** — enqueue *all* sources upfront, then run the same loop. Used for problems like "distance from any rotten orange" (994) or "distance from any 0" (0542).

### DFS template

```csharp
void Dfs(int node) {
    if (visited[node]) return;
    visited[node] = true;
    foreach (int nei in adj[node]) Dfs(nei);
}
```

For grids, you can skip a separate `visited` array by **mutating the grid in place** as you visit (e.g. flip `'1'` to `'0'`). Saves memory and is idiomatic for problems like `200. Number of Islands`.

### Cycle detection — directed graph

A plain `visited` flag confuses "already done" with "currently on my path." Use three states (white / gray / black):

| State | Meaning                              | Reaction          |
| ----- | ------------------------------------ | ----------------- |
| 0 (white) | Unvisited                        | Recurse           |
| 1 (gray)  | On the current DFS path          | Seeing again = **cycle** |
| 2 (black) | Fully processed, no cycle below  | Skip              |

```csharp
int[] state = new int[n];

bool HasCycle(int node) {
    if (state[node] == 1) return true;     // hit a gray ancestor → back edge
    if (state[node] == 2) return false;    // already cleared
    state[node] = 1;                        // gray BEFORE recursing
    foreach (int nei in adj[node]) {
        if (HasCycle(nei)) return true;
    }
    state[node] = 2;                        // black AFTER all descendants done
    return false;
}
```

The gray state is the new idea: it means "an ancestor of where I currently am." A directed cycle exists iff DFS ever follows an edge to a gray node (a "back edge").

### Cycle detection — undirected graph

Pass the parent and ignore the edge you came in on:

```csharp
bool HasCycleUndirected(int node, int parent) {
    visited[node] = true;
    foreach (int nei in adj[node]) {
        if (nei == parent) continue;
        if (visited[nei]) return true;
        if (HasCycleUndirected(nei, node)) return true;
    }
    return false;
}
```

Or use **Union-Find**: for each edge, if both endpoints are already in the same set, that edge closes a cycle.

### Topological sort

A linear ordering of a DAG such that for every edge `u → v`, `u` comes before `v`. Exists **iff** the graph has no cycle — topo sort and cycle detection are two sides of the same coin.

#### Option A — DFS / post-order reverse

The cycle-detection algorithm with **one extra line**:

```csharp
int[] state = new int[n];
var order = new List<int>(n);

bool Dfs(int node) {
    if (state[node] == 1) return false;    // cycle → no valid order
    if (state[node] == 2) return true;
    state[node] = 1;
    foreach (int nei in adj[node]) {
        if (!Dfs(nei)) return false;
    }
    state[node] = 2;
    order.Add(node);                        // post-order: add AFTER children
    return true;
}

for (int i = 0; i < n; i++) if (!Dfs(i)) return null;
order.Reverse();                             // post-order = reverse-topo
return order;
```

Same shape as your tree post-order in [0145_BinaryTreePostorderTraversal.cs](LeetCode.CSharp/Algorithms/0145_BinaryTreePostorderTraversal.cs), with two additions: the three-state coloring (graphs can cycle, trees can't) and the final `.Reverse()`.

#### Option B — Kahn's algorithm (BFS by in-degree)

"Peel the graph from its sources."

```csharp
int[] indeg = new int[n];
foreach (var edges in adj) foreach (int v in edges) indeg[v]++;

var q = new Queue<int>();
for (int i = 0; i < n; i++) if (indeg[i] == 0) q.Enqueue(i);

var order = new List<int>(n);
while (q.Count > 0) {
    int node = q.Dequeue();
    order.Add(node);
    foreach (int nei in adj[node]) {
        if (--indeg[nei] == 0) q.Enqueue(nei);
    }
}

return order.Count == n ? order : null;     // < n means cycle
```

Cycle detection is free: nodes in a cycle never reach in-degree 0, so they're left out of `order`.

#### Which to pick

| | DFS / post-order | Kahn's |
| --- | --- | --- |
| Code length | Shorter | Slightly longer (in-degree setup) |
| Natural output order | Sinks first (reverse needed) | Sources first |
| Stack-overflow risk on deep DAGs | Yes (use iterative if worried) | No |
| "All valid orderings?" | Hard | Easy (any in-degree-0 node can go next) |
| Identifying the cycle's nodes | Easy (the gray ones) | Harder |

For `207. Course Schedule` (just "is there an order?"), either works — DFS is shorter. For `210. Course Schedule II` (return the order), Kahn's reads more naturally.

### Patterns by problem family

| Problem family                                | Approach                                              |
| --------------------------------------------- | ----------------------------------------------------- |
| Connected components / "count islands"        | DFS or BFS from every unvisited node, count starts    |
| Shortest path, unweighted                     | BFS                                                   |
| Shortest path, weighted (non-negative)        | Dijkstra — `PriorityQueue<int, int>` of `(node, dist)`|
| Shortest path, with negative edges            | Bellman-Ford (rare in LeetCode)                       |
| Dependency order / scheduling                 | Topological sort                                      |
| Cycle exists?                                 | 3-state DFS (directed) or parent-check DFS / Union-Find (undirected) |
| Connectivity / "are these two nodes linked?"  | Union-Find                                            |
| Clone / mirror a graph                        | DFS/BFS + `Dictionary<Node, Node>` (original → clone) |
| Flood fill, regions                           | Grid DFS/BFS, often mutating in place                 |

### Gotchas

- **Mark visited on enqueue, not dequeue** (BFS). Easy to typo, blows up silently with duplicate work.
- **Directed vs undirected matters.** Cycle detection, edge-list building, and even whether a problem is solvable change based on this — read the problem statement carefully.
- **The graph may be disconnected.** Always loop `for (i = 0; i < n; i++) if (!visited[i]) ...` to seed from every component.
- **Recursion depth.** A linear chain of 10,000 nodes overflows the C# stack. For competitive limits, prefer iterative BFS or convert DFS to use an explicit `Stack<int>`.
- **In grids, the implicit graph is huge** — `rows × cols` nodes, up to 4× as many edges. O(rows × cols) is the floor; don't add `Contains` on a `List<>` inside the loop.

---

## 12. Binary Search Tree (BST) — ordering on top of `TreeNode`

A BST is a `TreeNode` (section 10) with one extra rule, the **ordering invariant**: for *every* node, all keys in its left subtree are `<` the node and all keys in its right subtree are `>` it. The catch is "every node / whole subtree" — **not** just the immediate children (that's the classic Validate-BST trap).

Two payoffs:

- **search / insert / delete are O(h)** — O(log n) when balanced, **O(n) when degenerate** (feed it sorted keys and it collapses into a linked list).
- **in-order traversal yields keys in sorted order** — the single fact behind validate, kth-smallest, successor, and range queries.

> Worked examples (Python, both forms): [`p0701_insert_into_a_binary_search_tree.py`](../LeetCode.Python/algorithms/p0701_insert_into_a_binary_search_tree.py).

### Search — O(h)

```csharp
TreeNode Search(TreeNode root, int target) {
    var node = root;
    while (node != null && node.val != target)
        node = target < node.val ? node.left : node.right;
    return node;   // null if not found
}
```

### Insert — O(h)

The new key always lands at a leaf: walk down comparing, attach where you fall off.

**Recursive ("return the subtree root"):**

```csharp
TreeNode Insert(TreeNode node, int val) {
    if (node == null) return new TreeNode(val);      // empty spot → new node
    if (val < node.val) node.left  = Insert(node.left,  val);
    else                node.right = Insert(node.right, val);
    return node;                                     // caller re-wires the child
}
```

The `null` base case *returns the new node*, and the caller's `node.left = Insert(...)` links it in — "create the node" and "attach to parent" unify, so no parent pointer is needed. O(h) time, O(h) stack.

**Iterative (look-ahead, O(1) space):**

```csharp
TreeNode Insert(TreeNode root, int val) {
    if (root == null) return new TreeNode(val);
    var p = root;
    while (true) {
        if (val < p.val) {
            if (p.left == null)  { p.left  = new TreeNode(val); return root; }
            p = p.left;
        } else {
            if (p.right == null) { p.right = new TreeNode(val); return root; }
            p = p.right;
        }
    }
}
```

The trick: check whether the next child is `null` *before* descending, and attach there — so you stop at the parent of the empty spot without tracking it. Same O(h) time, but **O(1) space** (no call stack), which matters on a degenerate tree where h = n.

### Delete — O(h), the tricky one

Three cases for the node being removed:

1. **Leaf** — detach it.
2. **One child** — splice that child up into its place.
3. **Two children** — overwrite the node's value with its **in-order successor** (smallest key in the right subtree: go right once, then left to the bottom), then delete that successor — which has at most one child, so it collapses to case 1 or 2.

### Complexity

| Op                         | Balanced  | Degenerate |
| -------------------------- | --------- | ---------- |
| search / insert / delete   | O(log n)  | O(n)       |

Shape depends on insert order. **Self-balancing variants** (AVL, red-black — and `SortedSet<T>` / `SortedDictionary<K,V>` *are* red-black trees under the hood) rotate on insert/delete to keep height O(log n). You rarely hand-roll balancing in an interview — you either reach for the framework's sorted collections or accept O(h) on a problem-provided BST.

### Problems & how the invariant pays off

- **701 Insert / 700 Search** — the templates above.
- **98 Validate BST** — recurse carrying a `(low, high)` range; *don't* just compare to immediate children (the trap).
- **230 Kth Smallest** — in-order traversal, stop at the k-th visit.
- **450 Delete Node** — the three-case delete above.
- **235 LCA of a BST** — exploit ordering: walk down; the point where the two targets split (one `<` node, one `>` node, or one *is* the node) is the LCA — O(h), no need to recurse into both sides.

### Gotchas

- **Validate ≠ immediate-children check.** A node can be greater than its parent yet still violate an *ancestor's* bound. Carry the `(low, high)` range down.
- **Degenerate trees.** Sorted input → an O(n) chain. If a problem stresses worst-case or huge n, the iterative insert (O(1) space) sidesteps the stack overflow the recursive one risks.
- **Duplicates** have no universal convention — disallow, always-one-side, or store a count. LeetCode usually guarantees distinct keys (701 does).

---

## 13. Trie (prefix tree) — a tree keyed by character path

A **trie** stores a set of strings as a tree where **each edge is a character** and **each node is the prefix spelled by the path from the root**. Words that share a prefix share the path for that prefix and only branch where they diverge — `app`, `apple`, `apply` all walk the same `a→p→p` spine, then split.

There is no built-in trie in the BCL — you hand-roll a node type. Two things live on every node:

- **children** — the outgoing edges, one per possible next character.
- **isEnd** — a `bool` marking "a complete word ends *here*," as distinct from "a node merely *exists* here." That flag is the whole reason a trie can tell the word `app` apart from `app` the prefix-of-`apple`.

Payoffs over a `HashSet<string>`:

- **Prefix queries in O(L)** (L = query length) — `startsWith`, autocomplete, "how many words begin with…". A hash set answers *exact* membership but knows nothing about prefixes.
- **Shared storage** for common prefixes — n words of length L cost O(total characters), not O(n·L) duplicated.

> Worked examples (Python — three variants: recursive, dict-sentinel, class-based): [`p0208_implement_trie_prefix_tree.py`](../LeetCode.Python/algorithms/p0208_implement_trie_prefix_tree.py).

### Node design — two representations

```csharp
// (a) Dictionary — any alphabet, sparse, the general default
public class TrieNode {
    public Dictionary<char, TrieNode> Children = new();
    public bool IsEnd;
}

// (b) Fixed array — lowercase a–z only, faster + cache-friendly, more memory
public class TrieNode {
    public TrieNode[] Children = new TrieNode[26];   // index = c - 'a'
    public bool IsEnd;
}
```

Pick **(a)** unless the problem pins the alphabet to lowercase letters and you want the constant-factor win — then **(b)**'s `Children[c - 'a']` indexing beats a hash lookup. The trade-off is memory: every node carries 26 slots whether used or not.

**Python contrast.** Python's idiomatic node is `children: dict[str, TrieNode]` (the dictionary form). Two Python-only shortcuts show up:

- **Node *is* a dict** — skip the class entirely; each node is a plain `dict[str, dict]` and a sentinel key (`node['#'] = True`) marks word-end. Compact, but only safe because the sentinel can't collide with a real character, and it mixes value types (child-dicts vs. the flag). The moment you want a real `bool` field, the node has to become a two-slot container — i.e. a class.
- **Slicing trap** — a recursive `insert(word[1:])` reads clean but **copies the string every level → O(L²)**. Pass an index (`insert(word, i + 1)`) or iterate to keep it O(L).

### The three operations share one walk

`insert` / `search` / `startsWith` all **walk down from the root, one character at a time.** They differ only at the ends:

```csharp
public void Insert(string word) {
    var node = root;
    foreach (var c in word) {
        if (!node.Children.TryGetValue(c, out var next)) {
            next = new TrieNode();
            node.Children[c] = next;
        }
        node = next;
    }
    node.IsEnd = true;                      // mark the terminal node
}

public bool Search(string word)       => Find(word) is { IsEnd: true };
public bool StartsWith(string prefix) => Find(prefix) is not null;

// the shared spine: walk the path, or null if any edge is missing
private TrieNode? Find(string s) {
    var node = root;
    foreach (var c in s) {
        if (!node.Children.TryGetValue(c, out var next)) return null;
        node = next;
    }
    return node;
}
```

The one idea to internalize: **`Search` and `StartsWith` are the same walk and differ only in the final check** — "did the path end on a word" (`IsEnd`) vs. "did the path exist at all" (`!= null`). `Insert` is the same walk but *creates* edges as it goes, so it can't reuse `Find`. (`TryGetValue` is the get-or-miss-in-one-lookup idiom from §8 — the C# analog of Python's `dict.get(c)`.)

The recursive form makes the symmetry even starker: all three are identical except the base case — `search` returns `node.IsEnd`, `startsWith` returns `true`, `insert` sets `node.IsEnd = true`. Iterative is the version to default to (no slicing cost, no recursion-depth ceiling); the empty string falls out for free — the loop just doesn't run, so the operation lands on the root.

### Complexity

| Op (word/prefix length L) | Time | Space (beyond storage) |
| ------------------------- | ---- | ---------------------- |
| insert / search / startsWith | O(L) | O(1) iterative · O(L) recursive (call stack) |

Storage is O(total characters across all inserted words), shared on common prefixes. The dictionary node costs memory proportional to actual branching; the `[26]` node costs 26 slots per node regardless.

### Problems & how the structure pays off

- **208 Implement Trie** — the three ops above; the canonical introduction.
- **211 Add and Search Word** — `search` gains a `.` wildcard. At a `.` you can't pick one edge, so `search` **branches into a DFS** over *all* children. The first problem where the walk stops being a straight line.
- **212 Word Search II** — build a trie of the target words, then DFS the grid once, pruning a branch the instant its prefix leaves the trie. Turns "search the grid for each of k words" into one shared traversal.
- **1268 Search Suggestions System** — autocomplete: after each typed character, descend one node and emit the (≤3) lexicographically smallest completions below it.
- **648 Replace Words** — insert dictionary roots, then for each word walk until you hit an `IsEnd` node — the shortest matching root.

### Gotchas

- **`IsEnd` ≠ "node exists."** Drop the flag and `search` collapses into `startsWith` — every prefix reports as a word. The flag is the entire point.
- **Python slicing.** `word[1:]` in a recursive trie is O(L) per call → O(L²) total. Pass an index or iterate.
- **Recursion depth.** A recursive trie recurses to depth L; Python's ~1000 default limit can bite on long words (208 allows length 2000). The iterative form has no ceiling.
- **Sentinel collisions** (dict-as-node trick). `'#'` only works as the end-marker because the input alphabet excludes it. For an arbitrary alphabet, use a real `bool` field (a class), not a magic key.
- **Memory.** The `[26]`-array node is fast but wasteful on sparse data (most slots null). Prefer the dictionary node unless the alphabet is small and dense.

---

## 14. Union-Find (DSU) — disjoint sets with near-O(1) merge and connectivity

A **union-find** (a.k.a. **disjoint-set union**, DSU) maintains a partition of `{0..n-1}` into disjoint sets and answers two questions fast, as merges stream in:

- **`find(x)`** — which set is `x` in? Returns the set's **representative** (the root of `x`'s tree).
- **`union(x, y)`** — merge the two sets containing `x` and `y`.

The structure is a **forest**: every element points to a `parent`, and a root (a node whose parent is itself) names the set. "Are `x` and `y` connected?" is just `find(x) == find(y)`. With the two optimizations below, both ops run in **amortized ~O(α(n))** — inverse Ackermann, ≤ 4 for any n you'll ever meet, i.e. effectively constant.

What it's *for*, and what a plain graph can't do as cheaply:

- **Incremental connectivity** — answer "connected?" / "merge" as edges arrive, with no re-traversal. A graph + BFS/DFS recomputes reachability per query; DSU folds each edge in once.
- **Component count / sizes** in one pass — keep a `count` (decremented per merge) and a `size[]` per root.
- **Undirected cycle detection** — an edge whose endpoints **already share a root** closes a cycle (684).
- It is the engine of **Kruskal's MST**.

What it *can't* do: it only **merges** — there is no efficient un-union / split / delete — and it tracks set *membership*, not the actual paths or edges between members.

> Worked example (Python — union-by-size solve; plus a `UnionFind` class cataloguing the four `find` variants in `program.py §20`): [`p0547_number_of_provinces.py`](../LeetCode.Python/algorithms/p0547_number_of_provinces.py).

### Representation — two arrays

```csharp
int[] parent;   // parent[i] == i  ⟺  i is a root (its own set's representative)
int[] size;     // size[root] = node count in that tree   (union by size)
// or:  int[] rank;   // rank[root] = an UPPER BOUND on tree height (union by rank)
int count;      // number of disjoint sets (optional — handy for "# of components")

void Init(int n) {
    parent = new int[n];
    size   = new int[n];
    for (int i = 0; i < n; i++) { parent[i] = i; size[i] = 1; }
    count = n;
}
```

Each element starts in its own singleton set: `parent[i] = i`, `size = 1`, `count = n`.

### `find` — with path compression

`find` walks parent-pointers to the root. **Path compression** flattens the tree on the way so later `find`s are cheap. Three variants, all correct, all the same amortized bound:

```csharp
// Path HALVING — single pass, O(1) space — the practical default
int Find(int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];   // point x at its grandparent
        x = parent[x];
    }
    return x;
}

// FULL compression (recursive) — flattens completely, but two passes:
// descend to the root, then re-point every node on the unwind (O(path) stack)
int FindFull(int x) => parent[x] == x ? x : (parent[x] = FindFull(parent[x]));
```

The idea to internalize: **full compression fundamentally needs two passes** — you can't point a node at the root until you've *found* the root, and you only find it by walking up. The recursive one-liner *looks* like one pass but pays the second in its call-stack unwind. **Path halving and path splitting are genuinely single-pass, O(1) space, and hit the same α(n)** — so full compression is never required; halving is the one to default to.

### `union` — by size (or by rank)

Always link the **roots**, and hang the **smaller tree under the larger** so depth grows slowly:

```csharp
void Union(int a, int b) {
    int ra = Find(a), rb = Find(b);
    if (ra == rb) return;                            // already together — do nothing
    if (size[ra] < size[rb]) (ra, rb) = (rb, ra);    // ra = the bigger root
    parent[rb] = ra;
    size[ra] += size[rb];
    count--;                                         // one real merge → one fewer set
}
```

Union **by rank** is the classic alternative — identical except it compares `rank` and, only when the two ranks tie, bumps the survivor's rank by 1:

```csharp
if      (rank[ra] < rank[rb]) parent[ra] = rb;
else if (rank[ra] > rank[rb]) parent[rb] = ra;
else  { parent[rb] = ra; rank[ra]++; }
```

### Rank vs. size — why size is the cleaner default

`rank` is an **upper bound on height**, not the height itself. Without path compression `rank` *equals* the true height; the moment compression runs, `find` shrinks real heights but `union` only ever *increments* rank — so **rank becomes a stale over-estimate**. It's harmless (still a valid bound for the balancing decision, and the α(n) analysis is stated in terms of rank), but it's a quantity you can't fully trust.

`size` has no such drift: path compression re-points nodes but never changes how many are in a tree, so **`size[root]` is always exact** — and it answers "how big is `x`'s group?" for free (1319, largest-component problems). Default to **union by size**; keep rank in your pocket to explain *why* it isn't the true height.

### Complexity

| Optimizations | `find` / `union` amortized |
| ------------- | -------------------------- |
| Path compression **+** union by size/rank | **O(α(n))** — effectively O(1) |
| Only one of the two | O(log n) |
| Neither | O(n) — the tree degrades to a chain |

Space is O(n) for the array(s). `α(n)` is the inverse Ackermann function (≤ 4 for all practical n).

### Problems & how the structure pays off

- **547 Number of Provinces** — union connected cities, return the component `count`. The canonical introduction (over an adjacency matrix).
- **323 Number of Connected Components** — same idea over an edge list instead of a matrix.
- **684 Redundant Connection** — process edges; the **first edge whose endpoints already share a root** is the cycle-closing one to return.
- **1319 Make Network Connected** — answer is `count − 1` (cables to link the remaining components) provided you have at least that many spare edges; `count` falls straight out of DSU.
- **990 Satisfiability of Equality Equations** — union all the `==` pairs first, then verify no `!=` pair shares a root.
- **200 Number of Islands** — grid connectivity; DSU is the alternative to BFS/DFS flood fill (union each land cell with its right/down land neighbors).
- **Kruskal's MST** — sort edges by weight, union greedily, skip any edge whose endpoints already share a root (it would form a cycle).

### Gotchas

- **Union the roots, not the raw nodes.** `parent[Find(a)] = Find(b)`, never `parent[a] = b` — the latter corrupts the forest.
- **Decrement `count` only on a real merge** — inside the `ra != rb` check. Bumping it unconditionally (or forgetting it) miscounts components. *(This was the one-line omission in the first `program.py` `union`.)*
- **No optimization → O(n).** Skip *both* compression and balancing and a chain of unions builds a linked list; `find` goes linear. Use at least one, ideally both.
- **`rank` isn't the true height** after compression — upper bound only. `size` stays exact; prefer it when you need real counts.
- **Read `rank`/`size` only at a root.** Non-root entries freeze at whatever they were when the node was last a root — stale everywhere else.
- **Merges only.** DSU has no efficient split/delete and doesn't remember edges — it answers "same set?", not "what path connects them?".
- **Indexing.** If the problem labels nodes `1..n`, size the arrays `n + 1` (or map down by one), or you'll index out of range / waste slot 0.

**Python contrast.** `parent = list(range(n))`, `size = [1] * n` — the `list(range(n))` idiom *is* the init loop. Two choices specific to Python:

- **Closure helper vs. a class.** For a one-off solve, a nested `def find(x)` that **closes over `parent`** (no need to pass it) is idiomatic — capture the fixed state, pass only what varies (`x`). For reuse across problems, promote to a `class UnionFind` with `self.parent` / `self.size`; instance attributes dissolve the where-does-the-helper-go and `nonlocal` questions at once.
- **`nonlocal` for the counter.** If `union` is a *nested* helper that rebinds an `int` component-counter, you need `nonlocal count` (rebinding a captured immutable). Sidestep it by decrementing in the driver loop or returning from a pure helper — but don't reach for the `count = [0]` list-wrap hack; `nonlocal` reads better. Mutating `parent`/`size` (a list) never needs it.

---

## 15. `Span<T>` / `stackalloc` — zero-allocation windows over memory

`Span<T>` is **not a collection** — it's a **`(pointer, length)` view** over contiguous memory you already have. It owns nothing and copies nothing; slicing it is O(1) (a new offset + length). It's the .NET tool for **touching part of an array or string without allocating a copy**.

It can wrap, uniformly:

- a managed array — `arr.AsSpan()`
- a slice of a string — `s.AsSpan(start, len)` → `ReadOnlySpan<char>`
- stack memory — `stackalloc int[26]`
- unmanaged / native memory

> Worked examples (C#): zero-alloc version parsing via `ReadOnlySpan<char>` — [`0165_CompareVersionNumbers.cs`](../LeetCode.CSharp/Algorithms/0165_CompareVersionNumbers.cs); a `stackalloc int[26]` frequency map — [`0242_ValidAnagram.cs`](../LeetCode.CSharp/Algorithms/0242_ValidAnagram.cs) (`IsAnagram3`).

### The variants

| Type | What it is | Typical source |
| ---- | ---------- | -------------- |
| `Span<T>` | read/write window | array, `stackalloc` |
| `ReadOnlySpan<T>` | read-only window | anything immutable |
| `ReadOnlySpan<char>` | the string-slicing workhorse | a `string` (implicit conversion) |
| `Memory<T>` / `ReadOnlyMemory<T>` | heap-storable cousin | when a span can't (fields, `async`) |

`string` converts to `ReadOnlySpan<char>` implicitly and for free — strings are immutable, so you only ever get the read-only span.

### Key operations

```csharp
ReadOnlySpan<char> s = "192.168.0.1";   // implicit, zero-copy
var head = s[..3];                       // "192" — O(1) slice, no allocation
var tail = s[(s.IndexOf('.') + 1)..];    // everything after the first dot
int n = int.Parse(s[..3]);               // parse straight from the window

Span<int> freq = stackalloc int[26];     // 26 ints on the STACK, zero heap
freq['c' - 'a']++;                       // index like an array
arr.AsSpan(1, 3).Reverse();              // in-place op on a subarray
```

Range syntax (`x[a..b]`, `x[a..]`, `x[..b]`) works on spans, arrays, and strings — but on an **array or string**, `arr[1..4]` *allocates a copy*, whereas on a **span**, `span[1..4]` is a free re-window. That asymmetry is the whole point: **take a span first, then slice.**

### The one rule that constrains everything — `ref struct`

`Span<T>` is a **`ref struct`**: it must live on the stack. The compiler forbids anything that could let it escape to the heap. It **cannot**:

- be a **field of a class** (only of another `ref struct`);
- be **boxed**, used as a **generic type argument**, or **captured by a lambda**;
- **survive an `await` or `yield`** — the most common real-world trip-up.

*Why:* a span can point at stack memory (`stackalloc`) or mid-object; letting it outlive its stack frame, or cross an async resume, would dangle. If you need to store a slice on the heap or hold it across `await`, use **`Memory<T>`** (heap-safe) and call **`.Span`** only at the point of use.

The safe everyday pattern: **create, use, discard within one stack frame** — slice it, parse/scan it, let it die. Both worked examples do exactly this; the span never escapes.

### `stackalloc` — the zero-heap fixed buffer

`Span<int> freq = stackalloc int[26];` carves a small buffer out of the **current stack frame** — no GC allocation, reclaimed when the method returns. Ideal for small fixed-size scratch (a 26-letter histogram, a 128-entry ASCII table). **Keep it small and never `stackalloc` in a loop** — the stack is ~1 MB and isn't freed until the method exits, so a large or repeated `stackalloc` risks a stack overflow. Rule of thumb: only for small, compile-time-bounded sizes.

### Complexity / allocation

| Approach | Slice / parse a substring | Heap allocation |
| -------- | ------------------------- | --------------- |
| `Substring` + `int.Parse(string)` | O(len) copy each time | **yes** — one string per slice |
| `ReadOnlySpan<char>` + `int.Parse(span)` | O(len), **no copy** | **none** |
| `new int[26]` frequency map | — | **yes** (heap array) |
| `stackalloc int[26]` | — | **none** (stack) |

Span doesn't change *time* complexity — it removes **allocations** (and the GC pressure they create). On a hot loop slicing thousands of times, that's the difference between churning the GC and not.

### Problems & where it pays off

- **165 Compare Version Numbers** — slice each dot-separated revision as `ReadOnlySpan<char>` and `int.Parse` it; zero `Substring` allocations.
- **242 Valid Anagram** — `stackalloc int[26]` frequency map; zero-heap counting (the third variant, vs `Dictionary` and a heap `int[26]`).
- **8 String to Integer (atoi), 71 Simplify Path** — span-based scanning / parsing without building intermediate strings.
- **Sliding window over a string** — carry a `ReadOnlySpan<char>` window instead of repeated `Substring`.

### Gotchas

- **`ref struct` rules** (above) — no class fields, no `async`/lambda capture, no boxing. Reach for `Memory<T>` when you hit them.
- **`stackalloc` discipline** — small and compile-time-bounded only; never in a loop. Big / looped `stackalloc` → stack overflow.
- **Ranges allocate on arrays/strings, not on spans.** `array[1..4]` copies; `array.AsSpan()[1..4]` doesn't. Span *first*, then slice.
- **A span is a view, not a guard.** A span over an array can be invalidated if the backing store is resized/replaced — don't hold one past changes to what it points at.
- **Alphabet assumptions.** A `stackalloc int[26]` histogram hard-codes `a–z` (`c - 'a'`); fine when the problem pins the alphabet, but a `Dictionary<char,int>` is the alphabet-agnostic fallback (the trade-off across 242's three variants).

**Python contrast.** Python slicing **copies** — `s[1:4]` and `lst[1:4]` both allocate. The zero-copy analogs are narrow: `memoryview` (bytes/buffers only) and NumPy array views. There's no general, type-safe "window over any list" the way `Span<T>` is the everyday default in C#. So these idioms have **no clean Python equivalent** — in Python you either take the copy or **thread indices** (`s`, `i`, `j`) to avoid it, which is the same move you already use to dodge the `word[1:]` O(L²) trap in the Trie notes (§13).

---

## When to reach for what (LeetCode lens)

| Need                                                  | Reach for                                                     |
| ----------------------------------------------------- | ------------------------------------------------------------- |
| Fixed size, random access, O(1) lookup by integer key | **Array** (or `int[26]` / `int[128]` as a tiny hash map)      |
| Dynamic size, random access, building unknown-length output | **`List<T>`**                                           |
| Stack semantics (LIFO), iterative DFS                 | **`Stack<T>`**                                                |
| Queue semantics (FIFO), BFS, level-order              | **`Queue<T>`**                                                |
| Top-K, Dijkstra, merge K sorted                       | **`PriorityQueue<TElement, TPriority>`**                      |
| Deque (both ends O(1))                                | **`LinkedList<T>`** — one of its few good uses                |
| "Have I seen this?" / dedup                           | **`HashSet<T>`**                                              |
| Key → value lookup, frequency map, memoization        | **`Dictionary<TKey, TValue>`**                                |
| Ordered iteration, min/max, range queries             | **`SortedSet<T>` / `SortedDictionary<K,V>`**                  |
| Problem hands you a `ListNode head`                   | **Manual traversal** — dummy head, two pointers, prev/curr/next |
| Problem hands you a `TreeNode root`                   | **Recursion** (post-order shape) or **`Queue<TreeNode>`** for BFS |
| Problem hands you `int n` + `int[][] edges`           | Build `List<int>[]` adjacency list, then BFS / DFS / topo sort |
| Grid problem (`char[][]` / `int[][]`)                 | Implicit graph — use the 4-direction `dirs` array, mutate in place to mark visited |
| Prefix queries, autocomplete, many words sharing prefixes | **Trie** — `TrieNode` with `Dictionary<char, TrieNode>` (or `TrieNode[26]`) + `IsEnd` |
| Dynamic connectivity, merge sets, count components, undirected cycle detection | **Union-Find (DSU)** — `int[] parent` + `int[] size`, path-compressed `Find`, union by size |
| Slice/parse part of an array or string without allocating; small fixed scratch buffer | **`Span<T>` / `ReadOnlySpan<char>`** (zero-copy window) · **`stackalloc int[26]`** (zero-heap buffer) |

---

## Up next (when ready)

- **`StringBuilder`** — O(1) amortized append vs O(n) per `string +`; the mutable-buffer counterpart to `Span<T>` for *building* strings. (The last performance-tools item; the data-structure walk itself is now complete — §1–15.)
