seasons = {
    1: 'зима',
    2: 'весна',
    3: 'лето',
    4: 'осень'

}
month1 = int(input("Решение задачи с помощью словаря. Введите первый номер месяца:  "))
if month1 == 1 or month1 ==2 or month1 == 12:
    print(seasons.get(1))
if month1 == 3 or month1 ==4 or month1== 5:
    print(seasons.get(2))
if month1 == 6 or month1 ==7 or month1 == 8:
    print(seasons.get(3))
if month1 == 9 or month1 ==10 or month1 == 11:
    print(seasons.get(4))



list_seasons1 = ['зима', 'весна', 'лето', 'осень']
month2 = int(input("Решение задачи с помощью списка. Введите второй номер месяца: "))
if month2 == 1 or month2 ==2 or month2 == 12:
    print(list_seasons1[0])
if month2 == 3 or month2 ==4 or month2== 5:
    print(list_seasons1[1])
if month2 == 6 or month2 ==7 or month2 == 8:
    print(list_seasons1[2])
if month2 == 9 or month2 ==10 or month2 == 11:
    print(list_seasons1[3])



seasons = {
    'Winter': [1, 2, 12],
    'Spring': [3, 4, 5],
    'Summer': [6, 7, 8],
    'Autumn': [9, 10, 11]
}




