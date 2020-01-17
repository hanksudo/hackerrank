a = [3, 2, 1]
n = len(a)

number_of_swaps = 0
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            number_of_swaps += 1
        
    if number_of_swaps == 0:
        break

print(f"Array is sorted in {number_of_swaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")
