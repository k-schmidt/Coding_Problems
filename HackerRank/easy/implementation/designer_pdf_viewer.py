"""
Consider a word consisting of lowercase English alphabetic letters,
where each letter is wide.
Given the height of each letter in millimeters (),
find the total area that will be highlighted by blue rectangle in
when the given word is selected in our new PDF viewer.

Input Format
The first line contains space-separated integers describing the
respective heights of each consecutive lowercase English letter (i.e., ).
The second line contains a single word, consisting of lowercase
English alphabetic letters.

Output Format
Print a single integer denoting the area of highlighted rectangle
when the given word is selected.
The unit of measurement for this is square millimeters (),
but you must only print the integer.
"""


def main(height_list, word):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                "w", "x", "y", "z"]
    alphabet_dict = dict(zip(alphabet, height_list))
    mx = max([alphabet_dict[char] for char in word])
    return mx * len(word)

# Other Solution
h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()
print(len(word) * max(h[ord(l)-ord('a')] for l in word))
