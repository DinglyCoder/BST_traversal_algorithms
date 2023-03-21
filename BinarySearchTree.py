''' Akshat Kumar
Binary Search Tree Implementation 9/9/2022
This program implements a binary search tree using a tree class and a node class.
The program can insert nodes as well as travers in inorder, preorder, and postorder.
'''

#node class that defines a single node
class treeNode:
    
    #node constructor
    def __init__(self, initData, initLeft, initRight, initParent):
        self.data = initData
        self.left = initLeft
        self.right = initRight
        self.parent = initParent        

#Tree class that has node class as attribute
class tree:
    
    #tree class constructor
    def __init__(self, initRoot):
        self.root = treeNode(initRoot, None, None, None)
        
    #insert function that sets node as root if there is none or calls addNode function
    def insertNode(self, value):
        #initializing a temp node to store value to be inserted
        newNode = treeNode(value, None, None, None)
        
        #if there is no root, make new node root
        if(self.root == None):
            self.root = newNode
        
        #else call other unction to add new node
        else:
            tree.addNode(self, self.root, newNode)
    
    #addNode function that adds node if there is a root      
    def addNode(self, c, newNode):
        #initialize the parent of the new node as the current candidate (c)
        newNode.parent = c.data
        
        #if the candidate has no children
        if(c.left == None and c.right == None):
            #new node is smaller, insert into left
            if(newNode.data < c.data):
                c.left = newNode
            #new node is larger, insert into right
            elif(newNode.data > c.data):
                c.right = newNode
        
        #if the candidate has no children on the left and the node is smaller, insert node
        elif(c.left == None and newNode.data < c.data):
            c.left = newNode
            
        #if the candidate has no children on the right and the node is larger, insert node    
        elif(c.right == None and newNode.data > c.data):
            c.right = newNode
        
        #recursively call function with left as the new candidate
        elif(newNode.data < c.data):
            tree.addNode(self, c.left, newNode)
            
        #recursively call function with right as the new candidate
        elif(newNode.data > c.data):
            tree.addNode(self, c.right, newNode)
        
    #preorder traversal that follows Visit,Left,Right pattern
    def preOrder(self, c):
        print(c.data)
        if(c.left != None):
            tree.preOrder(self, c.left)
        if(c.right != None):
            tree.preOrder(self, c.right)
     
    #preorder traversal that follows Left,Visit,Right pattern
    def inOrder(self, c):
        if(c.left != None):
            tree.inOrder(self, c.left)
        print(c.data)
        if(c.right != None):
            tree.inOrder(self, c.right)
        
    #preorder traversal that follows Left,Right,Visit pattern
    def postOrder(self, c):
        if(c.left != None):
            tree.postOrder(self, c.left)
        if(c.right != None):
            tree.postOrder(self, c.right)
        print(c.data)
    '''    
    def findNode(self, c, value):
        if(c.left != None):
            tree.inOrder(self, c.left)
        if(c.right != None):
            tree.inOrder(self, c.right)
        if(c.getData() == value):
            return c
        
    def deleteNode(self, value):
        c = tree.findNode(self, self.root, value)
        if(c.left == None and c.right == None):
            del(c)
    '''
    def __str__(self):
        return "root is " + str(self.root)      
        
#constructing the tree with root of 8 
testTree = tree(8)
#inserting nodes into the tree
testTree.insertNode(5)
testTree.insertNode(10)
testTree.insertNode(9)
testTree.insertNode(11)
testTree.insertNode(3)
testTree.insertNode(1)
testTree.insertNode(2)

#displaying tree values in three traversal methods
print("In Order: ")
testTree.inOrder(testTree.root)
print()
print("Pre order: ")
testTree.preOrder(testTree.root)
print()
print("Post order: ")
testTree.postOrder(testTree.root)


#testTree.deleteNode(4)

        
    