class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_so_far = 0
        paths = {}
        chunks = input.split('\n')
        for c in chunks:
            level = 0
            while level < len(c) and c[level] == '\t':
                level += 1
            
            path_len = len(c) if level == 0 else paths[level-1] + 1 + len(c[level:])
            
            if '.' in c:
                max_so_far = max(max_so_far, path_len)
            else:
                paths[level] = path_len
        return max_so_far