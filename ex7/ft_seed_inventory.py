#!/usr/bin/env python3

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    message = seed_type.capitalize() + " seeds: "
    if unit == "packets":
        message += str(quantity) + " " + unit + " available"
    elif unit == "grams":
        message += str(quantity) + " " + unit + " total"
    elif unit == "area":
        message += "covers " + str(quantity) + " square meters"
    else:
        message = "Unknown unit type"
    print(message)
