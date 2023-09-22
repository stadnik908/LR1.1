ch="Да"
slovar={'Кольцо':["Золото", 100, 5],'Серьги':["Серебро", 50, 3],'Подвеска':["Белое золото", 200, 7],'Кулон':["Серебро", 60, 8],'Браслет':["Золото", 150, 4]}
while ch=="Да":
    print("Ювелирный Магазин")
    print("Меню")
    print("1. Просмотр описания: название-описание")
    print("2. Просмотр цены: название-цены")
    print("3. Просмотр количества: название-количество")
    print("4. Всю информация")
    print("5. Покупка")
    print("6. До свидания")
    while True:
        try:
            choice = int(input("Выберите пожалуйста услугу: "))
            break
        except ValueError:
            print("Ошибка!")
    if choice==1:
        for i in slovar:
            print(i, "-", slovar[i][0])
    elif choice==2:
        for i in slovar:
            print(i, "-", slovar[i][1])
    elif choice == 3:
        for i in slovar:
            print(i, "-", slovar[i][2])
    elif choice == 4:
        for i in slovar:
            print(i, "-", slovar[i][0], "-", slovar[i][1], " руб", "-", slovar[i][2], "шт")
    elif choice == 5:
        sum=0
        slovar_2 = {'Название': ["Количество", "Сумма"]}
        while ch=="Да":
            k=0
            thing=input("Введите название товара, который хотите приобрести: ")
            while True:
                try:
                    kol = int(input("Введите количество товара, который хотите приобрести: "))
                    break
                except ValueError:
                    print("Ошибка!")
            for i in slovar:
                if thing==i and slovar[i][2]>=kol:
                    sum+=kol*slovar[i][1]
                    slovar[i][2]-=kol
                    slovar_2.update({thing:[kol,kol*slovar[i][1]]})
                    k=1
            if k==0:
                print("Товара с таким названием или в таком количестве нет в наличии")
            ch = input("Если хочешь продолжить выбирать товары введите 'Да':")
        print("-------Чек-------")
        for i in slovar_2:
            print(i, "-", slovar_2[i][0], "(шт) -", slovar_2[i][1], " (руб)")
        print("Сумма ваших товаров составила: ", sum, " руб")
        print("-------Чек-------")


    elif choice == 6:
        print("До свидания)")
        ch="Нет"
    else:
        print("Введено некорректное значние")
    if choice!=6:
        ch=input("Если хочешь продолжить введи 'Да':" )