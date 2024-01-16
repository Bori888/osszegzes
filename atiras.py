def feladat():
    i:int = int(0)
    n:int = int(0)

    while(n <= 0):
        n = int(input("N ="))
    ossz:int = int(0)
    for i in range(n+1):
        ossz += i
    print(f"Az első {n} db természetes szösszege: {ossz}")


