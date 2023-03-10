"""
Luke Jarvis
3/8/23
"""
import random


class Tree:

    def __init__(self, key: str) -> None:
        self.key = key
        self.nodes = []

    def add_node(self, key: str) -> None:
        self.nodes.append(Tree(key))


def build_tree(node: Tree, rules: dict) -> None:
    key = node.key
    # checks if node's rule is in rules
    if key in rules:
        for child in rules.get(key):
            node.add_node(child)
    # checks if node's rule is concatenated
    elif ' ' in key:
        for child in key.split(' '):
            node.add_node(child)
    for child in node.nodes:
        # recursive step build_tree for each child
        build_tree(child, rules)


# calls _generate and returns generated sentence as a string
def sentence_generator(root: Tree, interations: int) -> None:
    # recursive nested function populates terminals with terminal values
    def fill_terminals(node: Tree, terminals: list) -> bool:
        # if node has children
        if len(node.nodes) > 0:
            # if node is a compound rule
            if ' ' in node.key:
                # for each rule in the compound
                for child in node.nodes:
                    # recursive step for each child node
                    if fill_terminals(child, terminals):
                        terminals.append(child.key)
            else:
                # recursive step for random choice
                if fill_terminals(rand := random.choice(node.nodes), terminals):
                    terminals.append(rand.key)
        else:
            return True

    print('Randomly generated sentences:')
    for i in range(interations):
        fill_terminals(root, sentence := [])
        # formats sentence as string
        print(' '.join(sentence).capitalize() + '.')


cfg: dict[str, tuple] = {
    'S': ('NP VP',), 'NP': ('Det N', 'Det Adj N'), 'VP': ('V NP', 'V Adv Pre NP', 'V'), 'Det': ('the', 'a', 'my'),
    'N': ('dog', 'cat', 'bird'), 'V': ('chased', 'ate', 'sang', 'barked'), 'Adj': ('fat', 'lazy', 'red'),
    'Adv': ('quickly', 'quietly', 'loudly', 'rudely'), 'Pre': ('after', 'around', 'at')
}
rule_tree = Tree('S')
build_tree(rule_tree, cfg)
sentence_generator(rule_tree, 10)
