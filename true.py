import pandas as pd

data = {
    
}
df = pd.DataFrame(data)

def display_menu():
    print("\nВыберите действие:")
    print("1. Вывести")
    print("2. Вывести конкретную строку")
    print("3. Вывести столбец")
    print("4. Вывести ячейку")
    print("0. Выход")

def main():
    while True:
        display_menu()
        choice = input("Введите номер действия: ")

        if choice == '1':
            print(df)

        elif choice == '2':
            index = int(input("Введите индекс строки: "))
            if 0 <= index < len(df):
                print(df.iloc[index])
            else:
                print("Некорректный индекс.")

        elif choice == '3':
            index = int(input("Введите индекс столбца: "))
            if 0 <= index < len(df.columns):
                print(df.iloc[:, index])
            else:
                print("Некорректный индекс.")

        elif choice == '4':
            row_index = int(input("Введите индекс строки: "))
            col_index = int(input("Введите индекс столбца: "))
            if 0 <= row_index < len(df) and 0 <= col_index < len(df.columns):
                cell_value = df.iat[row_index, col_index]
                print(f"Значение ячейки: {cell_value}")

                action = input("Что вы хотите сделать с ячейкой? (удалить, изменить, создать): ").strip().lower()
                if action == 'удалить':
                    df.iat[row_index, col_index] = None
                    print("Ячейка удалена.")
                elif action == 'изменить':
                    new_value = input("Введите новое значение: ")
                    df.iat[row_index, col_index] = new_value
                    print("Ячейка изменена.")
                elif action == 'создать':
                    print("Создание новой ячейки не поддерживается в этом контексте.")
                else:
                    print("Некорректное действие.")
            else:
                print("Некорректные индексы.")

        elif choice == '0':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
    блэк бокс имбуля
