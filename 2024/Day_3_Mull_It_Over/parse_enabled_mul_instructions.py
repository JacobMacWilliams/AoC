import re

corrupted_instructions = open("input.txt", "r").readlines()
total = 0
do = r"do\(\)"
dont = r"don't\(\)"
mul = r"mul\((\d{1,3}),(\d{1,3})\)"

search_string = "".join(corrupted_instructions)

start = 0

# Find first substring to search
dont_match = re.search(dont, search_string)
if dont_match:
    stop = dont_match.start()
else:
    stop = len(search_string)

while stop <= len(search_string):
    # Search first sub string
    enabled_string = search_string[start:stop]
    total += sum([int(x[0]) * int(x[1]) for x in re.findall(mul, enabled_string)])

    # find start of next sub string
    do_match = re.search(do, search_string[stop:])
    if do_match:
        start = do_match.end() + stop
    else:
        break
    
    dont_match = re.search(dont, search_string[start:])
    if dont_match:
        stop = dont_match.start() + start
    else:
        stop = len(search_string)

print(total)
