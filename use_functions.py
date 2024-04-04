"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

def bankfunc():

    count = 0
    history = []

    while True:
        print('1 - Пополнение счета')
        print('2 - Покупка')
        print('3 - История покупок')
        print('4 - Выход')
        print('Текущая сумма: ', count)
        print()
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            refill = int(input('Введите сумму: '))
            count += refill
            print()
        elif choice == '2':
            purchase = int(input('Введите сумму покупки: '))
            if purchase > count:
                print('Недостаточно средств!')
            else:
                name = input('Введите название покупки: ')
                count -= purchase
                history.append((name, purchase))
            print()
        elif choice == '3':
            print('История покупок:')
            for i in history:
                print(i)
            print()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
            print()
