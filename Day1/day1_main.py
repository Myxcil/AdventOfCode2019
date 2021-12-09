import math


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def calc_fuel(mass: int):
    return max(0, math.floor(mass / 3) - 2)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def calc_fuel_total(mass: int):
    fuel = calc_fuel(mass)
    if fuel > 0:
        fuel += calc_fuel_total(fuel)
    return fuel


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Part One
print(sum([calc_fuel(int(x)) for x in open("day1_input.txt", "r").readlines()]))

# Part Two
print(sum([calc_fuel_total(int(x)) for x in open("day1_input.txt", "r").readlines()]))
