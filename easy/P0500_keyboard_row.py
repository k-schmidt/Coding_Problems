"""
Given a list of words, return the words that can be typed using letters of
alphabet on only one row of American keyboard.

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""

# n = list of words
# b = max char in words
# l = length of max keyboard row (10)
# First Pass O(n * b * 10) Runtime Yikes!
class Solution:

    row1 = ["z", "x", "c", "v", "b", "n", "m"]
    row2 = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
    row3 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]

    def findWords(self, words):
        one_row = []

        for word in words:
            if word in self.row1:  # O(n)
                row = self.row1
            elif word in self.row2:  # O(n)
                row = self.row2
            elif word in self.row3:  # O(n)
                row = self.row3
            else:
                continue
            i = 1
            while i < len(word):
                char = word[i]
                if char.lower() not in row:  # O(n)
                    break
                else:
                    i += 1
            if i == len(word):
                one_row.append(word)
        return one_row

# Second Pass O(n * b) Runtime
class Solution:

    row1 = {"z": True,
            "x": True,
            "c": True,
            "v": True,
            "b": True,
            "n": True,
            "m": True}
    row2 = {"a": True,
            "s": True,
            "d": True,
            "f": True,
            "g": True,
            "h": True,
            "j": True,
            "k": True,
            "l": True}
    row3 = {"q": True,
            "w": True,
            "e": True,
            "r": True,
            "t": True,
            "y": True,
            "u": True,
            "i": True,
            "o": True,
            "p": True}

    def findWords(self, words):
        one_row = []

        for word in words:
            if word in self.row1:  # O(1)
                row = self.row1
            elif word in self.row2:  # O(1)
                row = self.row2
            elif word in self.row3:  # O(1)
                row = self.row3
            else:
                continue
            i = 1
            while i < len(word):
                char = word[i]
                if char.lower() not in row:  # O(1)
                    break
                else:
                    i += 1
            if i == len(word):
                one_row.append(word)
        return one_row
