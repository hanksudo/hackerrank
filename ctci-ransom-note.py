def checkMagazine(magazine, note):
    _dict = {}
    for word in magazine:
        try:
            _dict[word] += 1
        except:
            _dict[word] = 1

    for word in note:
        try:
            _dict[word] -= 1
            if _dict[word] < 0:
                print("No")
                return
        except:
            print("No")
            return

    print("Yes")
