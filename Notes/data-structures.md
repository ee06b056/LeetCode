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

---

## Up next (when ready)

- **Graphs:** adjacency list as `Dictionary<int, List<int>>` or `List<int>[]`. BFS/DFS templates, visited sets, cycle detection.
- **Trie:** custom class with `Dictionary<char, TrieNode>` (or `TrieNode[26]` for lowercase) + `isEnd` flag. Prefix search, autocomplete.
- **Union-Find (DSU):** `int[] parent`, `int[] rank`, with path-compressed `Find` and union-by-rank `Union`. Connectivity, Kruskal's MST, redundant-connection problems.
- **Performance tools:** `Span<T>` / `ReadOnlySpan<char>` for zero-allocation slicing, `StringBuilder` for repeated concatenation.
