class Node:
    def __init__(self, key):
        self.val = key
        self.children = []
        
    def numChild(self):
        return len(self.children)

def minChild(root):
    node = Node(root)
    minVal = node.numChild()
    for child in node.children:
        minVal = min(minVal,)
def add_child(root, key):
    child = Node(key)
    root.children.append(child)
    return child

def preorder(root):
    print(root.val, end=' ')
    for child in root.children:
        preorder(child)

def postorder(root):
    for child in root.children:
        postorder(child)
    print(root.val, end=' ')

def level_order(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=' ')
        queue.extend(node.children)

def height(node):
    if node is None:
        return 0
    if not node.children:
        return 1
    return 1 + max(height(child) for child in node.children)

def find_minimum(root):
    min_val = root.val
    for child in root.children:
        min_val = min(min_val, find_minimum(child))
    return min_val

def find_maximum(root):
    max_val = root.val
    for child in root.children:
        max_val = max(max_val, find_maximum(child))
    return max_val

def is_balanced(root):
    def check_balance(node):
        if node is None:
            return 0, True
        if not node.children:
            return 1, True
        heights = []
        for child in node.children:
            height, balanced = check_balance(child)
            if not balanced:
                return 0, False
            heights.append(height)
        return max(heights) + 1, all(abs(h - heights[0]) <= 1 for h in heights)
    _, balanced = check_balance(root)
    return balanced

root = Node("Rosa")

grand1 = add_child(root, "Egliciria")


add_child(grand1,"Dionisio")
add_child(grand1,"Francisca")
parent = add_child(grand1,"Mercedita")
add_child(grand1,"Serafin")
add_child(grand1,"Arnel")

add_child(parent, "Jomer")
add_child(parent, "Hazel")

print("===PREORDER===")
print(preorder(root))
print()
print("===POSTORDER===")
print(postorder(root))
print()
print("===LEVEL ORDER===")
print(level_order(root))
print()
print("===TREE HEIGHT===")
print(height(root))
print()
print("===TREE BALANCE===")
print(is_balanced(root))
print()
print("===MAXIMUM VALUE===")
print(find_maximum(root))
print("===MINIMUM VALUE===")
print(find_minimum(root))

