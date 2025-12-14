from src.data_processor import get_csv, get_excel
from src.data_search import process_bank_search
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_data
from src.widjet import get_date, mask_account_card


def main():
    while True:
        print(
            """
        Привет! Добро пожаловать в программу работы с банковскими транзакциями.
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
        """
        )

        username_input = input()

        if username_input == "1":
            data = get_data("./data/operations.json")
            print("Для обработки выбран JSON-файл.")
            break
        elif username_input == "2":
            data = get_csv("./data/transactions.csv")
            print("Для обработки выбран CSV-файл.")
            break
        elif username_input == "3":
            data = get_excel("./data/transactions_excel.xlsx")
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print(
                "Указанного пункта нет в меню. Пожалуйста, используйте цифры 1, 2 или 3,\n"
                "чтобы выбрать необходимый пункт."
            )

    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )

        state = input().upper()

        if state == "EXECUTED":
            data = filter_by_state(data)
            print("Операции отфильтрованы по статусу 'EXECUTED'")
            break
        elif state == "CANCELED":
            data = filter_by_state(data, state)
            print("Операции отфильтрованы по статусу 'CANCELED'")
            break
        elif state == "PENDING":
            data = filter_by_state(data, state)
            print("Операции отфильтрованы по статусу 'PENDING'")
            break
        else:
            print(f"Статус операции {state} недоступен.")

    while True:
        print("Отсортировать операции по дате? Да/Нет")

        user_input = input().lower()

        if user_input == "да":
            while True:
                print("Отсортировать по возрастанию или по убыванию?")

                user_input = input().lower()

                if user_input == "по возрастанию":
                    data = sort_by_date(data, False)
                    break
                elif user_input == "по убыванию":
                    data = sort_by_date(data)
                    break
                else:
                    print("Пожалуйста, введите 'по возрастанию' или 'по убыванию'")
            break
        elif user_input == "нет":
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'")

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")

        user_input = input().lower()

        if user_input == "да":
            if username_input == "1":
                data = list(filter_by_currency(data, "RUB"))
                break
            elif username_input == "2" or "3":
                data = list(filter(lambda x: x["currency_code"] == "RUB", data))
                break
        elif user_input == "нет":
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'")

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")

        user_input = input().lower()

        if user_input == "да":
            print("Введите слово для фильтрации:")

            search = input().lower()

            data = process_bank_search(data, search)
            break
        elif user_input == "нет":
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'")

    print("Распечатываю итоговый список транзакций...")

    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

    for item in data:
        item["date"] = get_date(item["date"])
        item["to"] = mask_account_card(item["to"])
        if item["description"] != "Открытие вклада":
            item["from"] = mask_account_card(item["from"])

    print(f"Всего банковских операций в выборке: {len(data)}")

    for item in data:
        if item["description"] == "Открытие вклада":
            if username_input == "1":
                print(
                    f"{item["date"]} {item["description"]}\n"
                    f"{item["to"]}\n"
                    f"Сумма: {item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n"
                )
            elif username_input == "2" or "3":
                print(
                    f"{item["date"]} {item["description"]}\n"
                    f"{item["to"]}\n"
                    f"Сумма: {item["amount"]} {item["currency_name"]}\n"
                )

        else:
            if username_input == "1":
                print(
                    f"{item["date"]} {item["description"]}\n"
                    f"{item["from"]} -> {item["to"]}\n"
                    f"Сумма: {item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n"
                )
            elif username_input == "2" or "3":
                print(
                    f"{item["date"]} {item["description"]}\n"
                    f"{item["from"]} -> {item["to"]}\n"
                    f"Сумма: {item["amount"]} {item["currency_name"]}\n"
                )


if __name__ == "__main__":
    main()
