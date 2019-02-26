def get_summ(num_one, num_two):
    try:
        num_summ = int(num_one) + int(num_two)
        print(num_summ)
    except ValueError:
        print("Один или оба аргумента не являются числами.")


get_summ(23, 2)
