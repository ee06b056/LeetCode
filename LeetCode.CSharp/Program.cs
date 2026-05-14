using System;
using System.Collections;
using System.Collections.Generic;

namespace LeetCode.CSharp;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");

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
        linkedList1.RemoveFirst();
        linkedList1.RemoveLast();
        int llCount = linkedList1.Count;
    }
}
