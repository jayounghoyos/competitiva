def clasify_nodes(graph):
    classification = {k: 0 for k in range(len(graph))}
    for node, edges in graph.items():
        if len(edges) == 1:
            classification[node] = 2
        else:
            for neir in edges:
                if len(graph[neir]) == 1:
                    classification[node] = 1
                    break
    return classification


def solve(vertices, edges):
    graph = {k: [] for k in range(vertices)}
    for _ in range(edges):
        from_, to = map(int, input().split())
        from_ -= 1
        to -= 1
        graph[from_].append(to)
        graph[to].append(from_)

    classification = clasify_nodes(graph)
    center = -1
    any_not_leaf = -1

    for node, score_classification in classification.items():
        if score_classification == 0:
            center_node = node
        elif score_classification == 1:
            any_not_leaf = node

        if center != -1 and any_not_leaf != -1:
            break

    x = len(graph[center_node])
    y = len(graph[any_not_leaf]) - 1
    print(f"{x} {y}")


def main():
    test_cases = int(input())
    while test_cases > 0:
        vertices, edges = map(int, input().split())
        solve(vertices, edges)
        test_cases -= 1


main()
