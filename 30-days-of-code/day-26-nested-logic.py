def calculate_fine(return_date, due_date):
    d1, m1, y1 = map(int, return_date.split(" "))
    d2, m2, y2 = map(int, due_date.split(" "))

    if y1 < y2:
        return 0
    elif y1 > y2:
        return 10000
    elif y1 == y2:
        if m1 > m2:
            return 500 * (m1 - m2)
        elif m1 < m2:
            return 0
        else:
            if d1 <= d2:
                return 0
            else:
                return 15 * (d1 - d2)
    return 0

if __name__ == "__main__":
    assert calculate_fine("9 6 2015", "6 6 2015") == 45
    assert calculate_fine("9 8 2015", "6 6 2015") == 1000
    assert calculate_fine("1 1 2015", "3 6 2014") == 10000
