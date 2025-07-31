from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(str) # key = data, value = TrieNode()
        self.isEOS = False

    def pprint(self):
        print(" +", end='')
        self._pprint()

    def _pprint(self, indent_str=""):
        needs_indent = False

        if self.isEOS:
            print(".")  # Terminate with '.'
            needs_indent = True

        for ix, (letter, curr) in enumerate(sorted(self.children.items())):
            last_child = ix == len(self.children)-1

            if needs_indent:
                print(indent_str + " +", end='')
            print('-' + letter, end='')

            child_indent = indent_str + ("  " if last_child else " |")
            curr._pprint(child_indent)
            needs_indent = True

class Trie:
    def __init__(self):
        ''' Time: O(1), Space: O(1)'''
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ''' Time: O(C), Space: O(C), C = num chars in word'''
        if not self.root:
            return None
        curr = self.root
        for c in word:
            if not curr.children[c]:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEOS = True

    def search(self, word: str) -> bool:
        ''' Time: O(C), Space: O(1), C = num chars in word'''
        if not self.root:
            return False
        curr = self.root
        for c in word:
            if not curr.children[c]:
                return False
            curr = curr.children[c]
        return curr.isEOS

    def startsWith(self, prefix: str) -> bool:
        ''' Time: O(C), Space: O(1), C = num chars in word'''
        if not self.root:
            return False
        curr = self.root
        for c in prefix:
            if not curr.children[c]:
                return False
            curr = curr.children[c]
        return True
