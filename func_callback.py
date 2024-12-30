from typing import Callable


def new_number(number: int) -> None:
    print(f"Received a new number: {number}")


def is_positive(number: int) -> None:
    if not number:
        print("Zero")
    else:
        print(
            f"{number} is a positive number"
            if number > 0
            else f"{number} is a negative number"
        )


def print_bye(number: int | str) -> None:
    print("Bye!")


def numbers_handler(
    numbers: list[int],
    before: Callable = new_number,
    action: Callable = is_positive,
    after: Callable = print_bye,
) -> None:
    for number in numbers:
        before(number)
        action(number)
        after(number)


numbers_handler([1, -1, 0], before=is_positive)
