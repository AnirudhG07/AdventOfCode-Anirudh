test_input = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
## Split the input in two parts based on the empty line
rules, updates = {}, []
with open("day5.txt") as f:
    input = f.read()
for rule in input.split("\n"):
    if rule == "":
        continue
    if "|" in rule:
        key, value = map(int, rule.split("|"))
        if key not in rules:
            rules[key] = []
        rules[key].append(value)
    else:
        updates.append(list(map(int, rule.split(","))))

## Part 1
def part_1(rules, updates):
    wrong_updates = []
    def check(x, y):
        if x in rules:
            if y in rules[x]:
                return True
        return False

    for update in updates:
        for i in range(len(update) - 1):
            for j in range(i + 1, len(update)):
                if not check(update[i], update[j]):
                    if update not in wrong_updates:
                        wrong_updates.append(update)
                    break
    return wrong_updates

def sum_middles(wrong_updates):
    sum = 0
    for update in updates:
        if update in wrong_updates:
            continue
        middle = len(update) // 2
        sum += update[middle]
    return sum

print(sum_middles(part_1(rules, updates)))

def part_2(rules, updates):
    wrong_updates = part_1(rules, updates)


