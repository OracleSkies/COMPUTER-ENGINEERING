class HashMap:
    def __init__(self, size = 10):
        self.table = [[] for _ in range(size)]
        self.size = size
        self.count = 0