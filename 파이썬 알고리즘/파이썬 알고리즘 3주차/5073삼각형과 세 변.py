while True:
    n1, n2, n3 = map(int,input().split(" "))

    if n1 == 0 and n2 == 0 and n3 == 0:
        break

    maximum = max(n1,n2,n3)

    if maximum >= n1+n2+n3-maximum:
        print("Invalid")
    else:
        if n1 == n2 or n2 == n3 or n1 == n3:
            if n1 == n2 and n2 == n3:
                print("Equilateral")
            else:
                print("Isosceles")
        else:
            print("Scalene")