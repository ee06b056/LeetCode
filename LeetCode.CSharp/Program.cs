using System;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;

namespace LeetCode.CSharp;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
        Console.WriteLine('a' - 0);
        int increInt = 1;
        Console.WriteLine(increInt++);


        // Tuple
        (string name, int age) person1 = ("Alice", 30);
        person1.name = "Bob";
        var t1 = (1, 2);
        var t2 = (x: 1, y: 2);
        (int x, int y) t3 = (1, 2);
        var t4 = (name: "Alice", age: 30, isAdmin: true);
        var tupleSet = new HashSet<(int, int)>();
        tupleSet.Add((1, 2));
        var tupleDict = new Dictionary<(int, int), string>();
        tupleDict[(1, 2)] = "Hi";
        tupleSet.Add(t1);
        tupleSet.Add(t2);
        tupleSet.Add(t3);
        var name1 = t4.name;
        
        // Array
        var stringArray = new string[5];
        int[] intArray = {2, 1, 3};
        int[] intArray2 =  [..intArray, 2, 3];
        int[] numbers = new int[6];
        var numbers2 = new int[6];
        int[] numebers3 = new int[6] {1,2,3,4,5,6};
        var numerbers4 = new int[6] {1,2,3,4,5,6};
        int[] numbers5 = new int[] {1,2,3,4,5,6};
        var numbers6 = new int[] {1,2,3,4,5};
        int[] numbers7 = new int[4];
        int[,] grid1 = new int[2,3] {{1,2,3}, {4,5,6}};
        var grid2 = new int[2,3] {{1,2,3}, {4,5,6}};
        int[,] grid3 = {{1,2,3}, {4,5,6}, {3, 4, 5}};
        int[][] grid4 = [[1, 2, 3], [4, 5, 6], [3, 4, 5]];
        int[][] grid5 = new int[3][];
        for (int i = 0; i < grid5.Length; i++) grid5[i] = new int[4];
        // allays use int[][] jagged in leetcode

        Array.Sort(grid4, (a, b) => a[0].CompareTo(b[0]));

        Console.WriteLine(string.Join(", ", intArray));
        Array.Sort(intArray);
        Console.WriteLine(string.Join(", ", intArray));

        // List
        // in C#, List is in System.Collections.Generic namespace, and it's a dynamic array, not a linked list
        List<int> list1 = new List<int>();
        //List<int> list2 = new ArrayList
        // never use ArrayList in C#, it's not type safe and it's not generic, use List<T> instead
        List<int> list2 = [];
        List<int> list3 = new();
        List<int> list4 = new() {1, 2, 3, 4};
        List<int> list5 = new() {1, 2, 4, 5};
        list1.Add(1);
        list1.IndexOf(0);
        list1.AddRange(new int[] {2, 3, 4});
        list1.AddRange(list4);
        list1.Insert(2, 4);
        list1.Sort();

        // LinkedList
        // in C#, LinkedList is in System.Collections.Generic namespace, and it's a doubly linked list, not a singly linked list
        // method return linked list node, not the linked list itself, so we need to use LinkedListNode<T> to get the value of the node
        // linked list node has properties Value, Next, Previous, and methods AddBefore, AddAfter, AddFirst, AddLast, Remove, RemoveFirst, RemoveLast
        // LinkedList canbe used as deque because c# doesn't have a build-in, for stack and queue, we can use Stack<T> and Queue<T> in System.Collections.Generic namespace
        LinkedList<int> linkedList1 = new LinkedList<int>();
        LinkedList<int> linkedList2 = new LinkedList<int>(new int[] {1, 2, 3, 4});
        linkedList1.AddLast(1);
        linkedList1.AddFirst(2);
        linkedList1.RemoveFirst();
        linkedList1.RemoveLast();
        int llCount = linkedList1.Count;

        // Stack
        Stack<int> stack1 = new();
        Stack<int> stack2 = new Stack<int>();
        Stack<int> stack3 = new(6);
        Stack<int> stack4 = new(capacity: 6);
        Stack<int> stack5 = new(new int[] {1, 2, 3, 4, 5});
        stack1.Push(1);
        stack1.Peek();
        stack1.Pop();
        int count = stack1.Count;

        // Queue
        Queue<int> queue1 = new();
        Queue<int> queue2 = new Queue<int>();
        Queue<int> queue3 = new(6);
        Queue<int> queue4 = new(capacity: 6);
        Queue<int> queue5 = new(new int[] {1, 2, 3});
        queue1.Enqueue(1);
        queue1.Enqueue(2);
        queue1.Enqueue(2);
        queue1.Enqueue(2);
        queue1.Peek();
        queue1.Dequeue();
        queue1.TryDequeue(out int result);
        queue1.TryPeek(out int result2);
        count = queue1.Count;

        // PriorityQueue
        PriorityQueue<int, int> pq1 = new();
        PriorityQueue<int, int> pq2 = new PriorityQueue<int, int>();
        var pq3 = new PriorityQueue<int, int>(Comparer<int>.Create((x, y) => y.CompareTo(x)));
        var pq4 = new PriorityQueue<int, (int, int)>(Comparer<(int first, int second)>.Create((x, y) => y.first.CompareTo(x.Item1)));
        var pq5 = new PriorityQueue<int, int>(Comparer<int>.Create((x, y) => 1));  // Never use this, it's not a valid comparer
        pq1.Enqueue(1, 1);
        pq1.Enqueue(1, 1);
        pq1.Enqueue(1, 1);
        pq1.Enqueue(1, 1);
        pq1.Dequeue();
        pq1.Peek();
        pq1.TryDequeue(out int pqresult, out int pqpriority);
        pq1.TryPeek(out int pqresult2, out int pqpriority2);
        count = pq1.Count;
        pq1.EnqueueDequeue(1, 1);
        pq1.DequeueEnqueue(1, 1);

        // HashSet
        HashSet<int> hashSet1 = new();
        HashSet<int> hashSet2 = new HashSet<int>();
        HashSet<int> hashSet3 = new HashSet<int>(9);
        var hashSet4 = new HashSet<int>(capacity: 10);
        var hashSet5 = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
        hashSet1.Add(1);
        hashSet1.Contains(1);
        hashSet1.Remove(1);
        count = hashSet1.Count;
    }
}
