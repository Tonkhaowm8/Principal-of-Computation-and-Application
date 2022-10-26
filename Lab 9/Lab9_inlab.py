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
 
    def find_min(self, node):
        if node.left != None:
            return self.find_min(node.left)
        else:
            return node


    def remove(self, username): 
        removeNode = self.find(username)
        # case 1, no child
        if removeNode.left == None and removeNode.right == None:
            removeNode.username = None
            removeNode.password = None

        # case 2, 2 child
        elif removeNode.left != None and removeNode.right != None:
            inorder = self.find_min(removeNode.right)
            inUsername = inorder.username
            inPassword = inorder.password
            inorder.username = None
            inorder.password = None
            removeNode.username = inUsername
            removeNode.password = inPassword

        #case 3, 1 child
        else:
            try:
                removeNode.username = removeNode.left.username
                removeNode.password = removeNode.left.password
                removeNode.left = removeNode.left.left
                removeNode.right = removeNode.left.right
            except:
                removeNode.username = removeNode.right.username
                removeNode.password = removeNode.right.password
                removeNode.left = removeNode.right.left
                removeNode.right = removeNode.right.right
            
            
 
    def is_empty(self, node): 
        return node.left == None or node.right == None
 
    def preorder(self, node): 
        if node == None:
            return 0
        print(node.username)
        self.preorder(node.left)
        self.preorder(node.right)
 
    def inorder(self, node): 
        if node == None:
            return
        self.inorder(node.left)
        print(node.username)
        self.inorder(node.right)
 
    def postorder(self, node): 
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.username) 
    
    def print(self):
        return self.printNode(self.root, 0)

    def printNode(self, node, level):
        if node != None:
            level += 1
            self.printNode(node.right, level)
            if node.username != None:
                print(" " * level * 15 + str([node.username, node.password])+ "\n")
            level += 1
            self.printNode(node.left, level)

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

#print("------------------------------------------------------original-------------------------------------------------------------------")
#binaryTree.print()
#print("-------------------------------------------------------removed-------------------------------------------------------------------")
#binaryTree.remove('sandy')
#binaryTree.preorder(binaryTree.root)
#binaryTree.inorder(binaryTree.root)
#binaryTree.postorder(binaryTree.root)
#binaryTree.print()
#print(binaryTree.find("panya").username)