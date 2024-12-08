texts = open('../Inputs/TestInput05.txt').read().split('\n\n')
rules = sorted([[rule.split("|")[0], rule.split("|")[1]] for rule in texts[0].splitlines()])
updates = texts[1].splitlines()

def connect_rules(rule_list, current_rule):
    if not rule_list:
        return current_rule
    for rule in rule_list:
        for idx, number in enumerate(current_rule):
            if number == rule[0]:
                print(current_rule, "\n")
                print("ADDING:", rule_list[0])

                new_rule = current_rule

                if rule[1] in current_rule:
                    new_rule.remove(rule[0])
                    new_rule.insert(new_rule.index(rule[1]), rule[0])
                else:
                    new_rule.insert(idx + 1, rule[1])

                return connect_rules(rule_list[1:], new_rule)

            # if number == rule[1]:
            #     print(current_rule)
            #     print("ADDING:", rule_list[0])

            #    new_rule = current_rule
            #    return connect_rules(rule_list[1:], new_rule)

    new_rule = current_rule + rule_list[0]
    return connect_rules(rule_list[1:], new_rule)

def sort_update(update_to_sort, ruleset):
    result = []
    for r in ruleset:
        if r in update_to_sort:
            result.append(r)
    return result


connected_rules = connect_rules(rules[1:], rules[0])
print(connected_rules)
print("\n")
for update in updates:
    print("\n")
    print("OLD:", update)
    print(sort_update(update.split(","), connected_rules))

