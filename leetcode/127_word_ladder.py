"""
Transform the word from begin word to endword from a list of words with only 1 letter change at a time
"""
from typing import List

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        Single-ended BFS with pre-processing
        """
        def construct_dict(word_list: set) -> dict:
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = f"{word[:i]}_{word[i + 1:]}"
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs_words(begin, end, dict_words):
            if end not in word_set:
                return 0
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = f"{word[:i]}_{word[i + 1:]}"
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps+1))
            return 0

        word_set = set(wordList)
        d = construct_dict(word_set | {beginWord, endWord})
        return bfs_words(beginWord, endWord, d)


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Double-ended BFS
        """
        if endWord not in wordList:
            return 0
        length = 1
        wordList = set(wordList)
        front, back = {beginWord}, {endWord}
        while front:
            print(front, back)
            if front & back:
                return length
            length += 1
            wordList -= front
            front = self.distance_be_1(front, wordList, beginWord)
            if len(front) > len(back):
                front, back = back, front
        return 0

    def distance_be_1(self, front, wordList, beginWord):
        return wordList & (set(word[:index] + ch + word[index + 1:] for word in front
                               for index in range(len(beginWord))
                               for ch in 'abcdefghijklmnopqrstuvwxyz'))

solution = Solution()
print(solution.ladderLength(beginWord, endWord, wordList))