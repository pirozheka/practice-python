class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def owner(self):
        return self._owner

    def check_balance(self):
        print(f'Баланс вашего счета: {self.balance}')

    def add_money(self, sum):
        #Проверяем, что сумма пополнения - положительное число
        if sum > 0:
            self.balance += sum
            print(f"Баланс пополнен успешно. Новый баланс счета: {self.balance}")
        else:
            print("Некорректная сумма, пожалуйста, введите положительное число")

    def take_money(self, sum):
        #Проверяем, что баланс не будет отрицательным
        if 0 < sum < self.balance:
            self.balance -= sum
            print(f"Выдача денег... Новый баланс счета: {self.balance}")
        else:
            print("Нет достаточной суммы для снятия. Введите другую сумму")

class BankGame:
    def __init__(self, account):
        self.account = account
    def start(self):
        print(f'Добро пожаловать в банкомат, {self.account.owner}!')

        while True:
            print("1. Положить деньги")
            print("2. Снять деньги")
            print("3. Проверить баланс")
            print("4. Выйти")

            choice = input('Выберите действие (1-4): ')

            if choice == '1':
                #Как бы пользователь не ввел буквы...
                try:
                    amount = float(input('Введите сумму для пополнения: '))
                    self.account.add_money(amount)
                except ValueError:
                    print('Ошибка, введите числовое значение')
            elif choice == '2':
                try:
                    amount = float(input('Введите сумму снятия: '))
                    self.account.take_money(amount)
                except ValueError:
                    print('Ошибка, введите числовое значение')
            elif choice == '3':
                self.account.check_balance()
            elif choice == '4':
                print(f'До свидания, {self.account.owner}!')
                return
            else:
                print('Неправильный ввод. Введите цифру от 1 до 4')

account = BankAccount("John Pearce", 1000)
game = BankGame(account)
game.start()

