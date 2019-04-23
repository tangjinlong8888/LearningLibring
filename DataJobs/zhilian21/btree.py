class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BTree:
    def __init__(self, dataset):
        self.root = self.build_node(dataset, 1)

    @classmethod
    def build_node(cls, dataset, position):
        node = Node(dataset[position - 1])

        left_index = 2 * position
        right_index = 2 * position + 1

        if left_index <= len(dataset):
            node.left = cls.build_node(dataset, left_index)

        if right_index <= len(dataset):
            node.right = cls.build_node(dataset, right_index)

        return node

    def __iter__(self):
        def loop_tree(node):
            data = []
            while data:
                if node.left:
                    data.append(node.right)
                else:
                    data.append(node.left)
            yield node.data
            # if node.left:
            #     for d in loop_tree(node.left):
            #         print('d=', d)
            #         # if node.right:
            # if node.right:
            #     for m in loop_tree(node.right):
            #         print('m=',m)

            yield node.data

        return loop_tree(self.root)

tree = BTree((1, 2, 3, 4, 5, 6, 7, 8, 9))
for data in tree:
    print(data)

