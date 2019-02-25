user_age = input("Пожалуйста, введите ваш возраст: \n")


def user_ocupation(age):
    try:
        if int(age) < 3:
            return "Вам пока можно ничего не делать!"
        elif int(age) in range(3, 7):
            return "Вы должны ходить в детский сад!"
        elif int(age) in range(7, 18):
            return "Вам должны учиться в школе!"
        elif int(age) in range(18, 24):
            return "Вы должны учиться в ВУЗе!"
        elif int(age) > 23:
            return "Вам пора работать!"
    except ValueError:
        return "Вы ввели не целое число. Попробуйте еще раз!"


user_message = user_ocupation(user_age)
print(user_message)
