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

## Up next (when ready)

Next layers after this foundation:

- **Hashing:** `HashSet<T>`, `Dictionary<TKey, TValue>` — O(1) average lookup, the engine behind most "is this a duplicate / have I seen this before" patterns.
- **Specialized linear:** `Stack<T>`, `Queue<T>`, `PriorityQueue<TElement, TPriority>` (built-in since .NET 6).
- **Trees and ordered sets:** `SortedDictionary<TKey, TValue>`, `SortedSet<T>` (red-black tree under the hood — O(log n) ops with ordered iteration).
- **Custom structures for problems:** binary trees (`TreeNode` LeetCode pattern), tries, union-find, graphs (adjacency list via `Dictionary<int, List<int>>` or `List<int>[]`).
