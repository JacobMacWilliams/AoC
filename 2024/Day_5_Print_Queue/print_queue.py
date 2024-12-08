import re

def parse_input(input: list[str]):
    rule = r"(\d{1,3})\|(\d{1,3})"
    rules = [re.search(rule, line) for line in input]
    updates = [input[i].strip().split(',') for i, _ in enumerate(rules) if not _]
    updates = [[int(n) for n in update] for update in updates]
    rules = [(int(rule[1]), int(rule[2])) for rule in rules if rule]
    return rules, updates

input = open("input.txt", "r").readlines()
input = [l.strip() for l in input]
rules, updates = parse_input(input)

total = 0
for update in updates:
    assert (len(update) % 2) == 1
    violations: list[tuple[int,int]] = []
    for i in range(1,len(update)):
        n = update[i]
        ordered_nums = update[:i]
        for m in ordered_nums:
            violations.extend([rule for rule in rules if rule == (n, m)])
    if not violations:
        total += update[len(update) // 2]
print(total)

