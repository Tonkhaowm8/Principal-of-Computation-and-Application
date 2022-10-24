# Siraphop Mukdaphetcharat 64011614

from itsdangerous import NoneAlgorithm
from matplotlib.pyplot import prism


class Node: 
    def __init__(self, username_in, password_in): 
        # your code here 
        self.username = username_in
        self.password = password_in
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
        if (new_node.username <= current_node.username): 
            if (current_node.left is not None): 
                self.__insert_node(current_node.left, new_node) 
            else: 
                current_node.left = new_node 
        elif (new_node.username > current_node.username): 
            if (current_node.right is not None): 
                self.__insert_node(current_node.right, new_node) 
            else: 
                current_node.right = new_node 
 
    def find(self, username): 
        return self.__find_node(self.root, username) 
 
    def __find_node(self, current_node, username):
        if current_node.username != username:
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
 
    #def find_min(self):


    def remove(self, username): 
        return self.removeNode(self, self.root, username)

    def removeNode(self, current_node, username):
        if current_node.username != username:
            if current_node.left != None:
                a = self.__find_node(current_node.left, username)
                if a != None:
                    return a
                if current_node.right != None:
                    return self.__find_node(current_node.right, username)
            if current_node.right != None:
                return self.__find_node(current_node.right, username)
        else:
            if current_node.left == None and current_node.right == None:
                current_node.username = None
                current_node.password = None
            #elif current_node.left != None and current_node.right != None:

 
    def is_empty(self): 
        return self.head.left == None and self.head.right == None
 
    #def preorder(self): 
        # your code here 
 
    #def inorder(self): 
        # your code here 
 
    #def postorder(self): 
        # your code here 
 
    def print(self):
        return self.printNode(self.root)

    def printNode(self, node):
        print(node.username)
        if node.left != None:
            self.printNode(node.left)
        if node.right != None:
            self.printNode(node.right)
    
    def printTree(self):
        return self.printTreee(self.root, 0)

    def printTreee(self, node, level):
        if node != None:
            level += 1
            self.printTreee(node.right, level)
            print(" " * level * 15 + str([node.username, node.password])+ "\n")
            level += 1
            self.printTreee(node.left, level)



binaryTree = BST()
f = open('users7.txt')
credentials = f.read()
creArr = credentials.split('\n')
for i in creArr:
    cret = i.split(" ")
    username = cret[0]
    password = cret[1]
    newNode = Node(username, password)
    binaryTree.insert(newNode)

binaryTree.printTree()
#print(binaryTree.find("panya").username)