# https://www.codewars.com/kata/recover-a-secret-string-from-random-triplets/train/python


def get_adjacency_list(triplets):
    # this function returns an adgacency list from triplets.
    # each triplet [a, b, c] means that:
    # a is father of b, and grand father of c (a->b), (a->c)
    # and b is father of c (b->c)
    adjacency_list = {}
    for triplet in triplets:
        grand_pa = triplet[0]
        father = triplet[1]
        son = triplet[2]

        if grand_pa not in adjacency_list:
            adjacency_list[grand_pa] = set()
        if father not in adjacency_list:
            adjacency_list[father] = set()

        adjacency_list[grand_pa].add(father)
        adjacency_list[grand_pa].add(son)
        adjacency_list[father].add(son)
    return adjacency_list


def get_orphan_nodes(graph):
    # this function returns a list of nodes in a graph that are orphans.
    # it means that they have no parents. So, there is no other node that
    # points to them
    has_parent = set()
    unique_nodes = set()
    for key in graph:
        childs = graph[key]
        unique_nodes.update(childs)
        unique_nodes.add(key)
        has_parent.update(childs)
    orphans = [node for node in unique_nodes if node not in has_parent]
    return orphans


def get_childs(dictionary, node, visited):
    if dictionary.get(node) is None:
        return []
    else:
        childs = [x for x in dictionary[node] if x not in visited]
    return childs


def topological_sort_dfs(graph, first_node):
    stack = []
    marked = []
    stack.append(first_node)
    answer = ""
    while stack:
        elem = stack[-1]
        if elem not in marked:
            hijos = get_childs(graph, elem, marked)
            if hijos == []:
                answer += elem
                marked.append(elem)
                stack.pop()
            else:
                stack = stack + hijos
        else:
            stack.pop()
    return answer[::-1]


def recoverSecret(triplets):
    # triplets is a list of triplets from the secrent string.
    # Return the string.
    adj_list = get_adjacency_list(triplets)

    # select the element with no parents
    first_node = get_orphan_nodes(adj_list)[0]  # there is just one orphan

    # apply dfs starting with the first elem
    secret_word = topological_sort_dfs(adj_list, first_node)

    return secret_word


if __name__ == "__main__":
    secret = "whatisup"
    triplets1 = [
      ['t', 'u', 'p'],
      ['w', 'h', 'i'],
      ['t', 's', 'u'],
      ['a', 't', 's'],
      ['h', 'a', 'p'],
      ['t', 'i', 's'],
      ['w', 'h', 's']
    ]

    triplets2 = [
        ['t', 's', 'f'],
        ['a', 's', 'u'],
        ['m', 'a', 'f'],
        ['a', 'i', 'n'],
        ['s', 'u', 'n'],
        ['m', 'f', 'u'],
        ['a', 't', 'h'],
        ['t', 'h', 'i'],
        ['h', 'i', 'f'],
        ['m', 'h', 'f'],
        ['a', 'u', 'n'],
        ['m', 'a', 't'],
        ['f', 'u', 'n'],
        ['h', 's', 'n'],
        ['a', 'i', 's'],
        ['m', 's', 'n'],
        ['m', 's', 'u']]
    print(recoverSecret(triplets2))
