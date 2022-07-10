class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.ans = []
        trie_root = TrieNode()
        # Add words to the trie
        for word in words:
            current_node = trie_root
            for char in word:
                if not char in current_node.children:
                    new_node = TrieNode(char)
                    current_node.children[char] = new_node
                current_node = current_node.children[char]
            current_node.is_end = word
        
        # Start traverse the board
        row_len = len(board)
        col_len = len(board[0])
        
        def is_matched(row, col, node):
            board_char = board[row][col]
            board[row][col] = '#'
            if board_char in node.children:
                if node.children[board_char].is_end != None:
                    self.ans.append(node.children[board_char].is_end)
                    node.children[board_char].is_end = None
                for row_offset, col_offset in [(-1,0), (1,0), (0,-1), (0,1)]:
                    new_row = row + row_offset
                    new_col = col + col_offset
                    if new_row < 0 or new_row >= row_len or new_col < 0 or new_col >= col_len:
                        continue
                    if not board[new_row][new_col] in node.children[board_char].children:
                        continue
                    is_matched(new_row, new_col, node.children[board_char])
                # Delete the matched leaf
                if not node.children[board_char].children:
                    node.children.pop(board_char)
            
            board[row][col] = board_char
            
        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] in trie_root.children:
                    is_matched(i, j, trie_root)
        
        return self.ans
    
class TrieNode:
    def __init__(self, char=''):
        self.char = char
        self.children = {}
        self.is_end = None