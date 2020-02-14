# Dynamic Array
# https://www.hackerrank.com/challenges/dynamic-array/problem
#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    last_ans = 0
    seq_list = []
    answers = []
    for _ in range(n):
        seq_list.append([])
    
    for t, x, y in queries:
        if t == 1:
            seq_list[(x ^ last_ans) % n].append(y)
        else:
            seq = seq_list[(x ^ last_ans) % n]
            last_ans = seq[y % len(seq)]
            answers.append(last_ans)

    return answers

if __name__ == '__main__':
    n = 2
    q = 5

    queries = [
        [1, 0, 5],
        [1, 1, 7],
        [1, 0, 3],
        [2, 1, 0],
        [2, 1, 1]
    ]

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))
