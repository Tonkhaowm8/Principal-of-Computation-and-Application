class Node: 
    def __init__(self, data): 
        # your code here 
        self.data = data
        self.left = None 
        self.right = None 

class BST:
    def __init__(self): 
        self.root = None 
 
    def insert(self, new_node): 
        if (self.root is None): 
            self.root = new_node 
        else: 
            self.__insert_node(self.root, new_node) 
 
    def __insert_node(self, current_node, new_node): 
        if (new_node.data <= current_node.data): 
            if (current_node.left is not None): 
                self.__insert_node(current_node.left, new_node) 
            else: 
                current_node.left = new_node 
        elif (new_node.data > current_node.data): 
            if (current_node.right is not None): 
                self.__insert_node(current_node.right, new_node) 
            else: 
                current_node.right = new_node

    def find(self, username): 
        return self.__find_node(self.root, username) 
 
    def __find_node(self, current_node, username):
        if current_node.data != username:
            if current_node.left != None:
                a = self.__find_node(current_node.left, username)
                if a != None:
                    return a
                if current_node.right != None:
                    return self.__find_node(current_node.right, username)
            if current_node.right != None:
                return self.__find_node(current_node.right, username)
        else:
            return current_node
 
    def find_min(self, node):
        if node.left != None:
            return self.find_min(node.left)
        else:
            return node


    def remove(self, data): 
        removeNode = self.find(data)
        # case 1, no child
        if removeNode.left == None and removeNode.right == None:
            removeNode.data = None

        # case 2, 2 child
        elif removeNode.left != None and removeNode.right != None:
            inorder = self.find_min(removeNode.right)
            inData = inorder.data
            try:
                inorder.data = inorder.left.data
                inorder.right = inorder.left.right
                inorder.left = inorder.left.left
            except:
                inorder.data = inorder.right.data
                inorder.left = inorder.right.left
                inorder.right = inorder.right.right
            removeNode.data = inData

    def trim(self, min, max):
        return self.__trim(min, max, self.root)

    def __trim(self, min, max, node):
        if node.data > min:
            self.__trim(min, max, node.left)
            self.__trim(min, max, node.right)
        else:
            self.remove(node.data)

    def print(self):
        return self.printNode(self.root, 0)

    def printNode(self, node, level):
        if node != None:
            #level += 1
            self.printNode(node.right, level + 1)
            if node.data != None:
                print(" " * level * 5 + str(node.data)+ "\n")
            self.printNode(node.left, level + 1)

data = [8, 3, 1, 6, 4, 7, 10, 14, 13]
binaryTree = BST()
for i in data:
    binaryTree.insert(Node(i))

binaryTree.print()
print("----------------------------------------------------------------")
binaryTree.trim(5, 13)
binaryTree.print()