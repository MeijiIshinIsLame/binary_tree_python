class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data 

    def insert(self, data):
        
        if (data <= self.data):

            if(self.hasleft()):
                self.left.insert(data)
            else:
                self.left = Node(data)

        elif (data > self.data):

            if(self.hasright()):
                self.right.insert(data)
            else:
                self.right = Node(data)
                
    def hasleft(self):
        if self.left is not None:
            return True
        return False

    def hasright(self):
        if self.right is not None:
            return True
        return False
    

def height(node):

    #highest one of these two will be returned
    i_left = 0
    i_right = 0

    #if has left, incriment and recursively move left
    if node.hasleft():
        i_left += height(node.left)
        i_left += 1

    #if has right, incriment and recursively move left
    if node.hasright():
        i_right += height(node.right)
        i_right += 1

    #return the higher value
    return max(i_left, i_right)


def find_level(node, data):
    
    #highest one of these two will be returned
    i_left = 0
    i_right = 0
    
    #root is level 0
    if node.data == data:
        return 0

    #if has left, incriment and recursively move left
    if node.hasleft():
        i_left = find_level(node.left, data)

        if node.left.data == data:
            return i_left + 1
        
    #if has right, incriment and recursively move left
    if node.hasright():
        i_right = find_level(node.right, data)

        if node.right.data == data:
            return i_right + 1

     #just need this to loop tbh
    return 1 + max(i_left, i_right)

def get_max_nodes(level):
    return 2**level

def make2d_list(rows, cols):
    return [ ([0] * cols) for row in range(rows) ]

def create_matrix(node):
    x = get_max_nodes(height(node)) * 2
    x += x-1 #spaces inbetween
    
    y = height(node) * 2

    #y starts at 0, so add 1
    return make2d_list(y + 1, x)
    

def populate_matrix(node, matrix, xpos, ypos):

    print("xpos:", xpos, "ypos:", ypos, "data: ", node.data)

    matrix[ypos][xpos] = node.data

    if node.hasleft():
        matrix[ypos+1][xpos-1] = ","
        populate_matrix(node.left, matrix, xpos-2, ypos+2)

    if node.hasright():
        matrix[ypos+1][xpos+1] = "`"
        populate_matrix(node.right, matrix, xpos+2, ypos+2)

    return matrix

def prettify_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i][j] = " "
    return matrix
        

#data = [2, 1, 3, 4, 5, 6]            
data = [50, 30, 24, 5, 28, 45, 98, 52, 60]

root = Node(data[0])
data.pop(0)

print(data)
print("")
print("")

for num in data:
    root.insert(num)
    
xpos = get_max_nodes(height(root))
ypos = 0 #start at level 0

print("node height", height(root))
print("level", find_level(root, 4))
print("mex nodes", get_max_nodes(height(root)))
matrix = create_matrix(root)

matrix = populate_matrix(root, matrix, xpos, ypos)

matrix = prettify_matrix(matrix)

for row in matrix:
    string = ""
    for i in range(len(row)):
        string += str(row[i])
    print(string)
