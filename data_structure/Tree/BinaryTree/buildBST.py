import typing


class Node:

    def __init__(self, data: int):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data: int) -> None:
        if self.data:
            if data <= self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_node_DLR(self) -> None:
        print(self.data, end=" ")
        if self.left:
            self.left.print_node_DLR()
        if self.right:
            self.right.print_node_DLR()

    def print_node_LDR(self) -> None:
        if self.left:
            self.left.print_node_LDR()
        print(self.data, end=" ")
        if self.right:
            self.right.print_node_LDR()

    def print_node_LRD(self) -> None:
        if self.left:
            self.left.print_node_LRD()
        if self.right:
            self.right.print_node_LRD()
        print(self.data, end=" ")


root = Node(20)
root.insert(12)
root.insert(34)
root.insert(15)
root.insert(5)
root.insert(100)
print("DLR")
root.print_node_DLR()
print("\nLDR")
root.print_node_LDR()
print("\nLRD")
root.print_node_LRD()
