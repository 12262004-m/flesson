list_of_rating = [7, 6, 4, 3, 1]
number = int(input("Введите число для добавления в список: "))
while number!=0:
    for i in range (len(list_of_rating)):
        if list_of_rating[i] == number:
            list_of_rating.insert(i+1, number)
            break
        elif list_of_rating[0] < number:
            list_of_rating.insert(0, number)
        elif list_of_rating[-1] > number:
            list_of_rating.append(number)
        elif list_of_rating[i] > number and list_of_rating[-1] < number:
            list_of_rating.insert(i+1, number)
    print("Вы добавили в список новое число. Вот что у вас получилось: ", list_of_rating)
    number=int(input("Введите число для добавления в список: "))





