
import re

def parse_input(input: list[str]):
    rule = r"(\d{1,3})\|(\d{1,3})"
    rules = [re.search(rule, line) for line in input]
    updates = [input[i].strip().split(',') for i, _ in enumerate(rules) if not _]
    updates = [[int(n) for n in update] for update in updates]
    rules = [(int(rule[1]), int(rule[2])) for rule in rules if rule]
    return rules, updates

def valid_rule(update: list[int]):
    violations: list[tuple[int,int]] = []
    for i in range(1,len(update)):
        n = update[i]
        ordered_nums = update[:i]
        for m in ordered_nums:
            violations.extend([rule for rule in rules if rule == (n, m)])
    return violations

def rule_fix_step(update: list[int], rule: tuple[int, int]) -> list[int]:
    n = rule[0]
    m = rule[1]
    n_idxs = [i for i, _ in enumerate(update) if _ == n]
    n_idxs.sort()

    m_idxs = [i for i, _ in enumerate(update) if _ == m]
    m_idxs.sort()

    n_idx = n_idxs[0]
    m_idx = m_idxs[0]
    tmp = update[n_idx]
    update[n_idx] = update[m_idx]
    assert tmp != update[n_idx]
    update[m_idx] = tmp
    return update
    
input = open("input.txt", "r").readlines()
input = [l.strip() for l in input]
rules, updates = parse_input(input)

total = 0
for update in updates:
    assert (len(update) % 2) == 1
    violations = valid_rule(update)
    if violations:
        while violations:
            for rule in violations:
                update = rule_fix_step(update, rule)
            violations = valid_rule(update)

        total += update[len(update) // 2]

print(total)
