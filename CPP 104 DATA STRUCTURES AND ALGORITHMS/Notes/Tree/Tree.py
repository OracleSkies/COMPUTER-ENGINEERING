class Node:
    def __init__(self, key):
        self.val = key
        self.children = []

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

#==== OUTPUT ====
#Level 1
root = Node(1)
child1 = add_child(root, 2)
child2 = add_child(root, 3)
child3 = add_child(root, 4)

#Level 2
add_child(child1, 5)
add_child(child1, 6)

#Level 3
add_child(child2, 7)

print("===PREORDER===")
print(preorder(root))
print()
print("===POSTORDER===")
print(postorder(root))
print()
print("===LEVEL ORDER===")
print(level_order(root))
print()
print()
print("===MAXIMUM VALUE===")
print(find_maximum(root))
print()
print("===MINIMUM VALUE===")
print(find_minimum(root))
print()
print("===TREE HEIGHT===")
print(height(root))
print()
print(f"Is the tree balanced?: {is_balanced(root)}")
