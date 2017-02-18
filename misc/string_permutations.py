"""
Compute String Permutations
"""


def main(in_str):
    used = [False] * len(in_str)
    return permute(in_str, used, "")


def permute(in_str, used, out_str):
    if len(out_str) == len(in_str):
        print(out_str)
        return

    for i, char in enumerate(in_str):
        print(i, used, char, out_str)
        if used[i]:
            continue
        out_str += char
        used[i] = True
        permute(in_str, used, out_str)
        used[i] = False
        out_str = out_str[:-1]
