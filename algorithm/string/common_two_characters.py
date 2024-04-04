from collections import defaultdict


def f(strings):
    prefix_table, suffix_table, common_table = defaultdict(int), defaultdict(int), defaultdict(int)
    ans = 0

    for s in strings:
        prefix, suffix = s[:2], s[-2:]
        if prefix == suffix:
            common_table[prefix] = max(common_table[prefix], len(s))
        else:
            prefix_table[prefix] = max(prefix_table[prefix], len(s))
            suffix_table[suffix] = max(suffix_table[suffix], len(s))

    for suffix, length in suffix_table.items():
        if suffix in prefix_table:
            ans = max(ans, length + prefix_table[suffix] - 2)
        if suffix in common_table:
            ans = max(ans, length + common_table[suffix] - 2)

    for suffix, length in common_table.items():
        if suffix in prefix_table:
            ans = max(ans, length + prefix_table[suffix] - 2)

    return ans


if __name__ == "__main__":
    strings = [
        "aaaa",
        "akkj",
        "kjiol",
        "cc",
        "kjkjkjkjkj"
    ]

    print(f(strings))
