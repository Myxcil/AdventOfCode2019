# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def count_orbits(name: str, table: dict[str, str], stop_at: str = "COM") -> int:
    if name != stop_at:
        if name in table:
            return 1 + count_orbits(table[name], table, stop_at)
    return 0


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def find_path(name: str, table: dict[str, str], route: list[str]):
    if name in table:
        route.append(name)
        find_path(table[name], table, route)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
orbits: dict[str, str] = dict()
with open("day6_input.txt", "r") as file:
    for line in file.readlines():
        center, orbiter = line.strip().split(')')
        orbits[orbiter] = center

# Part One
total_orbits = 0
for o in orbits.keys():
    total_orbits += count_orbits(o, orbits)
print(f'Total orbits: {total_orbits}')


# Part Two
orbits.clear()
with open("day6_input.txt", "r") as file:
    for line in file.readlines():
        center, orbiter = line.strip().split(')')
        orbits[orbiter] = center

you_path: [str] = []
find_path("YOU", orbits, you_path)
# print(you_path)

san_path: [str] = []
find_path("SAN", orbits, san_path)
# print(san_path)

intersect = next(i for i in you_path if i in san_path)
# print(intersect)

num_hops = count_orbits(orbits["YOU"], orbits, intersect)
num_hops += count_orbits(orbits["SAN"], orbits, intersect)
print(f'YOU -> SAN: {num_hops}')
