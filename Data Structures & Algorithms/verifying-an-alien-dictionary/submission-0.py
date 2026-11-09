class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = {}
        for i,ch in enumerate(order):
            dict[ch] = i
        for index in range(len(words) - 1):
            word1, word2 = words[index], words[index+1]
            for i, j in zip(word1, word2):
                if dict[i] < dict[j]:
                    break
                elif dict[i] > dict[j]:
                    return False
                elif dict[i] == dict[j]:
                    continue
            else:
                if len(word2) < len(word1):
                    return False
        return True