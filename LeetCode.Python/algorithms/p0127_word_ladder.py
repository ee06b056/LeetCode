from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        buckets_map = defaultdict(list)
        for w in wordList:
            buckets_list = self.get_buckets(w)
            for b in buckets_list:
                buckets_map[b].append(w)
        count = 0
        l = [beginWord]
        visited = set()
        while l:
            count += 1
            l2 = []
            for w in l:
                bl = self.get_buckets(w)
                for b in bl:
                    if b not in visited:
                        visited.add(b)
                        for nw in buckets_map.get(b, []):
                            if nw == endWord:
                                return count + 1
                            l2.append(nw)
            l = l2
        return 0
    
    def get_buckets(self, word: str) -> list[str]:
        bucket_list = []
        for i in range(len(word)):
            bucket_list.append(word[:i] + "*" + word[i + 1:])
        return bucket_list
