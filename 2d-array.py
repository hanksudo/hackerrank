# 2D Array - DS
# https://www.hackerrank.com/challenges/2d-array

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = None
    for y in range(len(arr) - 2):
        for x in range(len(arr[y]) - 2):
            hourglass_sum = 0
            hourglass_sum += sum(arr[y][x + _] + arr[y + 2][x + _] for _ in range(3))
            hourglass_sum += arr[y + 1][x + 1]
            if max_sum is None:
                max_sum = hourglass_sum
            else:
                max_sum = max(max_sum, hourglass_sum)
                
    return max_sum

if __name__ == "__main__":
    arr = []
    arr.append([1, 1, 1, 0, 0, 0])
    arr.append([0, 1, 0, 0, 0, 0])
    arr.append([1, 1, 1, 0, 0, 0])
    arr.append([0, 0, 2, 4, 4, 0])
    arr.append([0, 0, 0, 2, 0, 0])
    arr.append([0, 0, 1, 2, 4, 0])

    assert hourglassSum(arr) == 19
