from typing import List


def hello(name: str = None) -> str:
    if name:
        string_out = 'Hello, ' + name + '!'
    else:
        string_out = 'Hello!'
    return string_out


def int_to_roman(num: int) -> str:
    M = ['', 'M', 'MM', 'MMM', 'MMMM']
    C_D = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    X_L = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    I_V = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    thousands = M[num // 1000]
    hundreds = C_D[(num // 100) % 10]
    ten = X_L[(num // 10) % 10]
    one = I_V[num % 10]
    out = thousands + hundreds + ten + one
    return out


def longest_common_prefix(strs_input: List[str]) -> str:
    if strs_input:
        for i in range(0, len(strs_input)):
            strs_input[i] = strs_input[i].strip()
        cnt = 0
        check = True
        for i in range(0, len(strs_input[0])):
            if not check:
                break
            for word in strs_input:
                if (len(word) - 1) >= i:
                    if strs_input[0][i] != word[i]:
                        check = False
                else:
                    check = False
            if check:
                cnt += 1
        return strs_input[0][:cnt]
    else:
        return ''


def prime_check(a):
    tmp = 2
    while a % tmp != 0:
        tmp += 1
    if tmp == a:
        return True
    return False


def primes() -> int:
    number = 1
    while True:
        number += 1
        if prime_check(number):
            yield number


class BankCard:
    def __init__(self, total_sum: int = 0, balance_limit: int = -1):
        self.total_sum = total_sum
        self.balance_limit = balance_limit

    def __call__(self, sum_spent):
        if self.total_sum >= sum_spent:
            self.total_sum -= sum_spent
        else:
            raise ValueError('Not enough money to spend send sum_spent dollars.')

    def get_balance(self):
        if self.balance_limit == 0:
            raise ValueError("Balance check limits exceeded.")
        if self.balance_limit == -1:
            return self.total_sum
        self.balance_limit -= 1
        return self.total_sum

    balance = property(get_balance)

    def __str__(self):
        return "To learn the balance call balance."

    def put(self, sum_put):
        self.total_sum += sum_put

    def __add__(self, x):
        return BankCard(self.total_sum + x.total_sum, max(self.balance_limit, x.balance_limit))

    # balance = property(getValue, None, None, None)
    # balance_limit = property(getBalance, None, None, None)


a = BankCard(10, 2)
print(a.balance) # 10
print(a.balance_limit) # 1
a(5)  # You spent 5 dollars.
print(a.total_sum) # 5
print(a) # To learn the balance call balance.
print(a.balance) # 5
try:
    a(6) # Not enough money to spend 6 dollars.
except ValueError:
    pass
a(5) # You spent 5 dollars.
try:
    a.balance # Balance check limits exceeded.
except ValueError:
    pass
a.put(2) # You put 2 dollars.
print(a.total_sum) # 2
b = BankCard(15, 4)
c = a + b
print(c.balance)