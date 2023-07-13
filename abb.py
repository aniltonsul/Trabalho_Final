from leitura import read_csv_file

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, value)
            else:
                self._insert_recursive(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, value)
            else:
                self._insert_recursive(node.right, key, value)
        else:
            # Key already exists, update the value
            node.value = value

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

def create_binary_search_tree(columns):
    bst = BinarySearchTree()
    for row in columns:
        bst.insert(row[0], row[1])
    return bst

def search_city_cep(bst):
    cidade = input("Digite o nome de uma cidade: ")
    result = bst.search(cidade)
    if result is not None:
        print("O CEP da cidade de {} é {}".format(cidade, result.value))
    else:
        print("Cidade não encontrada.")

columns = read_csv_file()
bst = create_binary_search_tree(columns)
search_city_cep(bst)
