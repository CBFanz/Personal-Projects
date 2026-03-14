while True:
    x = input("Enter the number max limit whole no: ")
    y = input("Enter the target whole no: ")
    if x.isdigit() == True and y.isdigit() == True:
        x = int(x)
        target = int(y)
        numset = list(range(0,x+1))
        ansset = {}
        for i in numset:
            for j in numset:
                if i*j == target:
                    ansset.update({i:j})
                    numset.remove(i)
                    numset.remove(j)
        print(ansset)
    else:
        print("Try again")