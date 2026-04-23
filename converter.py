def show_menu():
    print("\nКонвертер величин")
    print("1. Длина (см - м)")
    print("2. Масса (г - кг)")
    print("3. Объём (л - галлон)")
    print("4. Температура (°C - °F)")
    print("0. Выход")

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

def main():
    while True:
        show_menu()
        choice = input("Выберите операцию: ")
        if choice == '0':
            break
        elif choice == '1':
            print("Функция в разработке")
        elif choice == '2':
            weight_conv()
        else:
            print("Функция в разработке")

if __name__ == "__main__":
    main()