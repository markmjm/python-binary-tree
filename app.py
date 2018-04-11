from node import Node
from binary_tree import BinaryTree

tree = BinaryTree( Node(9))
tree.add( Node(5))
tree.add( Node(11))
tree.inorder()
tree.preorder()

print(tree.find(11))
print('==================================')
print('==================================')
print('==================================')
print('==================================')
tree2 = BinaryTree(Node(6))
nodes = [5,3,9,7,8,7.5,12,11]
for n in nodes:
    tree2.add(Node(n))

tree2.delete(9)
tree2.inorder()




