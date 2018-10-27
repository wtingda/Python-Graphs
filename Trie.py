# Trie Class for storing and searching for words

class TrieNode(object):
    ''' Trie node class that stores children and whether this is a word '''
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)
        
class Trie:

    def __init__(self):
        # root is dummy node
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            # we fetch the child if it exists otherwise we create one using default dict
            node = node.children[c]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        # same as search except for we don't check for is_word
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
