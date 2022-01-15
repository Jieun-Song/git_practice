# 271 - 280
import random


class Account:

    account_count = 0
    plus_count = 0
    plus_history = []
    minus_history = []

    def __init__(self, owner, left):
        self.owner = owner
        self.left = left
        self.bank = "SCbank"
        a = ""
        for i in range(3):
            a += str(random.randrange(1, 10))
        a += "-"
        for i in range(2):
            a += str(random.randrange(1, 9))
        a += "-"
        for i in range(6):
            a += str(random.randrange(1, 10))
        self.num = a

        Account.account_count += 1

    def get_account_num(self):
        print(Account.account_count)

    def deposit(self, plus_money):
        if plus_money >= 1:
            self.left += plus_money

        self.plus_count += 1
        self.plus_history.append(plus_money)

        if self.plus_count == 5:
            self.left += self.left * 0.01
            self.plus_count = 0

    def withdraw(self, minus_money):
        if minus_money <= self.left:
            self.left -= minus_money

        self.minus_history.append(minus_money)

    def display_info(self):
        print("은행이름 :", self.bank)
        print("예금주 :", self.owner)
        print("계좌번호 :", self.num)
        print("잔고 :", self.left)

    def deposit_history(self):
        for i in self.plus_history:
            print(i)

    def withdraw_history(self):
        for i in self.minus_history:
            print("-", i)


kim = Account("김민수", 1)
kim.display_info()
kim.deposit(100)
kim.deposit(100)
kim.deposit(100)
kim.deposit(100)
kim.deposit(100)
kim.withdraw(100)
kim.withdraw(100)
kim.withdraw(100)
kim.withdraw(100)
kim.withdraw(100)
kim.deposit_history()
kim.withdraw_history()
