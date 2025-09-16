import collections
from typing import List

class Trie:
    class TrieNode(collections.defaultdict):
        def __init__(self):
            # Each node maps char -> child node; default creates child nodes on demand
            super().__init__(Trie.TrieNode)
            self.eow = False  # end-of-word flag

    def __init__(self):
        self.root = Trie.TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node[ch]
        node.eow = True

    def replace(self, word: str) -> str:
        node = self.root
        for i, ch in enumerate(word):
            if ch not in node:        # no matching path; keep original word
                return word
            node = node[ch]
            if node.eow:              # found a root/prefix
                return word[:i+1]
        return word                   # no shorter root found

class Solution:
    def replaceWords(self, prefixes: List[str], sentence: str) -> str:
        trie = Trie()
        for p in prefixes:
            trie.insert(p)
        return ' '.join(map(trie.replace, sentence.split()))
