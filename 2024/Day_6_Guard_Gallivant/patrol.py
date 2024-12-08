import re

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

input = open("input.txt", "r").readlines()
input = [l.strip() for l in input]

guard = r">|<|\^|v"

def update_map(pos: tuple[int, int], map: list[list[str]]) -> tuple[int, int]:
    assert (map[pos[0]][pos[1]] == UP) or\
        (map[pos[0]][pos[1]] == DOWN) or\
        (map[pos[0]][pos[1]] == LEFT) or\
        (map[pos[0]][pos[1]] == RIGHT)
    
    guard = map[pos[0]][pos[1]]
    new_pos = pos
    
    while pos == new_pos:

        if guard == UP:
            next_step = map[pos[0] - 1][pos[1]]
            if next_step == "#":
                guard = RIGHT
            else:
                new_pos = (pos[0] - 1, pos[1])

        if guard == DOWN:
            next_step = map[pos[0] + 1][pos[1]]
            if next_step == "#":
                guard = LEFT
            else:
                new_pos = (pos[0] + 1, pos[1])

        if guard == LEFT:
            next_step = map[pos[0]][pos[1] - 1]
            if next_step == "#":
                guard = UP
            else:
                new_pos = (pos[0],pos[ 1] - 1)

        if guard == RIGHT:
            next_step = map[pos[0]][pos[1] + 1]
            if next_step == "#":
                guard = DOWN
            else:
                new_pos = (pos[0],pos[ 1] + 1)
    
    map[pos[0]][pos[1]] = "X"
    map[new_pos[0]][new_pos[1]] = guard
    return new_pos

searched_positions = [(i, re.search(guard,l)) for i, l in enumerate(input)]
pos = [(pos[0], pos[1].start()) for pos in searched_positions if pos[1] is not None][0]
map = [list(l) for l in input]
try:
    while True:
        pos = update_map(pos, map)
except IndexError:
    map_string = "".join(["".join(l) for l in map])
    total = len(re.findall("X", map_string)) + 1
    print(total)
