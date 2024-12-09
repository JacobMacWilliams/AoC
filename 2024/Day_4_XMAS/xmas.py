from time import sleep
#### TESTS ###
# 1 xmas
lines_1 = [
            "XMAS",
            "ASXM",
            "MSSA",
            "SMSA"
        ]

# 2 xmas
lines_2 = [
            "XMAS",
            "AMXM",
            "MSAA",
            "SMSS"
        ]

# 1 xmas
lines_3 = [
            "XMAX",
            "ASMM",
            "MASA",
            "SMSA"
        ]

def xmas_finder_4by4(lines: list[str]) -> int:
    assert len(lines) == 4
    assert all([len(s) == 4 for s in lines])
    
    count = 0
    
    valid_cols: set[int] = {i for i in range(4)} 
    valid_rows: set[int] = {i for i in range(4)}
    valid_diag: set[int] = {i for i in range(2)}
    for i, j in [(1,1),(1,2),(2,1),(2,2)]:
        if lines[i][j] == "X" or lines[i][j] == "S":
            valid_rows.difference_update({i})
            valid_cols.difference_update({j})
            valid_diag.difference_update({i != j})
            
    for i in valid_rows:
        word = lines[i]
        if word == "XMAS" or word == "SAMX":
            count += 1

    for j in valid_cols:
        word = "".join([l[j] for l in lines])
        if word == "XMAS" or word == "SAMX":
            count += 1
    
    for i in valid_diag:
        if i == 0:
            word = "".join([l[i] for i, l in enumerate(lines)])
        elif i == 1:
            word = "".join([l[3 - i] for i, l in enumerate(lines)])
        if word == "XMAS" or word == "SAMX":
            count += 1
    return count

def xmas_simple_finder_4by4(lines: list[str]) -> int:
    assert len(lines) == 4
    assert all([len(s) == 4 for s in lines])
    count = 0
    for i in range(4):
        word = lines[i]
        if word == "XMAS" or word == "SAMX":
            count += 1

    for j in range(4):
        word = "".join([l[j] for l in lines])
        if word == "XMAS" or word == "SAMX":
            count += 1
    
    for i in range(2):
        if i == 0:
            word = "".join([l[k] for k, l in enumerate(lines)])
        elif i == 1:
            word = "".join([l[3 - k] for k, l in enumerate(lines)])
        if word == "XMAS" or word == "SAMX":
            count += 1
    return count

# print("------------------------")
# print(xmas_finder_4by4(lines_1))
# print("------------------------")
# print(xmas_finder_4by4(lines_2))
# print("------------------------")
# print(xmas_finder_4by4(lines_3))

input = open("input.txt", "r").readlines()
lines = [l.rstrip() for l in input]
total = 0
for i in range(len(lines) - 3):
    for j in range(len(lines[0]) - 3):
        block = [l[j:j+4] for l in lines[i:i+4]]
        total += xmas_simple_finder_4by4(block)
print(total) 
