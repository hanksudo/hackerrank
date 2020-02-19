# https://www.hackerrank.com/challenges/equal-stacks/problem
#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    new_h1 = []
    new_h2 = []
    new_h3 = []

    height_of_h1 = 0
    for _ in h1[::-1]:
        height_of_h1 += _
        new_h1.append(height_of_h1)

    height_of_h2 = 0
    for _ in h2[::-1]:
        height_of_h2 += _
        new_h2.append(height_of_h2)

    height_of_h3 = 0
    for _ in h3[::-1]:
        height_of_h3 += _
        new_h3.append(height_of_h3)

    while True:
        if not new_h1 or not new_h2 or not new_h3:
            return 0

        val1 = new_h1[-1]
        val2 = new_h2[-1]
        val3 = new_h3[-1]
        if val1 == val2 == val3:
            return val1

        if val1 >= val2 and val1 >= val3:
            new_h1.pop()
        elif val2 >= val1 and val2 >= val3:
            new_h2.pop()
        elif val3 >= val1 and val3 >= val2:
            new_h3.pop()
