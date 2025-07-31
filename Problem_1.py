'''
208 Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/description/

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Example 1:
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output:
[null, null, true, false, true, null, true]
Explanation:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

Solution:
1. Design Trie data structure using hash map
https://youtu.be/-JJCOdLilxg?t=2088

N = no. of words in Trie
W = average length of word in the Trie

            Time        Space
Trie DS:    O(W)       O(NW)
Insert:     O(W)       O(W)
Search:     O(W)       O(1)
StartsWith: O(W)       O(1)
'''
from collections import defaultdict

class TrieNode:
        def __init__(self):
            self.children = defaultdict(str) # key = data, value = TrieNode()
            self.isEOS = False

class Trie:
    def __init__(self):
        ''' Time: O(1), Space: O(1)'''
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ''' Time: O(N), Space: O(N), N = num chars in word'''
        if not self.root:
            return None
        curr = self.root
        for c in word:
            if not curr.children[c]:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEOS = True

    def search(self, word: str) -> bool:
        ''' Time: O(N), Space: O(1), N = num chars in word'''
        if not self.root:
            return False
        curr = self.root
        for c in word:
            if not curr.children[c]:
                return False
            curr = curr.children[c]
        return curr.isEOS

    def startsWith(self, prefix: str) -> bool:
        ''' Time: O(N), Space: O(1), N = num chars in word'''
        if not self.root:
            return False
        curr = self.root
        for c in prefix:
            if not curr.children[c]:
                return False
            curr = curr.children[c]
        return True

def run_insert_search_prefix():
    t = Trie()
    words = ["apple", "ape", "no", "not", "news", "not", "never"]
    for word in words:
        t.insert(word)

    tests = [("newz", False), ("new", False), ("news", True), ("india", False)]
    for test in tests:
        word, ans = test[0], test[1]
        found = t.search(word)
        success = (ans == found)
        print(f"word = {word}, found = {found}")
        print(f"Pass: {success}")
        if not success:
            return

    print(f"\n")
    tests = [("a", True), ("ap", True), ("app", True), ("ape", True), ("appn", False)]
    for test in tests:
        prefix, ans = test[0], test[1]
        is_prefix = t.startsWith(prefix)
        success = (ans == is_prefix)
        print(f"is_prefix({prefix}) = {is_prefix}")
        print(f"Pass: {success}")
        if not success:
            return

run_insert_search_prefix()