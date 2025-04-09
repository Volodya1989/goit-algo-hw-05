from typing import Callable
import re

# generate real numbers


def generator_numbers(text: str):
    # finding real numbers separated by spaces
    pattern = r'(?<=\s)[+-]?\d+(?:\.\d+)?(?=\s)'
    matches = re.findall(pattern, f'{text}')
    # converting each match into float
    for n in matches:
        yield float(n)

# calculates total sum of the found numbers and returns result


def sum_profit(text: str, func: Callable) -> float:
    total = 0
    for num in func(text):
        total += num

    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f'Total income: {total_income}.')
