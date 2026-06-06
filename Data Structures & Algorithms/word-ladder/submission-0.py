class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        new_dic = collections.defaultdict(list)
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        for word in wordList:
            for i in range(len(word)):
                new_w = word[:i] + '*' + word[i+1:]
                new_dic[new_w].append(word)
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            word, steps = queue.popleft()
            for i in range(len(word)):
                new_w = word[:i] + '*' + word[i+1:]
                for w_2 in new_dic[new_w]:
                    if w_2 == endWord:
                        return steps +1
                    if w_2 not in visited:
                        visited.add(w_2)
                        queue.append((w_2,steps+1))
                new_dic[new_w] = []
        return 0