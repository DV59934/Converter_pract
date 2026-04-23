def show_menu():
    print("\nКонвертер величин")
    print("1. Длина (см ↔ м)")
    print("2. Масса (г - кг)")
    print("3. Объём (л - галлон)")
    print("4. Температура (°C - °F)")
    print("0. Выход")

def main():
    while True:
        show_menu()
        choice = input("Выберите операцию: ")
        if choice == '0':
            break
        print("Функция в разработке")

if __name__ == "__main__":
    main()