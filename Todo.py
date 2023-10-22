def display_menu():
    print("\nTo-Do List:")
    print("1. Dodaj zadanie")
    print("2. Usuń zadanie")
    print("3. Wyświetl wszystkie zadania")
    print("4. Zakończ program")

def add_task(tasks):
    task = input("Podaj nazwę zadania: ")
    tasks.append(task)
    print("Zadanie dodane.")

def remove_task(tasks):
    if not tasks:
        print("Lista jest pusta!")
        return
    print("\nZadania do wykonania:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
    try:
        task_num = int(input("Podaj numer zadania do usunięcia: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Zadanie '{deleted_task}' zostało usunięte.")
        else:
            print("Nieprawidłowy numer!")
    except ValueError:
        print("Nieprawidłowy numer!")

def display_tasks(tasks):
    if not tasks:
        print("Lista jest pusta!")
        return
    print("\nZadania do wykonania:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nWybierz opcję (1-4): ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
