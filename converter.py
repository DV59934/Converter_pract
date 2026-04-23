def show_menu():
    print("\nКонвертер величин")
    print("1. Длина (см - м)")
    print("2. Масса (г - кг)")
    print("3. Объём (л - галлон)")
    print("4. Температура (°C - °F)")
    print("0. Выход")

def temp_conv():
    val = float(input("Введите значение: "))
    unit = input("Из единиц (C/F): ").lower()
    if unit == 'c':
        result = val * 9/5 + 32
        print(f"{val}°C = {result:.1f}°F")
    elif unit == 'f':
        result = (val - 32) * 5/9
        print(f"{val}°F = {result:.1f}°C")
    else:
        print("Ошибка: введите C или F")

def main():
    while True:
        show_menu()
        choice = input("Выберите операцию: ")
        if choice == '0':
            break
        elif choice == '1':
            print("Функция в разработке")
        elif choice == '2':
            print("Функция в разработке")
        elif choice == '3':
            print("Функция в разработке")
        elif choice == '4':
            temp_conv()
        else:
            print("Функция в разработке")

if __name__ == "__main__":
    main()