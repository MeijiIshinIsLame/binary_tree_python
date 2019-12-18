

class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.node_count = 1
        matrix_width = 0


    def insert(self, data):
        
        if (data <= self.data):
            
            if(self.left is None):
                self.left = Node(data)
                self.node_count += 1
            else:
                self.node_count += 1
                self.left.insert(data)
                
        elif (data > self.data):

            if(self.right is None):
                self.right = Node(data)
                self.node_count += 1
            else:
                self.node_count += 1
                self.right.insert(data)
                

    def get_matrix_width(self, matrix_w):

        if self.left is None and self.right is None:
                return matrix_w
        elif self.left is not None:
            self.get_matrix_width(matrix_w + 1)
        else:
            self.get_matrix_width(matrix_w + 1)
                
           
        
            
data = [10, 5, 8, 19, 24, 43, 2, 32, 99, 13, 14, 12, 9]            

root = Node(data[0])
data.pop(0)

print(data)
print("")
print("")

for num in data:
    root.insert(num)

print(root.get_matrix_width(0))
        
            
