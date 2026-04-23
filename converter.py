def show_menu():
    print("\nКонвертер величин")
    print("1. Длина (см - м)")
    print("2. Масса (г - кг)")
    print("3. Объём (л - галлон)")
    print("4. Температура (°C - °F)")
    print("0. Выход")

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
            print("Функция в разработке")
        elif choice == '2':
            print("Функция в разработке")
        elif choice == '3':
            volume_conv()
        else:
            print("Функция в разработке")

if __name__ == "__main__":
    main()