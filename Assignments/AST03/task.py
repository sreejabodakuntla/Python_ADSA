
i
def count_good_substrings(s):
    count = 0

    for i in range(len(s) - 2):
        a, b, c = s[i], s[i + 1], s[i + 2]

        if a != b and b != c and a != c:
            count += 1

    return count


s = input()
print(count_good_substrings(s))