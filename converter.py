import math

import sys

def show_menu():
    print("\nКонвертер величин")
    print("1. Длина (см - м)")
    print("2. Масса (г - кг)")
    print("3. Объём (л - галлон)")
    print("4. Температура (°C - °F)")
    print("0. Выход")

def length_conv():
    val = float(input("Введите значение: "))
    unit = input("Из единиц (cm/m): ").lower()
    if unit == 'cm':
        result = val / 100
        print(f"{val} см = {result:.2f} м")
    elif unit == 'm':
        result = val * 100
        print(f"{val} м = {result:.2f} см")
    else:
        print("Ошибка: введите cm или m")

def main():
    while True:
        show_menu()
        choice = input("Выберите операцию: ")
        if choice == '0':
            break
        elif choice == '1':
            length_conv()
        else:
            print("Функция в разработке")

if __name__ == "__main__":
    main()