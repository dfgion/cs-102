def summ(a: int, b: int):
    return a + b


def difference(a: int, b: int):
    return a - b


def multiply(a: int, b: int):
    return a * b


def division(a: int, b: int):
    return a / b


def exponentiation(a: int, b: int = 1):
    return a**b


def main():
    while True:
        try:
            a = input("Введите первое число\n")
            a = float(a)
            b = input("Введите второе число\n")
            b = float(b)
        except:
            print("\nВведите число!\n")
            continue
        do = input(
            "Введите действие(Умножение/Деление/Разность/Сумма/Степень)\nУмножение-1\nДеление-2\nРазность-3\nСумма-4\nСтепень-5\n"
        )
        if (do == "Умножение") or (do == "1"):
            print(multiply(a, b))
        elif (do == "Деление") or (do == "2"):
            if int(b) == 0:
                print("\nНельзя делить на 0\n")
                continue
            else:
                print(division(a, b))
        elif (do == "Разность") or (do == "3"):
            print(difference(a, b))
        elif (do == "Сумма") or (do == "4"):
            print(summ(a, b))
        elif (do == "Степень") or (do == "5"):
            print(exponentiation(a, b))
        else:
            print("Введите команду из предложенных!")


if __name__ == "__main__":
    main()
