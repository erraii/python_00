!/usr/bin/python3

def ft_helper_recursive(current: int, days: int) -> None:
    print("Day " + str(current))
    if current < days:
        ft_helper_recursive(current + 1, days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    ft_helper_recursive(1, days)
    print("Harvest time!")
