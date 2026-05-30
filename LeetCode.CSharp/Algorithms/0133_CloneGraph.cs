using System.Collections.Generic;

namespace LeetCode.CSharp.Algorithms;

public class _0133_CloneGraph
{
    public class Node {
        public int val;
        public IList<Node> neighbors;

        public Node() {
            val = 0;
            neighbors = new List<Node>();
        }

        public Node(int _val) {
            val = _val;
            neighbors = new List<Node>();
        }

        public Node(int _val, List<Node> _neighbors) {
            val = _val;
            neighbors = _neighbors;
        }
    }

    public Node CloneGraph(Node node)
    {
        if (node == null) return null;
        var nodeDict = new Dictionary<int, Node>();
        var nodeQ = new Queue<Node>();
        var startNode = new Node(node.val);
        nodeQ.Enqueue(node);
        nodeDict.Add(node.val, startNode);
        while (nodeQ.Count > 0)
        {
            var currentNode = nodeQ.Dequeue();
            var newCurrentNode = nodeDict[currentNode.val];
            foreach (var nextNode in currentNode.neighbors)
            {
                if (!nodeDict.TryGetValue(nextNode.val, out var newNextNode))
                {
                    newNextNode = new Node(nextNode.val);
                    nodeDict[nextNode.val] = newNextNode;
                    nodeQ.Enqueue(nextNode);
                }
                newCurrentNode.neighbors.Add(newNextNode);
            }
        }
        return nodeDict[node.val];
    }
}
