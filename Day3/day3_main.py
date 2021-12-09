# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def parse_entry(_text) -> [tuple[chr,int]]:
    return _text[0], int(_text[1:])


def fill_set(_segments: [tuple[chr,int]]) -> tuple[set[tuple[int,int]], dict[tuple[int, int, int]]]:
    x = 0
    y = 0
    d = 0
    matrix: set[tuple[int, int]] = set()
    distances: dict[tuple[int, int], int] = dict()
    for seg in _segments:
        if seg[0] == 'L':
            for i in range(seg[1]):
                x -= 1
                d += 1
                matrix.add((x, y))
                distances[x, y] = d
        elif seg[0] == 'R':
            for i in range(seg[1]):
                x += 1
                d += 1
                matrix.add((x, y))
                distances[x, y] = d
        elif seg[0] == 'U':
            for i in range(seg[1]):
                y += 1
                d += 1
                matrix.add((x, y))
                distances[x, y] = d
        else:
            for i in range(seg[1]):
                y -= 1
                d += 1
                matrix.add((x, y))
                distances[x, y] = d
    return matrix, distances


def calc_manhattan_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
with open("day3_input.txt", "r") as file:
    wire_a = [parse_entry(x) for x in file.readline().split(',')]
    wire_b = [parse_entry(x) for x in file.readline().split(',')]

set_a, dist_a = fill_set(wire_a)
set_b, dist_b = fill_set(wire_b)

intersect = set_a.intersection(set_b)
nearest = min([calc_manhattan_distance((0,0), x) for x in intersect])
print(f'Part 1: {nearest}')


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
nearest = min([dist_a[x] + dist_b[x] for x in intersect])
print(f'Part 2: {nearest}')