from typing import List


class Transaction:
    def __init__(self, amount: float, description: str, transaction_type: str):
        self.amount = amount
        self.description = description
        self.type = transaction_type


class FinanceManager:
    def __init__(self):
        self.transactions: List[Transaction] = []

    def add_transaction(self, amount: float, description: str, transaction_type: str):
        transaction = Transaction(amount, description, transaction_type)
        self.transactions.append(transaction)
    def total_for_type(self, transaction_type: str) -> float:
        return sum(transaction.amount for transaction in self.transactions if transaction.type == transaction_type)

    def display_balance(self) -> float:
        return self.total_for_type("income") - self.total_for_type("expense")

    def display_summary(self):
        print("\nPrzychody:")
        for transaction in [t for t in self.transactions if t.type == "income"]:
            print(f"{transaction.description}: {transaction.amount} PLN")

        print("\nWydatki:")
        for transaction in [t for t in self.transactions if t.type == "expense"]:
            print(f"{transaction.description}: {transaction.amount} PLN")

        print(f"\nBilans: {self.display_balance()} PLN")
class App:
    def __init__(self):
        self.manager = FinanceManager()

    def run(self):
        while True:
            print("\nZarządzanie finansami:")
            print("1. Dodaj przychód")
            print("2. Dodaj wydatek")
            print("3. Wyświetl podsumowanie")
            print("4. Zakończ program")

            choice = input("\nWybierz opcję (1-4): ")

            if choice == "1":
                self._add_transaction("income")

            elif choice == "2":
                self._add_transaction("expense")

            elif choice == "3":
                self.manager.display_summary()

            elif choice == "4":
                print("Koniec programu.")
                break

            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

    def _add_transaction(self, transaction_type: str):
        try:
            amount = float(input(f"Podaj kwotę {transaction_type}: "))
            description = input(f"Opis {transaction_type}: ")
            self.manager.add_transaction(amount, description, transaction_type)
        except ValueError:
            print("Podaj prawidłową kwotę!")


if __name__ == "__main__":
    app = App()
    app.run()
