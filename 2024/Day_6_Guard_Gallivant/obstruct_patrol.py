import re

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

input = open("input.txt", "r").readlines()
input = [l.strip() for l in input]

guard = r">|<|\^|v"

def update_map(pos: tuple[int, int], map: list[list[str]]):
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
    return new_pos, guard

searched_positions = [(i, re.search(guard,l)) for i, l in enumerate(input)]
pos = [(pos[0], pos[1].start()) for pos in searched_positions if pos[1] is not None][0]
map = [list(l) for l in input]
obstructions = 0
guard = map[pos[0]][pos[1]]
try:
    positions = [pos]
    collisions = []
    i = 0
    while True:
        last_guard = guard
        current_pos, guard = update_map(positions[-1], map)
        if last_guard != guard:
            collisions.append(i)
        i += 1
        
        if len(collisions) < 3:
            positions.append(current_pos)
            continue
    
        parallel_path = [p2 - p1 for p1, p2 in zip(positions[collisions[-3]], positions[collisions[-2]])]
        last_path = [p2 - p1 for p1, p2 in zip(positions[collisions[-1]], current_pos)]
    
        # print(parallel_path)
        # print(last_path)
        if abs(sum(parallel_path)) == abs(sum(last_path)):
            print("potential obstructor")
            print(current_pos)
            print(positions[collisions[-3]])
            connecting_vec = [p2 - p1 for p1, p2 in zip(current_pos, positions[collisions[-3]])]
            print(connecting_vec)
            if connecting_vec[0] == 0:
                if connecting_vec[1] >= 0:
                    connecting_map = map[current_pos[0]][current_pos[1]:positions[collisions[-3]][1]]
                else:
                    connecting_map = map[current_pos[0]][positions[collisions[-3]][1]:current_pos[1]]
            elif connecting_vec[1] == 0:
                if connecting_vec[0] >= 0:
                    connecting_map = [row[current_pos[1]] for row in map[current_pos[0]:positions[collisions[-3]][0]]]
                else:
                    connecting_map = [row[current_pos[1]] for row in map[positions[collisions[-3]][0]:current_pos[0]]]
            if not "#" in connecting_map:
                obstructions += 1
        positions.append(current_pos)
except IndexError:
    map_string = "".join(["".join(l) for l in map])
    total = len(re.findall("X", map_string)) + 1
    print(total)
    print(obstructions)
