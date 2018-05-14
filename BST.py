class BinarySearchTree:
    def __init__(self):
        """
        Creates a Binary Search Tree object, initializing all class attributes to None
        """
        self._value = None
        self._left = None
        self._right = None
    
    
    def add(self, value):
        """
        Adds a value to a Binary Search Tree object
        """
        if self._value == None: #if there are no nodes in the Tree
            
            self._value = value
            
        else:
            
            if value > self._value: #if the value is greater than our current Node's value
                
                if self._right == None: #if reference to right Node is None
                    
                    self._right = BinarySearchTree() #creates that right Node
                    
                self._right.add(value) #recursively adds that value to the right Node
                
            elif value < self._value: #the mirror of the above lines of code
                
                if self._left == None:
                    
                    self._left = BinarySearchTree()
                
                self._left.add(value)
    
    def find(self, value):
        """
        Finds the Node that contains the value in the parameter and returns that Node
        """
        if self._value == None: #if the value is not present in our BST
            return None
            
        else:
            if self._value == value: #once we actually find our Node
                return self
                
            if self._value > value: #recursively finds our value using the right Node
                return self._left.find(value)
                
            elif self._value < value:#recursively finds our value using the left Node
                return self._right.find(value)
    
    def __str__(self):
        # a String representation of our Binary Search Tree
        
        if self._value == None:
            return None
            
        else:
            return "({:d} {} {})".format(self._value, str(self._left), str(self._right))
