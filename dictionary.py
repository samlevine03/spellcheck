from settings import SUGGEST_THRESHOLD, DICT_SIZE

MAX_DICT_SIZE = 70961

class Dictionary:
    def __init__(self):
        self.ordered_dict = self._build_dict()
        self.dict = set(self.ordered_dict)
        self.word_rank = {word: i for i, word in enumerate(self.ordered_dict)}

    def _build_dict(self, size=DICT_SIZE) -> list:
        with open('words.txt', 'r') as f:
            words = [word.strip().lower() for word in f.readlines()]

        check = set()
        words = [word for word in words if word not in check and (check.add(word) or True)]
        
        if size < .01:
            size = .01
        elif size > 1.0:
            size = 1.0

        return words[:int(MAX_DICT_SIZE * size)]

    def is_word(self, word: str) -> bool:
        return word.lower() in self.dict
    
    def get_word_rank(self, word: str) -> int:
        """
        Returns the index of the word in the dictionary.
        """
        return self.word_rank.get(word, -1)

    def wagner_fischer(self, w1: str, w2: str) -> int:
        """
        Wagner-Fischer algorithm for finding the edit distance between two words.
        """
        len1, len2 = len(w1), len(w2)
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

        # set the first row and column
        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j

        # fill in the rest of the dp
        for i, char_w1 in enumerate(w1, start=1):
            for j, char_w2 in enumerate(w2, start=1):
                if char_w1 == char_w2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

        # return the bottom right corner
        return dp[-1][-1]
    
    def suggest_words(self, word: str, k=SUGGEST_THRESHOLD*MAX_DICT_SIZE) -> list:
        """
        Suggests words based on the input word.
        """
        suggestions = []
        min_dist = float('inf')
        
        for word_in_dict in self.ordered_dict:
            dist = self.wagner_fischer(word_in_dict, word)
            if dist <= min_dist:
                suggestions.append((word_in_dict, dist))
                min_dist = dist
            else:
                continue
    
        suggestions = list(filter(lambda x: x[1] == min_dist, suggestions))[:3]
        suggestions = list(filter(lambda x: self.get_word_rank(x[0]) - self.get_word_rank(suggestions[0][0]) < k, suggestions))
        return suggestions
