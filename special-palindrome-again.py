# https://www.hackerrank.com/challenges/special-palindrome-again/problem
def substrCount(n, s):
    count = n
    for i in range(n):
        left_chars_count = 1
        right_chars_count = 0
        previous_char = s[i]
        is_middle = False

        for j in range(i + 1, n):
            if not is_middle and s[j] != previous_char:
                is_middle = True
            elif is_middle and (s[j] != previous_char or j == n - 1):
                if j == n - 1 and s[j] == previous_char:
                    right_chars_count += 1

                if left_chars_count == right_chars_count:
                    count += 1
                break
            elif s[j] == previous_char:
                if is_middle:
                    right_chars_count += 1
                    if right_chars_count == left_chars_count:
                        count += 1
                        break
                else:
                    left_chars_count += 1
                    if left_chars_count >= 2:
                        count += 1
    return count


if __name__ == "__main__":
    assert substrCount(4, "aaaa") == 10
    assert substrCount(8, "mnonopoo") == 12
    assert substrCount(5, "asasd") == 7
    assert substrCount(7, "abcbaba") == 10
    assert substrCount(0, "") == 0
