import collections
import sys
input = sys.stdin.readline
N = int(input())

arr = [list(map(str, input().rstrip().split("\\"))) for i in range(N)]

# 트라이의 노드
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 단어 삽입
    def insert(self, words):
        node = self.root
        for s in words:
            node = node.children[s]

    # 트라이 프린트
    def search(self, node, cnt):
        a = list(node.children)
        a.sort()
        for char in a:
            print((" " * cnt) + char)
            self.search(node.children[char], cnt + 1)

trie = Trie()
for s in arr:
    trie.insert(s)
trie.search(trie.root, 0)