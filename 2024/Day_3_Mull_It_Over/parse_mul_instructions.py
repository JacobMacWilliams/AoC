import re

# I cheated here, I don't know regex so the commented out query is what\
# I came up with reading through the docs, but for whatever reason this did
# not give me all of the matches. Don't know why still. In the end I just stole
# the regex string from another answer and learned about capture groups and
# the digit symbol \d

corrupted_instructions = open("input.txt", "r").readlines()
total = 0
for instruction in corrupted_instructions:
    mul = r"mul\((\d{1,3}),(\d{1,3})\)"
    #mul = 'mul[(][1-9]*,[1-9]*[)]'
    matches = re.findall(mul, instruction)
    for match in matches:
        total += int(match[0]) * int(match[1])
        # nums = match[4:-1].split(',')
        # total += int(nums[0])*int(nums[1])

print(total)
