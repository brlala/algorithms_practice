class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # check first if there is a root value
        if self.root is None:
            self.root = Node(value)
        else:
            # _insert will be a recursive function
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._insert(value, current_node.left_child)

        elif value > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._insert(value, current_node.right_child)

        # if value exist, the logic is not to add it in
        else:
            print("Value exist!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
        else:
            print("Tree is empty.")

    def _print_tree(self, current_node):
        if current_node is not None:
            self._print_tree(current_node.left_child)
            print(str(current_node.value))
            self._print_tree(current_node.right_child)

    # checking the height of the tree
    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node is None:
            return current_height
        left_height = self._height(current_node.left_child, current_height + 1)
        right_height = self._height(current_node.right_child, current_height + 1)
        return max(left_height, right_height)

    # searching for a value
    def search(self, value):
        if self.root is not None:
            return self._search(self.root, value)
        else:
            return False

    def _search(self, current_node, value):
        if current_node.value == value:
            return True
        elif value < current_node.value and current_node.left_child is not None:
            return self._search(current_node.left_child, value)
        elif value > current_node.value and current_node.right_child is not None:
            return self._search(current_node.right_child, value)
        return False


def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)

    tree.insert(test_value)
    return tree


test_value = 1045
tree = binary_search_tree()
tree = fill_tree(tree)
tree.print_tree()
print("Tree height:", tree.height())
print("Value found for {}:".format(test_value), tree.search(test_value))
