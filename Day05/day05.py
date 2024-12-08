texts = open('../Inputs/Input05.txt').read().split('\n\n')
rules = sorted([[rule.split("|")[0], rule.split("|")[1]] for rule in texts[0].splitlines()])
updates = texts[1].splitlines()

def create_graph(ruleset):
    graph = {rule[0]: [] for rule in ruleset}
    for r in ruleset:
        graph[r[0]].append(r[1])

    return graph

def apply_graph(unsorted_update, graph):
    result = []
    for idx, number in enumerate(unsorted_update):
        result.append(number)
        if idx == 0:
            continue

        for number_before in result[:]:
            if number in graph:
                if number_before in graph[number]:
                    result[-1], result[result.index(number_before)] = number_before, number
                    return apply_graph(result + unsorted_update[idx+1:], graph)

    return result

graph = create_graph(rules)
print(rules)
print(graph)
total = 0
for update in updates:
    update = update.split(",")
    r = apply_graph(update, graph)
    if r != update:
        print(r, "Result Number: ", int(r[int(len(r)/2)]))
        total += int(r[int(len(r)/2)])
print("Total: ", total)
