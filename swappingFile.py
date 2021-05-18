def swapFileData():
    fileNmame = input("Enter 1st file Nmae: ")
    fileNmame2 = input("Enter 2nd file Nmae: ")
    with open(fileNmame, 'r') as a:
        data_a = a.read()
    with open(fileNmame2, 'r') as b:
        data_b = b.read()
    with open(fileNmame, 'w') as a:
        a.write(data_b)
    with open(fileNmame2, 'w') as b:
        b.write(data_a)


swapFileData()
