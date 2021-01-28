new_list = []
n = 10
for i in range(n):
    new_list.append(input("Введите элемент для добавления в список: "))
print(new_list)
#добавление в список только 10 элементов, но можно больше или меньше(просто чтобы ограниить ввод элементов с консоли)
l=0
for k in range(int(len(new_list)/2)):
    new_list[l],new_list[l+1] = new_list[l+1],new_list[l]
    l+=2
print(new_list)





