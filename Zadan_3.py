p = 1
#spisok=[1, 2, 3, 4]
while True:
    try:
        n=int(input("Сколько элементов вы добавить в список? n= "))
        break
    except ValueError:
        print("Введено некорректное значение!")
spisok =[]
for i in range(n):
    while True:
        try:
            spisok.append(int(input("Число= ")))
            break
        except ValueError:
            print("Введено некорректное значение!")
i=1
while i<n:
    p*=spisok[i]
    i=i+2
print("Длина списка: ", len(spisok))
print("Произведение элементов списка с четными номерами: ", p)