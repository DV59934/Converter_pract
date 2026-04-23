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

def weight_conv():
    val = float(input("Введите значение: "))
    unit = input("Из единиц (g/kg): ").lower()
    if unit == 'g':
        result = val / 1000
        print(f"{val} г = {result:.3f} кг")
    elif unit == 'kg':
        result = val * 1000
        print(f"{val} кг = {result:.3f} г")
    else:
        print("Ошибка: введите g или kg")

def volume_conv():
    val = float(input("Введите значение: "))
    unit = input("Из единиц (l/gal): ").lower()
    if unit == 'l':
        result = val / 3.78541
        print(f"{val} л = {result:.2f} галлон")
    elif unit == 'gal':
        result = val * 3.78541
        print(f"{val} галлон = {result:.2f} л")
    else:
        print("Ошибка: введите l или gal")

def main():
    while True:
        show_menu()
        choice = input("Выберите операцию: ")
        if choice == '0':
            break
        elif choice == '1':
            length_conv()
        elif choice == '2':
            weight_conv()
        elif choice == '3':
            volume_conv()
        else:
            print("Функция в разработке")

if __name__ == "__main__":
    main()