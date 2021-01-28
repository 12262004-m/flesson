new_str = input("Введите строку: ")
a = new_str.split()
for i in a:
    if len(i)<=10:
        print(i)
    else:
        print(i[0:10])