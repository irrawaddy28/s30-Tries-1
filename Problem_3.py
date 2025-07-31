'''
648 Replace Words
https://leetcode.com/problems/replace-words/description/

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"


Constraints:
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.

Solution:
1. Build a trie from the words in the wordlist. Then this becomes the trie of root words. For each word in the sentence, feed the word into the trie. Check for the existence of the shortest prefix of the word in the trie. If so, return that prefix. If not, we use the word from the sentence.

Let M = no. of words in the dictionary
    K = avg len of words in the dictionary
    N = no. of words in the sentence
    W = avg len of words in the sentence
https://www.youtube.com/watch?v=yIY-cPhVGIo

Time: O(MK + NW + NK), Space: O(MK + NW)
'''
from trie import *

def replaceWords(dictionary, sentence):
    def get_root(t, word): #O(C), C=no. of characters in word
        curr = t
        path=""
        for c in word:
            if not curr.children[c]: # no child 'c'
                return ""
            path += c
            if curr.children[c].isEOS:
                return path
            curr = curr.children[c]
        return "" # prefix found but no EOS at the end of prefix

    if not sentence:
        return ""

    t = Trie()
    for word in dictionary:
        t.insert(word) # O(MK)

    result = []
    words = sentence.split() #Time: O(NW), Space: O(NW)
    for word in words: # (N)
        root = get_root(t.root, word) # O(K)
        if not root:
            result.append(word)
        else:
            result.append(root)

    return " ".join(result)

def run_replaceWords():
    tests = [(["cat","bat","rat"],
              "the cattle was rattled by the battery",
              "the cat was rat by the bat"
             ),
             (["cat","bat","rat"],
               "the cattle was rattled by the battery ba",
               "the cat was rat by the bat ba",
             ),
             (["cat","bat","rat",'b'],
              "the cattle was rattled by the battery",
              "the cat was rat b the b",
             ),
             (["a","b","c"],
              "aadsfasf absbs bbab cadsfafs",
               "a a b c",
             ),
            ]
    for test in tests:
        dictionary, sentence, ans = test[0], test[1], test[2]
        new_sentence = replaceWords(dictionary, sentence)
        print(f"\nDictionary = {dictionary}")
        print(f"Sentence = {sentence}")
        print(f"New Sentence = {new_sentence}")
        success = (ans == new_sentence)
        print(f"Pass: {success}")
        if not success:
            break

run_replaceWords()