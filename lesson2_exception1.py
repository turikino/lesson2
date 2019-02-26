answers = {
            "Как дела?": "Хорошо",
            "Что делаешь?" : "Программирую",
            "Какие новости?": "Да ничего особенного",
            "Яйцо или курица?" : "В этом году ты точно знаешь!"
        }

def ask_user(dct):
    try:
        while True:
            user_say = input("Пользователь: \n")
            if user_say == "Молодец!":
                print("Программа: \nСпасибо!")
                return False
            elif user_say in dct.keys():
                print("Программа: \n{}".format(dct.get(user_say)))
    except KeyboardInterrupt:
        print("\nПока!")

ask_user(answers)

