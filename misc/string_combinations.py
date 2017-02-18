"""
Print combinations of a given string
"""


def combine(in_str, start, out_str):
    while start < len(in_str):
        out_str += in_str[start]
        print(out_str)
        if start < len(in_str):
            combine(in_str, start + 1, out_str)
        out_str = out_str[:-1]
        start += 1


def combine_opto(in_str, start, out_str):
    while start < len(in_str):
        out_str += in_str[start]
        print(out_str)
        combine(in_str, start + 1, out_str)
        start += 1
    out_str = out_str[:-1]
    print(out_str)
    out_str = out_str[:-1]


def main(in_str):
    return combine(in_str, 0, "")


def main_opto(in_str):
    return combine(in_str, 0, "")
