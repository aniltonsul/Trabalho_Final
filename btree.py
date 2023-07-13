from leitura import read_csv_file

class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.values = []
        self.children = []
        self.leaf = leaf

    def insert(self, key, value):
        if self.leaf:
            self._insert_leaf(key, value)
        else:
            index = 0
            while index < len(self.keys) and key > self.keys[index]:
                index += 1
            self.children[index].insert(key, value)

    def _insert_leaf(self, key, value):
        index = 0
        while index < len(self.keys) and key > self.keys[index]:
            index += 1
        self.keys.insert(index, key)
        self.values.insert(index, value)

    def search(self, key):
        index = 0
        while index < len(self.keys) and key > self.keys[index]:
            index += 1
        if index < len(self.keys) and key == self.keys[index]:
            return self.values[index]
        elif self.leaf:
            return None
        else:
            return self.children[index].search(key)

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(leaf=True)
        self.t = t

    def insert(self, key, value):
        if len(self.root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode()
            new_root.children.append(self.root)
            self.root = new_root
            self._split_child(self.root, 0)
        self._insert_non_full(self.root, key, value)

    def _insert_non_full(self, node, key, value):
        index = len(node.keys) - 1
        if node.leaf:
            node.insert(key, value)
        else:
            while index >= 0 and key < node.keys[index]:
                index -= 1
            index += 1
            if len(node.children[index].keys) == (2 * self.t) - 1:
                self._split_child(node, index)
                if key > node.keys[index]:
                    index += 1
            self._insert_non_full(node.children[index], key, value)

    def _split_child(self, parent, index):
        node = parent.children[index]
        new_node = BTreeNode(leaf=node.leaf)
        parent.keys.insert(index, node.keys[self.t - 1])
        parent.values.insert(index, node.values[self.t - 1])
        parent.children.insert(index + 1, new_node)
        new_node.keys = node.keys[self.t:]
        new_node.values = node.values[self.t:]
        node.keys = node.keys[:self.t - 1]
        node.values = node.values[:self.t - 1]
        if not node.leaf:
            new_node.children = node.children[self.t:]
            node.children = node.children[:self.t]

    def search(self, key):
        return self.root.search(key)

def create_btree(columns):
    btree = BTree(t=3)  # t is the minimum degree of the B-tree
    for row in columns:
        btree.insert(row[0], row[1])
    return btree

def search_city_cep(btree):
    cidade = input("Digite o nome de uma cidade: ")
    result = btree.search(cidade)
    if result is not None:
        print("O CEP da cidade de {} é {}".format(cidade, result))
    else:
        print("Cidade não encontrada.")

columns = read_csv_file()
btree = create_btree(columns)
search_city_cep(btree)
